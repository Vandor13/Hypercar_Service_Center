from django.views import View
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Ticket, QueueManager, QueueManagerFactory


class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "welcome_page.html")


class MenuView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "menu.html")


class OilView(View):
    def get(self, request, *args, **kwargs):
        queue_manager = QueueManagerFactory.get_queue_manager()
        ticket_number, wait_time = queue_manager.get_ticket("oil")
        context = {
            "ticket_number": ticket_number,
            "wait_time": wait_time
        }
        return render(request, "ticket.html", context=context)


class TireView(View):
    def get(self, request, *args, **kwargs):
        queue_manager = QueueManagerFactory.get_queue_manager()
        ticket_number, wait_time = queue_manager.get_ticket("tire")
        context = {
            "ticket_number": ticket_number,
            "wait_time": wait_time
        }
        return render(request, "ticket.html", context=context)


class DiagnosticView(View):
    def get(self, request, *args, **kwargs):
        queue_manager = QueueManagerFactory.get_queue_manager()
        ticket_number, wait_time = queue_manager.get_ticket("diagnostic")
        context = {
            "ticket_number": ticket_number,
            "wait_time": wait_time
        }
        return render(request, "ticket.html", context=context)


class ResetView(View):
    def get(self, request, *args, **kwargs):
        Ticket.objects.all().delete()
        return render(request, "reset.html")
