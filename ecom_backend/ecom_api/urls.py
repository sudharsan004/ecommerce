from django.urls import path, include
from rest_framework.authtoken import views
from .views import home

urlpatterns = [
    path('', home, name="api.home"),
    path('category/', include('ecom_api.category.urls')),
    path('product/', include('ecom_api.product.urls'))
]
