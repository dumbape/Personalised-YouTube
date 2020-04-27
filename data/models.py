from django.db import models
from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import SearchVectorField
from django.db.models.signals import post_save

# table scema for storing data
class Video(models.Model):
    videoId = models.SlugField(max_length = 50, null = False, primary_key = True)
    title = models.CharField(max_length = 200, null = False)
    description = models.CharField(max_length = 2000, null = False)
    publishedAt = models.DateTimeField(null = False)
    thumbnailURL = models.URLField(max_length = 200, null = False)

    # New field to index on
    searchvector = SearchVectorField(null = True, blank = True)

    def __str__(self):
        return self.title

    class Meta:
        indexes = [GinIndex(fields=["searchvector"])]

class APIFetch(models.Model):
    fetchAPI = models.BooleanField(default = False)

    def __str__(self):
        return str(self.fetchAPI)

    @staticmethod
    def post_save(sender, **kwargs):
        instance = kwargs.get('instance')
        if instance and instance.fetchAPI == True:
            from data.fetchData import startFetchingData
            startFetchingData()

# register signal
post_save.connect(APIFetch.post_save, sender=APIFetch)

