from django.db import models


class Place(models.Model):
    id = models.IntegerField(null=False, default=None, primary_key=True)
    name = models.CharField(null=False, default=None, max_length=50)

    def __str__(self):
        return '%s %s' % (self.value, self.unit)
