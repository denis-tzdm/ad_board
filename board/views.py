from django.views.generic import ListView, DetailView
from .models import Ad


class AdList(ListView):
    model = Ad
    ordering = '-create_ts'
    template_name = 'board/ad_list.html'
    context_object_name = 'ads'
    paginate_by = 10


class AdDetail(DetailView):
    model = Ad
    template_name = 'board/ad_detail.html'
    context_object_name = 'ad'
