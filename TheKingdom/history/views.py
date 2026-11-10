from django.shortcuts import render
from django.http import Http404


STATES = {
    'first': {
        'title': 'الدولة السعودية الأولى',
        'period': '1727 — 1818م',
        'image': 'history/images/eras/first-banner.jpg',
        'description': 'من الدرعية انطلقت مسيرة تأسيس الدولة السعودية في عهد الإمام محمد بن سعود.',
    },
    'second': {
        'title': 'الدولة السعودية الثانية',
        'period': '1824 — 1891م',
        'image': 'history/images/eras/second-banner.jpg',
        'description': 'أعاد الإمام تركي بن عبدالله تأسيس الدولة السعودية، وأصبحت الرياض عاصمتها.',
    },
    'third': {
        'title': 'الدولة السعودية الثالثة',
        'period': '1902م — اليوم',
        'image': 'history/images/eras/third-banner.jpg',
        'description': 'من استرداد الرياض على يد الملك عبدالعزيز إلى توحيد المملكة ونهضتها الحديثة.',
    },
}


def home(request):
    return render(request, 'history/home.html')


def state_detail(request, era):
    state = STATES.get(era)

    if state is None:
        raise Http404('الدولة المطلوبة غير موجودة')

    return render(request, 'history/state_detail.html', {
        'state': state,
    })