
from django.conf.urls import url
from django.contrib import admin
from search.views import IndexView, PlayerView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index_view'),
    url(r'^(?P<player_url>.*)', PlayerView.as_view(), name='player_view'),
]
