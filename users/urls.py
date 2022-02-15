from django.urls import path
from users.views import user_api_view, user_detail_view

urlpatterns = [
    path('usuario/', user_api_view),
    path('usuario/<int:pk>', user_detail_view),
]