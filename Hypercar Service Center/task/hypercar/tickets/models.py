from django.db import models
from collections import deque


# Create your models here.
# class CurrentTicketNumber(models.Model):
#     ticket_number = models.IntegerField()
#
#     def __init__(self):
#         super().__init__()
#         self.ticket_number = 1

    # def save(self, *args, **kwargs):
    #     super(CurrentTicketNumber, self).save(*args, **kwargs)
    #
    # def delete(self, *args, **kwargs):
    #     pass

    # def get_ticket_number(self):
    #     return self.ticket_number
    #
    # @classmethod
    # def load(cls):
    #     try:
    #         current_ticket_number = CurrentTicketNumber.objects.get(pk=1)
    #     except CurrentTicketNumber.DoesNotExist:
    #         current_ticket_number = CurrentTicketNumber()
    #         current_ticket_number.save()
    #     return current_ticket_number


class Ticket(models.Model):
    service_type = models.CharField(max_length=32)
    ticket_number = models.IntegerField()


class QueueManagerFactory:
    queueManager = None

    @staticmethod
    def get_queue_manager():
        if not QueueManagerFactory.queueManager:
            print("Creating new QueueManager")
            QueueManagerFactory.queueManager = QueueManager()
        return QueueManagerFactory.queueManager


class QueueManager:

    def __init__(self):
        # oil_tickets = list(Ticket.objects.filter(service_type="oil"))
        # current_ticket_number = CurrentTicketNumber.load()
        print("Queuemanager init")
        self.oil_queue = deque()
        self.tires_queue = deque()
        self.diagnostic_queue = deque()
        self.current_ticket_number = 1
        for ticket in Ticket.objects.filter(service_type="oil"):
            self.oil_queue.appendleft(ticket)
        for ticket in Ticket.objects.filter(service_type="tire"):
            self.tires_queue.appendleft(ticket)
        for ticket in Ticket.objects.filter(service_type="diagnostic"):
            self.diagnostic_queue.appendleft(ticket)

    # @classmethod
    # def load(cls):
    #     obj, created = cls.objects.get_or_create()
    #     return obj

    def calculate_wait_time(self, service_type):
        if service_type == "oil":
            print("Number of Oil Changes in Queue:", str(len(self.oil_queue)))
            return len(self.oil_queue) * 2
        elif service_type == "tire":
            print("Number of Oil Changes in Queue:", str(len(self.oil_queue)))
            print("Number of Tire Inflations in Queue:", str(len(self.tires_queue)))
            return len(self.oil_queue) * 2 + len(self.tires_queue) * 5
        else:
            return len(self.oil_queue) * 2 + len(self.tires_queue) * 5 + len(self.diagnostic_queue) * 30

    def add_item_to_queue(self, service_type, ticket_number):
        if service_type == "oil":
            self.oil_queue.appendleft(ticket_number)
        elif service_type == "tire":
            self.tires_queue.appendleft(ticket_number)
        else:
            self.diagnostic_queue.appendleft(ticket_number)

    def get_ticket(self, service_type):
        wait_time = self.calculate_wait_time(service_type)
        ticket_number = self.current_ticket_number
        self.current_ticket_number += 1
        # CurrentTicketNumber.objects.all().update(ticket_number=self.current_ticket_number)
        new_ticket = Ticket(ticket_number=self.current_ticket_number, service_type=service_type)
        new_ticket.save()
        self.add_item_to_queue(service_type, ticket_number)
        return ticket_number, wait_time
