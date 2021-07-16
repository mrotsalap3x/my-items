from django.db import models


class Entity(models.Model):
    needs_update = models.BooleanField(default=False)
    has_subs = models.BooleanField(default=False)
    created_at = models.DateTimeField('Date created', auto_now_add=True)
    updated_at = models.DateTimeField('Last updated', auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return '{} [{}]'.format(self.title, self.id)


class Location(Entity):
    contained_in = models.ManyToManyField('self', blank=True)
    title = models.CharField(max_length=200)
    order_no = models.SmallIntegerField(default=0)


class Item(Entity):
    title = models.CharField(max_length=200)
    description = models.TextField()
    outter_view = None
    inner_view = None
    stored_in = models.ManyToManyField(Location, blank=True)
    contained_in = models.ManyToManyField('self', blank=True)
