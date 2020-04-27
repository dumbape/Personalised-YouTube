from django.db import models
from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import SearchVectorField
from django.db.models.signals import post_save
from django.contrib.postgres.fields import ArrayField

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

    def getDefaultAPIKeys():
        return []

    fetchAPI = models.BooleanField(default = False)
    searchQuery = models.CharField(default = "", null = False, max_length = 50)
    apiKey = ArrayField(models.CharField(default = "", null = False, max_length = 100), default = getDefaultAPIKeys)
    fetchInterval = models.IntegerField(default = 60)

    def __str__(self):
        return str(self.fetchAPI)

    @staticmethod
    def post_save(sender, **kwargs):
        instance = kwargs.get('instance')
        if instance and instance.fetchAPI == True:
            from data.fetchData import startFetchingData
            fetchInterval = int(instance.fetchInterval)
            # currently fetching from first API only
            apiKey = instance.apiKey[0]
            searchQuery = instance.searchQuery
            startFetchingData(fetchInterval, apiKey, searchQuery)

# register signal
post_save.connect(APIFetch.post_save, sender=APIFetch)

