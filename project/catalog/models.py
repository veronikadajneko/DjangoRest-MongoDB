from djongo import models


class Texts(models.Model):
    _id = models.ObjectIdField()
    textual_paragraph = models.CharField(max_length=9000, blank=False, default='')
    author = models.CharField(max_length=900, blank=False, default='')
    date = models.DateTimeField()
