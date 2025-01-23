from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'accessories', views.AccessoryViewSet)
router.register(r'bars', views.BarViewSet)
router.register(r'redeau-accessories', views.RedeauAccessoryViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('tables/', views.tables, name='tables'),
    path('save-prices/', views.save_prices, name='save-prices'),
    path('api/', include(router.urls)),
]
