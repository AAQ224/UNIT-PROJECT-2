
import json
from functools import lru_cache
from pathlib import Path

from django.http import Http404
from django.shortcuts import render


DATA_DIR = Path(__file__).resolve().parent / "data"


@lru_cache(maxsize=1)
def load_states():
    file_path = DATA_DIR / "states.json"

    with file_path.open("r", encoding="utf-8") as file:
        return json.load(file)


@lru_cache(maxsize=1)
def load_rulers():
    file_path = DATA_DIR / "rulers.json"

    with file_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def home(request):
    return render(request, "history/home.html")


def state_detail(request, era):
    states = load_states()
    state = states.get(era)

    if state is None:
        raise Http404("الدولة المطلوبة غير موجودة")

    # Add a URL slug based on each ruler's existing image filename.
    rulers = [
        {
            **ruler,
            "slug": Path(ruler["image"]).stem,
        }
        for ruler in state.get("rulers", [])
    ]

    return render(
        request,
        "history/state_detail.html",
        {
            "state": state,
            "era": era,
            "rulers": rulers,
        },
    )


def ruler_detail(request, slug):
    rulers_data = load_rulers()
    states = load_states()

    ruler = rulers_data.get(slug)

    if ruler is None:
        raise Http404("الحاكم المطلوب غير موجود")

    # Identify the state associated with this ruler.
    era = None
    state_title = None

    for state_slug, state in states.items():
        for state_ruler in state.get("rulers", []):
            image_slug = Path(state_ruler["image"]).stem

            if image_slug == slug:
                era = state_slug
                state_title = state["title"]
                break

        if era is not None:
            break

    if era is None:
        raise Http404("الحاكم غير مرتبط بدولة موجودة")

    return render(
        request,
        "history/ruler_detail.html",
        {
            "ruler": ruler,
            "era": era,
            "state_title": state_title,
        },
    )
