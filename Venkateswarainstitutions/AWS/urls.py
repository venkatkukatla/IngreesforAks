from django.urls import path
from AWS.views import aws
from AWS.views import jen


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('cloud2/', aws),
    path('jen/', jen),
]