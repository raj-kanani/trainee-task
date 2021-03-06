from django.conf import settings
from django.db import models
from django.utils.translation import gettext

STATUS = (('active', 'active'),
          ('inactive', 'inactive'))


class Sprint(models.Model):
    number = models.CharField(max_length=150, blank=True, null=True, default=0)
    status = models.CharField(choices=STATUS, max_length=120)
    start_date = models.DateField()
    end_date = models.DateField()

    # def __str__(self):
    #     return self.number

    def __str__(self):
        return self.number or gettext('Sprint ending %s') % self.end_date


class Task(models.Model):
    STATUS_TODO = 'STATUS_TODO'
    STATUS_IN_PROGRESS = 'STATUS_IN_PROGRESS'
    STATUS_COMPLETED = 'STATUS_COMPLETED'
    STATUS_DONE = 'STATUS_DONE'

    STATUS_CHOICES = (
        (STATUS_TODO, gettext('Not Started')),
        (STATUS_IN_PROGRESS, gettext('In Progress')),
        (STATUS_COMPLETED, gettext('Completed')),
        (STATUS_DONE, gettext('Done')),
    )

    def nameFile(instance, filename):
        return '/'.join(['images', str(instance.user), filename])

    task_number = models.IntegerField()
    description = models.CharField(max_length=150, null=True, blank=True)
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=120, choices=STATUS_CHOICES, default=STATUS_TODO)
    start_date = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to=nameFile, blank=True, null=True)
    backlog = models.BooleanField()

    def __int__(self):
        return self.task_number


