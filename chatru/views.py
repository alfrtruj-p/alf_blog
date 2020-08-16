from django.shortcuts import render
from .forms import TranslateForm
from chatru import traductor

# Create your views here.


def chatru_form(request):
    input = ''
    if request.method == 'POST':
        form = TranslateForm(request.POST)
        if form.is_valid():
            input = form.cleaned_data.get('texto')
    else:
        form = TranslateForm()
    texto_traducido = traductor.separar_palabras(input)
    texto_chatru = traductor.palabras_en_chatru(texto_traducido)
    chatru = ' '.join(texto_chatru)
    args = {'form': form, 'chatru': chatru}
    return render(request, 'chatru/chatru.html', args)

def about_chatru(request):
    return render(request, 'chatru/about.html', {'title': 'About'})


def about_esp(request):
    return render(request, 'chatru/about_esp.html', {'title': 'About'})






