from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class BlogPageView(TemplateView):
    template_name = 'pages/blog.html'


class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'


class WorksPageView(TemplateView):
    template_name = 'pages/works.html'
