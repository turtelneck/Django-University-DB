from django.db import models

# creates a class that can be used to create objects
class djangoClasses(models.Model):
    title = models.CharField(max_length=60)
    courseNumber = models.CharField(max_length=4, default="", blank=True, null=False)
    instructor = models.CharField(max_length=60, default="", blank=True)
    duration = models.DecimalField(default=0.0, max_digits=10000, decimal_places=1)

    objects = models.Manager()

    # ensures the admin console will show the object's title
    def __str__(self):
        return self.title
