from django.core.management.base import BaseCommand
from dreamhome.models import Lease, Client, Propertyforrent
from django.utils import timezone
from django.core.mail import send_mail
from django.db.models import Q
from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler


def send_email():
    active_leases = Lease.objects.filter(rent_finish__gt=timezone.now().date())
    clients = Client.objects.all()
    for client in clients:
        matched_properties = []
        properties = Propertyforrent.objects.filter(
            regbranch=client.regbranch,
            rent__lte=client.maxrent,
            proptype=client.preftype
        ).exclude(
            Q(leaseno__in=active_leases.values("leaseno")) &
            Q(leaseno__isnull=False)
        )
        for property in properties:
            matched_properties.append(property)
        if matched_properties:
            email = "{}@example.com".format(client.clientno)
            subject = "Matched Properties for {}".format(client.fname)
            message = "Dear {},\n\nHere are the properties that match your criteria:\n\n{}".format(
                client.fname,
                "\n".join([str(property) for property in matched_properties])
            )
            print("[{}] Email sent to {}.\nSubject: {}\nMessage: {}".format(
                datetime.now(), email, subject, message
            ))
        print('-------------------------------------------')


class Command(BaseCommand):
    help = 'Sends email to clients with matched properties every 1 minute.'

    def handle(self, *args, **options):
        scheduler = BackgroundScheduler()
        scheduler.add_job(send_email, 'interval', minutes=0.5)
        scheduler.start()
        print('Scheduler started. Press Ctrl+C to exit.')
        try:
            # This is to prevent the main thread from exiting.
            while True:
                pass
        except KeyboardInterrupt:
            print('Scheduler stopped.')
            scheduler.shutdown()
