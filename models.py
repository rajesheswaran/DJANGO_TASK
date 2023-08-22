from django.db import models

class competition(models.Model):
    id=models.PositiveBigIntegerField(primary_key=True)
    name=models.CharField(max_length=255)
    code=models.CharField(max_length=20)
    
    def __str__(self):
        return self.name


