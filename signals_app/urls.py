from django.urls import path
from .views import (
    test_sync,
    test_thread,
    test_transaction
)

urlpatterns = [
    path('q1/', test_sync),
    path('q2/', test_thread),
    path('q3/', test_transaction),
]