from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from users.log import Login, Logout, UserToken


schema_view = get_schema_view(
   openapi.Info(
      title="DOCUMENTACION DE API",
      default_version='v0.1',
      description="Documentacion publica API ECOMMERCE",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="matias_remo19@hotmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path(r'swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('logout/', Logout.as_view()),
    path('login/', Login.as_view()),
    path('refresh-token/', UserToken.as_view()),
    path('usuario/', include('users.urls')),
    path('productos/', include('products.routers')),
]
