from djongo import models


class QuickStar(models.Model):
    _id = models.ObjectIdField()
    Textual_paragraph = models.CharField(max_length=9000, blank=False, default='')
    author = models.CharField(max_length=900, blank=False, default='')
    date = models.DateField(default='2021/01/01')



