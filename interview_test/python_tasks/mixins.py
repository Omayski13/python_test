from django.db import models

class ModifiedDataMixin(models.Model):
    ModifiedDate = models.DateTimeField(auto_now=True, )

    class Meta:
        abstract = True