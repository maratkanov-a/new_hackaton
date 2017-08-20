# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView
from django.views.generic import DetailView
from django.views.generic import ListView

from front_site.forms import CreateCompanyForm, CreateEventForm, UpdateCompanyForm
from front_site.models import Company, Events


class MainPage(ListView):
    template_name = 'index.html'
    model = Events


class CompanyCreateView(CreateView):
    template_name = 'company_create.html'
    model = Company
    form_class = CreateCompanyForm
    success_url = reverse_lazy('front_site:index')


class CompanyUpdateView(UpdateView):
    template_name = 'company_update.html'
    model = Company
    form_class = UpdateCompanyForm
    success_url = reverse_lazy('front_site:index')


class EventCreateView(CreateView):
    template_name = 'event_create.html'
    model = Events
    form_class = CreateEventForm
    success_url = reverse_lazy('front_site:index')

    def form_valid(self, form):
        user = self.request.user
        form.instance.company = Company.objects.filter(user=user).first()
        return super(EventCreateView, self).form_valid(form)


class EventDetailView(DetailView):
    template_name = 'event_detail.html'
    model = Events


def event_subscribe(request, pk):
    Events.objects.filter(id=pk).first().users.add(request.user)
    return redirect('front_site:index')
