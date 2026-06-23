import time
from django.http import JsonResponse
from .models import TestModel
import threading
from django.db import transaction

def test_sync(request):

    start = time.time()

    TestModel.objects.create(name="Pavan")

    end = time.time()

    return JsonResponse({
        "execution_time": end - start
    })

def test_thread(request):

    caller_thread = threading.get_ident()

    TestModel.objects.create(name="Pavan")

    return JsonResponse({
        "caller_thread": caller_thread
    })

def test_transaction(request):

    try:

        with transaction.atomic():

            TestModel.objects.create(
                name="Pavan"
            )

            raise Exception(
                "Rollback Transaction"
            )

    except Exception:
        pass

    return JsonResponse({
        "message": "Done"
    })