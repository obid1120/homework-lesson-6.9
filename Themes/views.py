from django.shortcuts import render

with open('static/lessons.txt', 'r') as file:
    themes_list = file.readlines()


def themes(request):
    return render(request, 'themes.html', {'themes': themes_list})
