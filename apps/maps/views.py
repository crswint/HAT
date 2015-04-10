from django.shortcuts import render
from django.views import generic

# Create your views here.


class MainView(generic.TemplateView):
    """Loads the main page."""
    template_name = 'maps/main.html'


class OneNorth(generic.TemplateView):
    """Loads the Route 1 North Page"""
    template_name = 'maps/onenorth.html'


class OneSouth(generic.TemplateView):
    """Loads the Route 1 South Page"""
    template_name = 'maps/onesouth.html'


class Two(generic.TemplateView):
    """Loads the Route 2 Page"""
    template_name = 'maps/two.html'


class Three(generic.TemplateView):
    """Loads the Route 3 Page"""
    template_name = 'maps/three.html'


class Four(generic.TemplateView):
    """Loads the Route 4 Page"""
    template_name = 'maps/four.html'


class FiveA(generic.TemplateView):
    """Loads the Route 5 A Page"""
    template_name = 'maps/fivea.html'


class FiveB(generic.TemplateView):
    """Loads the Route 5 B Page"""
    template_name = 'maps/fiveb.html'


class Six(generic.TemplateView):
    """Loads the Route 6 Page"""
    template_name = 'maps/six.html'


class AllRoutes(generic.TemplateView):
    """Loads All the Routes on one Page"""
    template_name = 'maps/all_routes.html'