from django.db import models

from django.db.models.fields import TextField
from django.utils import timezone
import uuid

# Create your models here.
class Companie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=256, verbose_name="Название", blank=False, null=False)
    description = models.TextField(max_length=2048, verbose_name="Описание", blank=True, null=False)
    site = models.CharField(max_length=256, verbose_name="Сайт", blank=True, null=False)
    # TODO LOGO and to serializer
    
    def __str__(self):
        return f"{self.name}: {self.description[0:128]}"


class Vacancy(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=256, verbose_name="Название", blank=False, null=False)
    description = models.TextField(max_length=2048, verbose_name="Описание", blank=True, null=False)
    companie = models.ForeignKey(Companie, on_delete=models.CASCADE, blank=False, null=False)
    wage_from = models.IntegerField(default=None, null=True)
    wage_up_to = models.IntegerField(default=None, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.name}: {self.description[0:128]}"

class Responses(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # TODO User
    vacancy_id = models.ForeignKey(Vacancy, on_delete=models.CASCADE, blank=False, null=False)
