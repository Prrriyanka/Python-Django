from django.contrib import admin
from django.urls import include, path

admin.site.site_header = "Garry IceCream Portal"
admin.site.site_title = "Garry Icecream Portal"
admin.site.index_title = "Welcome to Garry IceCreams"


urlpatterns = [
    path("", include('polls.urls')),
#    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
