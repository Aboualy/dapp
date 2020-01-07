from django.shortcuts import render

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Game


def home(request):
    context = {
        'games': Game.objects.all(),
        'rang': range(len(Game.objects.all())//2+1),
    }
    return render(request, 'gameboard/home.html', context)


class GameListView(ListView):
    model = Game
    template_name = 'gameboard/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'games'
    ordering = ['-date_posted']


class GameDetailView(DetailView):
    model = Game


class GameCreateView(LoginRequiredMixin, CreateView):
    model = Game
    fields = ['title', 'url', 'description']

    def form_valid(self, form):
        form.instance.developer = self.request.user
        return super().form_valid(form)


class GameUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Game
    fields = ['title', 'url', 'description']

    def form_valid(self, form):
        form.instance.developer = self.request.user
        return super().form_valid(form)

    def test_func(self):
        game = self.get_object()
        if self.request.user == game.developer:
            return True
        return False


class GameDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Game
    success_url = '/'

    def test_func(self):
        game = self.get_object()
        if self.request.user == game.developer:
            return True
        return False


def about(request):
    return render(request, 'gameboard/about.html', {'title': 'About'})