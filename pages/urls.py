from django.urls import path

from .views import HomePageView, BlogPageView, WorksPageView, ContactPageView

app_name = 'pages'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('blog/', BlogPageView.as_view(), name='blog'),
    path('works/', WorksPageView.as_view(), name='works'),
    path('contact/', ContactPageView.as_view(), name='contact'),
]
