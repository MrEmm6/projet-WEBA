from django.conf import settings
from django.db import models
from django.utils import timezone

class Film(models.Model):
    auteur = models.CharField(max_length=50)
    titre = models.CharField(max_length=50)
    avis = models.TextField()
    dateVue = models.DateField(default=timezone.now)

    def get_date_vue(self):
        return self.dateVue.strftime("%d.%m.%Y")

    def __str__(self):
        return self.titre