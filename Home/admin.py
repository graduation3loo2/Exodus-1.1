from django.contrib import admin
from .models import TripPhotos, Response, Agencies, Activity, Follows, Phones, Trips, Users, Vote

admin.site.register(TripPhotos)
admin.site.register(Response)
admin.site.register(Agencies)
admin.site.register(Activity)
admin.site.register(Follows)
admin.site.register(Phones)
admin.site.register(Trips)
admin.site.register(Users)
admin.site.register(Vote)
