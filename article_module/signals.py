from django.db.models.signals import post_delete
from .models import Article
import os
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from sorl.thumbnail import delete


@receiver(post_delete, sender=Article)
def delete_product_image_file(sender, instance, **kwargs):
    if instance.image:
        image_path = instance.image.path
        if os.path.isfile(image_path):
            os.remove(image_path)



@receiver(pre_delete, sender=Article)
def delete_image_files(sender, instance, **kwargs):
    # حذف thumbnail از cache
    delete(instance.image)


