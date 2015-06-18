from django.db import models

# Create your models here.
class Expression(models.Model):
    expression = models.CharField(max_length=150)
    number = models.IntegerField(unique=True)
    
    def __unicode__(self):
        return unicode(self.expression)