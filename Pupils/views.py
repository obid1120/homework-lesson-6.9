from django.shortcuts import render

pupils_data = {
    1: ['Yusufjon Muhammadov', ]
}


def pupils(request):
    return render(request, 'pupils.html', {'hello': []})


def pupil1(request):
    return render(request, 'pupil1.html', {'hello': []})


def pupil2(request):
    return render(request, 'pupil2.html', {'hello': []})


def pupil3(request):
    return render(request, 'pupil3.html', {'hello': []})


def pupil4(request):
    return render(request, 'pupil4.html', {'hello': []})


def pupil5(request):
    return render(request, 'pupil5.html', {'hello': []})
