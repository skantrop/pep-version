from datetime import timedelta
from itertools import product

from django.utils import timezone
from django.db.models import Q
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView

from cart.forms import CartAddProductForm
from .models import *


class MainPageView(ListView):
    model = Food
    template_name = 'index.html'
    context_object_name = 'foods'
    paginate_by = 4

    def get_template_names(self):
        template_name = super(MainPageView, self).get_template_names()
        search = self.request.GET.get('q')
        if search:
            template_name = 'search.html'
        return template_name

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        search = self.request.GET.get('q')
        filter = self.request.GET.get('filter')
        f = Food.objects.get(id=1)
        print(f.company.name)
        if search:
            context['products'] = Food.objects.filter(Q(title__icontains=search)|
                                                       Q(company__name__icontains=search))

        else:
            context['products'] = Food.objects.all()
        return context




class CompanyDetailView(DetailView):
    model = Company
    template_name = 'company_detail.html'
    context_object_name = 'company'
    

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.slug = kwargs.get('slug', None)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        print(self.context)
        context = super().get_context_data(**kwargs)
        context['products'] = Food.objects.filter(company_id=self.slug)
        return context






class FoodDetailView(DetailView):
    model = Food
    template_name = 'food_detail.html'
    context_object_name = 'food'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product']= get_object_or_404(Food, id=1)
        context['cart_product_form'] = CartAddProductForm()
        return context






