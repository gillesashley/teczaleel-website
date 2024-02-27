from django.urls import path

from .views import TrackProjectView

app_name = 'company'
urlpatterns = [
    path('track-project/', TrackProjectView.as_view(), name='track-project'),
]
