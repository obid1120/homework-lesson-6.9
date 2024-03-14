from django.urls import path

from .views import pupils, pupil1, pupil2, pupil3, pupil4, pupil5

urlpatterns = [
    path('', pupils, name='pupils'),
    path('1/', pupil1, name='1'),
    path('2/', pupil2, name='2'),
    path('3/', pupil3, name='3'),
    path('4/', pupil4, name='4'),
    path('5/', pupil5, name='5'),
]