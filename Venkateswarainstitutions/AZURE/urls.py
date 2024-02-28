from django.urls import path
from AZURE.views import azure
from AZURE.views import ado


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('cloud1/', azure),
    path('ado/', ado),
]