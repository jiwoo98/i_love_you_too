from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def post(request):
    return render(request, 'post.html')

def post_list(request):
    return render(request, 'post_list.html')