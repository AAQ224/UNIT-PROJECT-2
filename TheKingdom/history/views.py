
import json
from functools import lru_cache
from pathlib import Path

from django.http import Http404
from django.shortcuts import render


DATA_FILE = Path(__file__).resolve().parent / "data" / "states.json"


@lru_cache(maxsize=1)
def load_states():
    with DATA_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def home(request):
    states = load_states()

    return render(
        request,
        "history/home.html",
        {"states": states}
    )


def state_detail(request, era):
    states = load_states()

    state = states.get(era)

    if state is None:
        raise Http404("الدولة المطلوبة غير موجودة")

    return render(
        request,
        "history/state_detail.html",
        {
            "state": state,
            "era": era,
        }
    )
