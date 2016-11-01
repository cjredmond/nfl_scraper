from django.shortcuts import render
from django.views.generic import TemplateView
from bs4 import BeautifulSoup
import requests

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self):
        context = super().get_context_data()
        if self.request.GET:
            base_url = 'http://www.nfl.com/players/search?category=name&filter={}&playerType=current'

            data = requests.get(base_url.format(self.request.GET.get('player')))
            souper = BeautifulSoup(data.text, 'html.parser')
            all_a_tags = souper.findAll('a')
            target = all_a_tags[43].get('href')
            context['target'] = target

        return context

class PlayerView(TemplateView):
    template_name = 'player.html'

    def get_context_data(self, player_url):
        context = super().get_context_data()
        page = requests.get('http://www.nfl.com/' + player_url)
        souper = BeautifulSoup(page.text, 'html.parser')
        #x = souper.findAll('table')
        x = souper.findAll('table', { "class" : 'data-table1'})[1]



        context['x'] = x
        return context
