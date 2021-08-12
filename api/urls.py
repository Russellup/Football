from django.urls import include, path
from . import views

urlpatterns = [
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
]