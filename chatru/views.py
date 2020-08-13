from django.shortcuts import render, redirect
from .models import Traduccion
from django.views.generic import CreateView
# Create your views here.


class ChatruView(CreateView):
    model = Traduccion
    template_name = 'chatru/chatru.html'
    fields = ['texto']
