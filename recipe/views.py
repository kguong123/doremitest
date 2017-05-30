# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView

from django.views.generic.edit import FormView
from django.db.models import Q

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from DjangoApp.views import LoginRequiredMixin
from django.shortcuts import redirect
from .forms import *
from .models import *


# Create your views here.


class RecipeLV(ListView) :
    model = Recipe
    template_name = 'recipe/recipe_all.html'
    context_object_name = 'recipes'
    paginate_by = 8

class RecipeDV(DetailView) :
    model = Recipe


'''
class RecipeCV(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = ['title', 'slug', 'foodname', 'titleimage', 'servings','cookingtime','viewcount','scraps', 'owner']
    template_name = 'recipe/recipe_form.html'

    def get_context_data(self, **kwargs):
        context = super(RecipeCV, self).get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = foodinfoInlineFormSet(self.request.POST, self.request.FILES)
        else:
            context['formset'] = foodinfoInlineFormSet()
        return context

    def form_valid(self, form):
        form.instance.owner = self.request.user
        context = self.get_context_data()
        formset = context['formset']
        for photoform in formset:
            photoform.instance.owner = self.request.user
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect('recipe/recipe_all.html', pk=self.object.id)
        else:
            return self.render_to_response(self.get_context_data(form=form))
'''
class RecipeCV(LoginRequiredMixin, CreateView):
    template_name = 'recipe/recipe_form.html'
    model = Recipe
    form_class = RecipeForm

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        foodinfo_form = foodinfoInlineFormSet()
        recipeinfo_form = RecipeinfoInlineFormSet()
        return self.render_to_response(
            self.get_context_data(form=form,
                                  foodinfo_form=foodinfo_form,
                                  recipeinfo_form=recipeinfo_form))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        foodinfo_form = foodinfoInlineFormSet(self.request.POST)
        recipeinfo_form = RecipeinfoInlineFormSet(self.request.POST)
        if (form.is_valid() and foodinfo_form.is_valid() and
            recipeinfo_form.is_valid()):
            return self.form_valid(form, foodinfo_form, recipeinfo_form)
        else:
            return self.form_invalid(form, foodinfo_form, recipeinfo_form)

    def form_valid(self, form, foodinfo_form, recipeinfo_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save()
        foodinfo_form.instance = self.object
        foodinfo_form.save()
        recipeinfo_form.instance = self.object
        recipeinfo_form.save()
        return redirect('recipe/recipe_all.html', pk=self.object.id)

    def form_invalid(self, form, foodinfo_form, recipeinfo_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form,
                                  foodinfo_form=foodinfo_form,
                                  recipeinfo_form=recipeinfo_form))

class RecipeDeleteView(LoginRequiredMixin, DeleteView) :
    model = Recipe
    success_url = reverse_lazy('recipe:index')