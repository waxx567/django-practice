from django.db import models

# Create your models here.

class Room(models.Model):
    # host = models.ForeignKey(User, on_delete=models.CASCADE)
    # topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # participants = models.ManyToManyField(User, related_name='rooms')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name