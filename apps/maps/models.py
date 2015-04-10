from django.contrib.gis.db import models
from django.core.files.storage import FileSystemStorage

# Create your models here.

fs = FileSystemStorage(location='/media/photos')


class Stop(models.Model):
    """This model will hold public transit bus stop information"""
    geom = models.PointField(srid=4326)
    name = models.CharField(max_length=40)
    amenities = models.CharField(max_length=40)

    def __str__(self):
        return "{}".format(self.name)


class Route(models.Model):
    """This model will hold public transit bus routes information"""
    geom = models.MultiLineStringField(srid=4326)
    route_num = models.CharField(max_length=40)

    def __str__(self):
        return "{}".format(self.route_num)


class R1NStops(models.Model):
    """This model will hold stops associated with route 1 N"""
    geom = models.PointField(srid=4326)
    name = models.CharField(max_length=42)
    amenities = models.CharField(max_length=40)

    def __str__(self):
        return "{}".format(self.name)


class R1SStops(models.Model):
    """This model will hold stops associated with route 1 S"""
    geom = models.PointField(srid=4326)
    name = models.CharField(max_length=42)
    amenities = models.CharField(max_length=40)

    def __str__(self):
        return "{}".format(self.name)


class R2Stops(models.Model):
    """This model will hold stops associated with route 2"""
    geom = models.PointField(srid=4326)
    name = models.CharField(max_length=42)
    amenities = models.CharField(max_length=40)

    def __str__(self):
        return "{}".format(self.name)


class R3Stops(models.Model):
    """This model will hold stops associated with route 3"""
    geom = models.PointField(srid=4326)
    name = models.CharField(max_length=42)
    amenities = models.CharField(max_length=40)

    def __str__(self):
        return "{}".format(self.name)


class R4Stops(models.Model):
    """This model will hold stops associated with route 4"""
    geom = models.PointField(srid=4326)
    name = models.CharField(max_length=42)
    amenities = models.CharField(max_length=40)

    def __str__(self):
        return "{}".format(self.name)


class R5AStops(models.Model):
    """This model will hold stops associated with route 5 A"""
    geom = models.PointField(srid=4326)
    name = models.CharField(max_length=42)
    amenities = models.CharField(max_length=40)

    def __str__(self):
        return "{}".format(self.name)


class R5BStops(models.Model):
    """This model will hold stops associated with route 5 B"""
    geom = models.PointField(srid=4326)
    name = models.CharField(max_length=42)
    amenities = models.CharField(max_length=40)

    def __str__(self):
        return "{}".format(self.name)


class R6Stops(models.Model):
    """This model will hold stops associated with route 6"""
    geom = models.PointField(srid=4326)
    name = models.CharField(max_length=42)
    amenities = models.CharField(max_length=40)

    def __str__(self):
        return "{}".format(self.name)


# class Images(models.Model):
#     """This model will hold image files of Stops."""
#     name = models.CharField(max_length=100)
#     place = models.ForeignKey(Stop)
#     photo = models.ImageField(storage=fs)
#
#     def __str__(self):
#         return self.name