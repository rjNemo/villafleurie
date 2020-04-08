from django.views.generic.base import TemplateView


class Legal(TemplateView):
    template_name = 'rental/legal.html'


class About(TemplateView):
    template_name = 'rental/about.html'


class Partners(TemplateView):
    template_name = 'rental/partners.html'


class Services(TemplateView):
    template_name = 'rental/service.html'
