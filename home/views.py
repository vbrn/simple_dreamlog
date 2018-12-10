from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Dreams_log

# Create your views here.
class HomeListView(ListView):
    model = Dreams_log

class PostView(DetailView):
    model = Dreams_log
    
class CreateView(CreateView):
    model = Dreams_log
    fields = ['title', 'content','rating','created_by']
    success_url = reverse_lazy('home')

class UpdateView(UpdateView):
    model = Dreams_log
    fields = ['title', 'content','rating']
    success_url = reverse_lazy('home')

class DeleteView(DeleteView):
    models = Dreams_log
    success_url = reverse_lazy('home')
    def get_queryset(self):
        queryset = Dreams_log.objects.all().filter(created_by=self.request.user)
        return queryset
 
