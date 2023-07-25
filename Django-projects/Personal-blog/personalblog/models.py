from django.db import models
import uuid

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)

    def __str__(self):
        return self.title