from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'base_model.html'


class TubeView(TemplateView):
    template_name = 'tube_cenica.html'


class DetailVideoView(TemplateView):
    template_name = 'detail.html'
