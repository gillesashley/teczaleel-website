from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class BlogPageView(TemplateView):
    template_name = 'pages/blog.html'


class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'


class CaseStudyView(TemplateView):
    template_name = 'pages/case_study.html'


class ProductsPageView(TemplateView):
    template_name = 'pages/products.html'
