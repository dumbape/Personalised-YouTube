from django.db import models
from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import SearchVectorField

# table scema for storing data
class Video(models.Model):
    id = models.SlugField(max_length = 50, null = False, primary_key = True)
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

