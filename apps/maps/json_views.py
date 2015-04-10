from apps.maps import models, serializers
from rest_framework import generics
import django_filters


class IntegerListFilter(django_filters.Filter):
    def filter(self, qs, value):
        if value not in (None, ''):
            integers = [int(v) for v in value.split('.')]
            return qs.filter(**{'{}__{}'.format(self.name, self.lookup_type): integers})
        return qs


class RouteFilter(django_filters.FilterSet):
    """ Filter used for the Route model."""
    id = IntegerListFilter(name='id', lookup_type='in')

    class Meta:
        model = models.Route
        fields = ('id', 'route_num')


class StopFilter(django_filters.FilterSet):
    """ Filter used for the Stop model."""
    id = IntegerListFilter(name='id', lookup_type='in')

    class Meta:
        model = models.Stop
        fields = ('id', 'name')


class R1NStopFilter(django_filters.FilterSet):
    """Filter used for the R 1 N Stops model."""
    id = IntegerListFilter(name='id', lookup_type='in')

    class Meta:
        model = models.R1NStops
        fields = ('id', 'name')


class R1SStopFilter(django_filters.FilterSet):
    """Filter used for the R 1 N Stops model."""
    id = IntegerListFilter(name='id', lookup_type='in')

    class Meta:
        model = models.R1SStops
        fields = ('id', 'name')


class R2StopFilter(django_filters.FilterSet):
    """Filter used for the R 1 N Stops model."""
    id = IntegerListFilter(name='id', lookup_type='in')

    class Meta:
        model = models.R2Stops
        fields = ('id', 'name')


class R3StopFilter(django_filters.FilterSet):
    """Filter used for the R 1 N Stops model."""
    id = IntegerListFilter(name='id', lookup_type='in')

    class Meta:
        model = models.R3Stops
        fields = ('id', 'name')


class R4StopFilter(django_filters.FilterSet):
    """Filter used for the R 1 N Stops model."""
    id = IntegerListFilter(name='id', lookup_type='in')

    class Meta:
        model = models.R4Stops
        fields = ('id', 'name')


class R5AStopFilter(django_filters.FilterSet):
    """Filter used for the R 1 N Stops model."""
    id = IntegerListFilter(name='id', lookup_type='in')

    class Meta:
        model = models.R5AStops
        fields = ('id', 'name')


class R5BStopFilter(django_filters.FilterSet):
    """Filter used for the R 1 N Stops model."""
    id = IntegerListFilter(name='id', lookup_type='in')

    class Meta:
        model = models.R5BStops
        fields = ('id', 'name')


class R6StopFilter(django_filters.FilterSet):
    """Filter used for the R 1 N Stops model."""
    id = IntegerListFilter(name='id', lookup_type='in')

    class Meta:
        model = models.R6Stops
        fields = ('id', 'name')


class RouteCollection(generics.ListAPIView):
    """
    API endpoint that allows transportation routes to be viewed or edited.
    """
    queryset = models.Route.objects.all()
    serializer_class = serializers.RouteSerializer
    filter_class = RouteFilter


class StopCollection(generics.ListAPIView):
    """
    API endpoint that allows transportation stops to be viewed or edited.
    """
    queryset = models.Stop.objects.all()
    serializer_class = serializers.StopSerializer
    filter_class = StopFilter


class R1NStopCollection(generics.ListAPIView):
    """API endpoint that allows R 1 N stops to be viewed"""
    queryset = models.R1NStops.objects.all()
    serializer_class = serializers.R1NStops
    filter_class = R1NStopFilter


class R1SStopCollection(generics.ListAPIView):
    """API endpoint that allows R 1 N stops to be viewed"""
    queryset = models.R1SStops.objects.all()
    serializer_class = serializers.R1SStops
    filter_class = R1SStopFilter


class R2StopCollection(generics.ListAPIView):
    """API endpoint that allows R 1 N stops to be viewed"""
    queryset = models.R2Stops.objects.all()
    serializer_class = serializers.R2Stops
    filter_class = R2StopFilter


class R3StopCollection(generics.ListAPIView):
    """API endpoint that allows R 1 N stops to be viewed"""
    queryset = models.R3Stops.objects.all()
    serializer_class = serializers.R3Stops
    filter_class = R3StopFilter


class R4StopCollection(generics.ListAPIView):
    """API endpoint that allows R 1 N stops to be viewed"""
    queryset = models.R4Stops.objects.all()
    serializer_class = serializers.R4Stops
    filter_class = R4StopFilter


class R5AStopCollection(generics.ListAPIView):
    """API endpoint that allows R 1 N stops to be viewed"""
    queryset = models.R5AStops.objects.all()
    serializer_class = serializers.R5AStops
    filter_class = R5AStopFilter


class R5BStopCollection(generics.ListAPIView):
    """API endpoint that allows R 1 N stops to be viewed"""
    queryset = models.R5BStops.objects.all()
    serializer_class = serializers.R5BStops
    filter_class = R5BStopFilter


class R6StopCollection(generics.ListAPIView):
    """API endpoint that allows R 1 N stops to be viewed"""
    queryset = models.R6Stops.objects.all()
    serializer_class = serializers.R6Stops
    filter_class = R6StopFilter