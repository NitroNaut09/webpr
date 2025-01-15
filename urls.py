from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Core app handles the homepage
    path('physics/', include('physics.urls')),  # Physics app handles the graph page
]