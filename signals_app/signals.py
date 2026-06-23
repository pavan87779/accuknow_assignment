import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import TestModel, SignalLog
import threading
@receiver(post_save, sender=TestModel)
def slow_signal(sender, instance, **kwargs):
    print("Signal Started")
    time.sleep(5)
    print("Signal Finished")

@receiver(post_save, sender=TestModel)
def check_signal_thread(sender, instance, **kwargs):

    print(
        "Signal Thread ID:",
        threading.get_ident()
    )

@receiver(post_save, sender=TestModel)
def create_log(sender, instance, **kwargs):

    SignalLog.objects.create(
        message="Signal Executed"
    )