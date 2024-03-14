from django.shortcuts import render

pupils_data = {
    1: 'Yusufjon Muhammadov',
    2: 'Nurbek Doniyorov',
    3: 'Boburmirzo Muhammadov',
    4: 'Fazliddin Asomov',
    5: 'Muhammadjon Ibrohimov'
}


def pupils(request):
    return render(request, 'pupils.html', {'pupils_ls': pupils_data})


def pupil1(request):
    return render(request, 'pupil1.html')


def pupil2(request):
    return render(request, 'pupil2.html')


def pupil3(request):
    return render(request, 'pupil3.html')


def pupil4(request):
    return render(request, 'pupil4.html')


def pupil5(request):
    return render(request, 'pupil5.html')
