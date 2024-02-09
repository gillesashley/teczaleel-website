from django.urls import path

from .views import HomePageView, BlogPageView, CaseStudyView, ContactPageView, ProductsPageView

app_name = 'pages'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('blog/', BlogPageView.as_view(), name='blog'),
    path('case-study/', CaseStudyView.as_view(), name='case-study'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('products/', ProductsPageView.as_view(), name='products'),
]
