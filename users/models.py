from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=265, blank=False, null=False)
    last_name = models.CharField(max_length=265, blank=False, null=False)
    email = models.CharField(max_length=265, blank=False, null=False)
    age = models.IntegerField(blank=True, null=False)

    def __str__(self):
        """Sensible string representation of a user"""
        return "{0} {1} | {2}".format(self.first_name, self.last_name,self.email)