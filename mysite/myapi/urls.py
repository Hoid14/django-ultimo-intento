from django.urls import include, path
from rest_framework import routers
from . import views
from .views import finanzas_list

router = routers.DefaultRouter()
router.register(r'heroes', views.HeroViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('finanzas/', finanzas_list, name='finanzas_list'),
]