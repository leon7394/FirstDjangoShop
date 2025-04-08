# product_module/signals.py

import os
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Product
from django.conf import settings

@receiver(post_delete, sender=Product)
def delete_product_image_file(sender, instance, **kwargs):
    if instance.image:
        image_path = instance.image.path
        if os.path.isfile(image_path):
            os.remove(image_path)
