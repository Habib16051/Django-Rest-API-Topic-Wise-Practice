from django.shortcuts import render
from django.http import HttpResponse
from apps import forms
from django.views.generic import View, TemplateView, ListView, DetailView

from apps import models


# Create your views here.

class IndexView(ListView):
    context_object_name = 'musician_list'
    model = models.Musician
    template_name = 'apps/index.html'


class MusicianDetail(DetailView):
    context_object_name = 'musician'
    model = models.Musician
    template_name = 'apps/musician_details.html'
