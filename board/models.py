from django.db import models


class TaskType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Task Types"
        ordering = ("name",)

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name
