from django.urls import path

from .views import pupils, pupil1, pupil2, pupil3, pupil4, pupil5

urlpatterns = [
    path('', pupils, name='pupils'),
    path('1/', pupil1, name='pupil1'),
    path('2/', pupil2, name='pupil2'),
    path('3/', pupil3, name='pupil3'),
    path('4/', pupil4, name='pupil4'),
    path('5/', pupil5, name='pupil5'),
]