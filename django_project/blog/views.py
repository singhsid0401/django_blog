from django.shortcuts import render
#from django.http import HttpResponse

posts = [
    {
        'author': 'Sid',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': '27/07/2018'
    },
    {
        'author': 'Mug',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': '28/07/2018'
    }
]

def home(request):
    #return HttpResponse('<h1>Blog Home</h1>')
    context={
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    #return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'blog/about.html', {'title': 'About'})
