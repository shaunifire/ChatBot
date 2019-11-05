from django.shortcuts import render
from .models import Odpowiedz
def odpowiedz_bota(request):
    return render (request, 'C:/Users/Asusik/Desktop/ChatBot/ChatBotApp/templates/odpowiedz.html', {})
def test (request):
    return odpowiedz_bota(request)

# Create your views here.
