import shapefile
from apps.maps.models import Route
import django
django.setup()

#Custom load file created to load Center model into database
route_path = 'C:/Users/crswin5726/PycharmProjects/HAT/apps/maps/data/routes.shp'

sf = shapefile.Reader(route_path)
sr = sf.shapeRecords()
record = {-1: True, 0: False}

for r in sr:
    stop_list = []
    stops = r.record[14].split(',')
    for stop in stops:
        s = models.Stops.objects.filter(stop_no=stop)
        stop_list.append(s)


    # LOOP OVER stop_list, ADD EACH STOP TO ROUTE MANY TO MANY

        s.save()
