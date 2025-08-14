from django.db import models

from django.conf import settings


class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField()
    location = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    related_persons = models.CharField(max_length=300, blank=True, verbose_name='关联人（可用逗号分隔）')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['date']