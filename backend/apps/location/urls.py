from django.urls import path

from apps.location.apis.views import LocationListAPIView, LocationDetailView, LocationCreateAPIView, LocationRetrieveAPIView, LocationUpdateAPIView, LocationDeleteAPIView


urlpatterns = [
    path("list/", LocationListAPIView.as_view()),
    path("detail/<int:pk>/", LocationDetailView.as_view()),
    path("retrieve/<int:pk>/", LocationRetrieveAPIView.as_view()),
    path("create/", LocationCreateAPIView.as_view()),
    path("update/<int:pk>/", LocationUpdateAPIView.as_view()),
    path("delete/<int:pk>/", LocationDeleteAPIView.as_view()),
]
