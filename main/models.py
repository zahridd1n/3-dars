from django.db import models

class Files(models.Model):
    filepath = models.ImageField(upload_to='img/')

    def __str__(self):
        return self.filepath.name

