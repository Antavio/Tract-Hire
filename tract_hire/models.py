from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tractor(models.Model):
    name = models.CharField(max_length=255)
    tractor_image = models.ImageField(upload_to='tractor_pics',blank=True)
    category = models.CharField(max_length=200)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    price_estimate = models.FloatField()
    location = models.CharField(max_length=255)
    contact = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']

    def save_tractor(self):
        self.save()

    def delete_tractor(self):
        self.delete()

    @classmethod
    def fetch_all_tractors(cls):
        all_tractors = Tractor.objects.all()
        return all_tractors

    @classmethod
    def search_tractor(cls,search_term):
        tractor = cls.objects.filter(category__icontains=search_term)
        return tractor   
