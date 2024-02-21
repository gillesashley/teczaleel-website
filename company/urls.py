from django.urls import path

from .views import TrackProjectView, StartProjectView

app_name = 'company'
urlpatterns = [
    path('track-project/', TrackProjectView.as_view(), name='track-project'),
    path('start-project/', StartProjectView.as_view(), name='start-project'),
]
