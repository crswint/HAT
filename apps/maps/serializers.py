from apps.maps import models
from rest_framework_gis import serializers as geoserializers


class RouteSerializer(geoserializers.GeoFeatureModelSerializer):
    """ Serializer used in API set up off the Route model."""
    class Meta:
        model = models.Route
        geo_field = 'geom'
        fields = ('id', 'route_num')


class StopSerializer(geoserializers.GeoFeatureModelSerializer):
    """ Serializer used in API set up off the Stop model."""
    class Meta:
        model = models.Stop
        geo_field = 'geom'
        fields = ('id', 'name', 'amenities')


class R1NStops(geoserializers.GeoFeatureModelSerializer):
    """Serializer used in API set up of the Route 1 N Stops."""
    class Meta:
        model = models.R1NStops
        geo_field = 'geom'
        field = ('id', 'name', 'amenities')


class R1SStops(geoserializers.GeoFeatureModelSerializer):
    """Serializer used in API set up of the Route 1 S Stops."""
    class Meta:
        model = models.R1SStops
        geo_field = 'geom'
        field = ('id', 'name', 'amenities')


class R2Stops(geoserializers.GeoFeatureModelSerializer):
    """Serializer used in API set up of the Route 1 S Stops."""
    class Meta:
        model = models.R2Stops
        geo_field = 'geom'
        field = ('id', 'name', 'amenities')


class R3Stops(geoserializers.GeoFeatureModelSerializer):
    """Serializer used in API set up of the Route 1 S Stops."""
    class Meta:
        model = models.R3Stops
        geo_field = 'geom'
        field = ('id', 'name', 'amenities')


class R4Stops(geoserializers.GeoFeatureModelSerializer):
    """Serializer used in API set up of the Route 1 S Stops."""
    class Meta:
        model = models.R4Stops
        geo_field = 'geom'
        field = ('id', 'name', 'amenities')


class R5AStops(geoserializers.GeoFeatureModelSerializer):
    """Serializer used in API set up of the Route 1 S Stops."""
    class Meta:
        model = models.R5AStops
        geo_field = 'geom'
        field = ('id', 'name', 'amenities')


class R5BStops(geoserializers.GeoFeatureModelSerializer):
    """Serializer used in API set up of the Route 1 S Stops."""
    class Meta:
        model = models.R5BStops
        geo_field = 'geom'
        field = ('id', 'name', 'amenities')


class R6Stops(geoserializers.GeoFeatureModelSerializer):
    """Serializer used in API set up of the Route 1 S Stops."""
    class Meta:
        model = models.R6Stops
        geo_field = 'geom'
        field = ('id', 'name', 'amenities')