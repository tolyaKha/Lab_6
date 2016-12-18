from django.shortcuts import render
from users.models import Fight
from django.views.generic import TemplateView


class Fights(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        Fights = Fight.objects.all()
        context = dict(Fights=Fights)
        return context

class HomePageView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context = Fight.objects.all()
        return context
