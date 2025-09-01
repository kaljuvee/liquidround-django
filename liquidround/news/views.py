from django.views import generic

from statpages.mixins import TopMenu
from . import models


class NewsList(TopMenu, generic.ListView):
    model = models.News
    template_name = 'news/list.html'
    paginate_by = 10
    context_object_name = 'news'

    def dispatch(self, request, *args, **kwargs):
        if request.is_ajax():
            self.template_name = 'news/list_unstyled.html'
        return super(NewsList, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(NewsList, self).get_context_data(*args, **kwargs)
        context['active_app'] = 'about'
        return context


class NewsDetail(TopMenu, generic.DetailView):
    model = models.News
    template_name = 'news/detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(NewsDetail, self).get_context_data(*args, **kwargs)
        context['active_app'] = 'about'
        return context