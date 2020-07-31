from django.shortcuts import render

posts = [
    {
        'author': 'Alfredo',
        'title': 'First post',
        'content': 'First post content',
        'date_posted': '27 august 2020'
    },
    {
        'author': 'Maria',
        'title': 'Second post',
        'content': 'Second post content',
        'date_posted': '28 august 2020'
    }
]
def home(request):
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

