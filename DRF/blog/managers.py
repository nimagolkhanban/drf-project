from django.db import models


class PublishedQuerySet(models.QuerySet):
    def published(self):
        return self.filter(status='published')

class PostManager(models.Manager):
    def get_queryset(self):
        return PublishedQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()