from pyexpat import model
from re import template
from turtle import home
from venv import create
from django.db import models
from django.db.models import fields
from django.shortcuts import render
from django.views.generic import *
from django.urls import reverse
from .models import Admission, Department, Home, School
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms

# Create your views here.

class HomeList(ListView):
    model = Home
    ordering = ['-id']
    paginate_by = 5

class HomeDetail(DetailView):
    model = Home
    pk_url_kwarg = 'hid'

class HomeCreate(LoginRequiredMixin, CreateView):
    model = Home
    template_name = 'form.html'
    pk_url_kwarg = 'hid'
    fields = ['htitle','hdesc','hlink1name','hlink1','hlink2name','hlink2']

    def get_success_url(self):
        return "/enter/{}".format(self.object.id)

class HomeUpdate(LoginRequiredMixin, UpdateView):
    model = Home
    template_name = 'form.html'
    pk_url_kwarg = 'hid'
    fields = ['htitle','hdesc','hlink1name','hlink1','hlink2name','hlink2']

    def get_success_url(self):
        return "/enter"

class HomeDelete(LoginRequiredMixin, DeleteView):
    model = Home
    pk_url_kwarg = 'hid'
    success_url = "/enter"

class LogListAdmission(ListView):
    model = Admission
    ordering = ['-id']
    paginate_by = 20

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            item = Admission.objects.filter(admit__icontains=query)
        else:
            item = Admission.objects
        return item.order_by('admit')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['query'] = self.request.GET.get('query') or ""
        return ctx

class LogViewAdmission(DetailView):
    model = Admission
    pk_url_kwarg = 'aid'

    def get_object(self):
        admission = super().get_object()
        admission.save()
        return admission

class LogCreateAdmission(LoginRequiredMixin, CreateView):
    model = Admission
    template_name = 'form.html'
    fields = '__all__'

    def get_success_url(self):
        return "/enter/admission/{}".format(self.object.id)

class LogUpdateAdmission(LoginRequiredMixin, UpdateView):
    model = Admission
    template_name = 'form.html'
    pk_url_kwarg = 'aid'
    fields = '__all__'

    def get_success_url(self):
        return "/enter/admission/{}".format(self.object.id)

class LogDeleteAdmission(LoginRequiredMixin, DeleteView):
    model = Admission
    pk_url_kwarg = 'aid'
    success_url = "/enter/admission"

#--------------------------------------------------------------------

class LogListDepartment(ListView):
    model = Department
    ordering = ['depart']
    paginate_by = 20

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            item = Department.objects.filter(depart__icontains=query)
        else:
            item = Department.objects
        return item.order_by('depart')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['query'] = self.request.GET.get('query') or ""
        return ctx

class LogViewDepartment(DetailView):
    model = Department
    pk_url_kwarg = 'did'

    def get_object(self):
        dep = super().get_object()
        dep.save()
        return dep

class LogCreateDepartment(LoginRequiredMixin, CreateView):
    model = Department
    template_name = 'form.html'
    fields = ['depart','admits','schools','ddesc','dfile','dlink1name','dlink1','dlink2name','dlink2']

    def get_form(self):
        form = super().get_form()
        widget = form.fields['schools'].widget
        form.fields['schools'].widget = forms.CheckboxSelectMultiple(choices = widget.choices)
        return form
        
    def get_success_url(self):
        return "/enter/department/{}".format(self.object.id)

class LogUpdateDepartment(LoginRequiredMixin, UpdateView):
    model = Department
    template_name = 'form.html'
    pk_url_kwarg = 'did'
    fields = ['depart','admits','schools','ddesc','dfile','dlink1name','dlink1','dlink2name','dlink2']

    def get_form(self):
        form = super().get_form()
        widget = form.fields['schools'].widget
        form.fields['schools'].widget = forms.CheckboxSelectMultiple(choices = widget.choices)
        return form

    def get_success_url(self):
        return "/enter/department/{}".format(self.object.id)

class LogDeleteDepartment(LoginRequiredMixin, DeleteView):
    model = Department
    pk_url_kwarg = 'did'
    success_url = "/enter/department"

#--------------------------------------------------------------------

class LogListSchool(ListView):
    model = School
    ordering = ['-id']
    paginate_by = 20

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            item = School.objects.filter(name__icontains=query)
        else:
            item = School.objects
        return item.order_by('name')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['query'] = self.request.GET.get('query') or ""
        return ctx

class LogViewSchool(DetailView):
    model = School
    pk_url_kwarg = 'sid'

    def get_object(self):
        dep = super().get_object()
        dep.save()
        return dep

class LogCreateSchool(LoginRequiredMixin, CreateView):
    model = School
    template_name = 'form.html'
    fields = '__all__'

    def get_success_url(self):
        return "/enter/school/{}".format(self.object.id)

class LogUpdateSchool(LoginRequiredMixin, UpdateView):
    model = School
    template_name = 'form.html'
    pk_url_kwarg = 'sid'
    fields = '__all__'

    def get_success_url(self):
        return "/enter/school/{}".format(self.object.id)

class LogDeleteSchool(LoginRequiredMixin, DeleteView):
    model = School
    pk_url_kwarg = 'sid'
    success_url = "/enter/school"
