from django.db import models

# Create your models here.


class Task(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.TextField(blank=True, null=False, default="")
    description = models.TextField(blank=True, null=False, default="")
    is_done = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
