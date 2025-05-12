import os
from django.db.models.signals import post_delete
from django.dispatch import receiver
from site_module.models import Slider

@receiver(post_delete, sender=Slider)
def delete_slider_image(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)