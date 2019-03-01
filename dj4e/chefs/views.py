from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.template.loader import render_to_string

from chefs.models import Chef, Recipe
# from chefs.forms import RecipeForm

# Create your views here.

class MainView(LoginRequiredMixin, View) :
    def get(self, request):
        mc = Recipe.objects.all().count();
        al = Chef.objects.all();

        ctx = { 'recipe_count': mc, 'chef_list': al };
        return render(request, 'chefs/chef_list.html', ctx)
