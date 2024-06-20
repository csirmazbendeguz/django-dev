from django.db import models


class Tenant(models.Model):
    pass


class Comment(models.Model):
    id = models.IntegerField(primary_key=True)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
