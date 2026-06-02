from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Employee, Audit

@receiver(post_save, sender=Employee)
def create_audit(sender, instance, **kwargs):
    Audit.objects.create(
        message=f"Employee {instance.name} created"
    )
    print("Audit record created")