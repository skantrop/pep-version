from distutils.command.upload import upload
from email.mime import image
from django.db import models
from django.core.validators import FileExtensionValidator



class Company(models.Model):
    slug = models.SlugField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='catgories', blank=True, null=True)
    parent = models.ForeignKey('self', related_name='children', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        if self.parent:
            return f'{self.parent} -> {self.name}'
        return self.name

    @property
    def get_children(self):
        if self.children:
            return self.children.all()
        return False


class Food(models.Model):
    title = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='recipes')
    image = models.ImageField(upload_to='food')
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('detail', kwargs={'pk': self.pk})



