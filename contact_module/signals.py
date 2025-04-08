

import os
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import UserProfile
from django.conf import settings

@receiver(post_delete, sender=UserProfile)
def delete_profile_image_file(sender, instance, **kwargs):
    if instance.image:
        image_path = instance.image.path
        if os.path.isfile(image_path):
            os.remove(image_path)
