from django.urls import path
from . import views
urlpatterns = [
    path('api/currencies/all_statistics', views.MyAPIView.as_view()),
    path('api/docs/redoc', views.serve_doc),
    path('api/docs/swagger', views.serve_swagger),
]