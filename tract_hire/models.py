from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.location

    def save_location(self):
        self.save()

    def delete_location(self):
        Location.objects.filter().delete()

    @classmethod
    def get_location(cls):
        location_found = cls.objects.all()
        return location_found


class Tractor(models.Model):
    name = models.CharField(max_length=255)
    tractor_image = models.ImageField(upload_to='tractor_pics',blank=True)
    category = models.CharField(max_length=200)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    price_estimate = models.FloatField()
    location_id = models.ForeignKey(Location,blank=True)
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

    @classmethod
    def get_single_tractor(cls, tractor):
        tractor = cls.objects.get(id=tractor)
        return tractor

    @classmethod
    def filter_by_location(cls,location_filter):
        located_tracts = Tractor.objects.filter(location_id__id=location_filter)
        return located_tracts