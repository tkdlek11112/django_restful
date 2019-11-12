from django.conf.urls import url, include
from addresses import views
from django.urls import path
from django.contrib import admin


urlpatterns = [
    path('addresses/', views.address_list),
    path('addresses/<int:pk>/', views.address),
    path('login/', views.login),
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]