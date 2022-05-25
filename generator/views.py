from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def about(request):
   return render(request, "generator/about.html")


def home(request):
    return render(request,"generator/home.html")

def password(request):

   characters = list("abcdefghijklmnopqrstuvwxyz")
   generator_password = ""

   tamaño_contraseña = int(request.GET.get("length"))

   if request.GET.get("uppercase"):
      characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
   if request.GET.get("special"):
      characters.extend(list("@!$%&()=#!"))
   if request.GET.get("numbers"):
      characters.extend(list("123456789"))

   
   for x in range(tamaño_contraseña):
      generator_password += random.choice(characters)


   return render(request, "generator/password.html", {"contraseña_creada": generator_password})