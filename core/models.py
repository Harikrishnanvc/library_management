from django.db import models


class MasterModel(models.Model):
    created_at = models.DateField(verbose_name="created time", auto_now_add=True)
    updated_at = models.DateField(verbose_name="updated time", auto_now=True)

    def __str__(self):
        return str(self.created_at)
