from django.urls import path

from .views import TrackProjectView

urlpatterns = [
    path('track-project/', TrackProjectView.as_view(), name='track-project'),
]
