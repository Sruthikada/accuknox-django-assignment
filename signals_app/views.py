from django.http import HttpResponse
from django.db import transaction
from .models import Employee

def create_employee(request):

    try:
        with transaction.atomic():

            Employee.objects.create(name="John")

            raise Exception("Force Rollback")

    except Exception:
        pass

    return HttpResponse("Transaction rolled back")