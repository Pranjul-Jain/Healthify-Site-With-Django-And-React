from django.db import models

# Create your models here.


class healthtips(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    tips = models.CharField(max_length=50, null=False)
    tip_description = models.TextField()
