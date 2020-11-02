from django.views import View
from django.http.response import HttpResponse
from django.shortcuts import render


class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "welcome_page.html")


class MenuView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "menu.html")
