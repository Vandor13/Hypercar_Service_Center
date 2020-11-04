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


class ProcessingView(View):
    def get(self, request, *args, **kwargs):
        queue_manager = QueueManagerFactory.get_queue_manager()
        no_oil, no_tire, no_diagnostic = queue_manager.get_queue_lengths()
        context = {
            "no_oil": no_oil,
            "no_tire": no_tire,
            "no_diagnostic": no_diagnostic
        }
        return render(request, "processing.html", context=context)

    def post(self, request, *args, **kwargs):
        queue_manager = QueueManagerFactory.get_queue_manager()
        queue_manager.process_next_request()
        no_oil, no_tire, no_diagnostic = queue_manager.get_queue_lengths()
        context = {
            "no_oil": no_oil,
            "no_tire": no_tire,
            "no_diagnostic": no_diagnostic
        }
        return render(request, "processing.html", context=context)


class NextView(View):
    def get(self, request, *args, **kwargs):
        queue_manager = QueueManagerFactory.get_queue_manager()
        next_number = queue_manager.get_next_number()
        if next_number:
            context = {
                "next_number": next_number
            }
        else:
            context = {}
        return render(request, "next.html", context=context)


class ResetView(View):
    def get(self, request, *args, **kwargs):
        Ticket.objects.all().delete()
        return render(request, "reset.html")
