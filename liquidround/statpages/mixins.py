from . import models

class TopMenu(object):
    def get_context_data(self, *args, **kwargs):
        context = super(TopMenu, self).get_context_data(*args, **kwargs)
        context['top_menu'] = models.Page.objects.filter(top_menu=True)
        context['howitworks'] = True if models.Page.objects.filter(slug='how-it-works').count() > 0 else False
        return context