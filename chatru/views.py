from django.shortcuts import render, redirect, get_object_or_404
from .forms import TranslateForm
from chatru import traductor
from .models import Translation

# Create your views here.


def chatru_form(request):
    if request.method == 'POST':
        form = TranslateForm(request.POST)
        if form.is_valid():
            input = form.cleaned_data.get('texto')
            # form.save()
            # return redirect('translate')
    else:
        form = TranslateForm()

    texto_traducido = traductor.separar_palabras(input)
    chatru = traductor.palabras_en_chatru(texto_traducido)

    args = {'form': form, 'chatru': chatru}
    return render(request, 'chatru/chatru.html', args)






