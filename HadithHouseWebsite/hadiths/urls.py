from django.conf.urls import url
from django.contrib import admin

from hadiths import views
from hadiths import apiviews

urlpatterns = [
  url(r'^admin/', admin.site.urls),
  url(r'^$', views.index, name='index'),
  url(r'^apis/books/?$', apiviews.BookSetView.as_view()),
  url(r'^apis/books/(?P<id>[0-9]+)$', apiviews.BookView.as_view()),
  url(r'^apis/bookvolumes/?$', apiviews.BookVolumeSetView.as_view()),
  url(r'^apis/bookvolumes/(?P<id>[0-9]+)$', apiviews.BookVolumeView.as_view()),
  url(r'^apis/bookchapters/?$', apiviews.BookChapterSetView.as_view()),
  url(r'^apis/bookchapters/(?P<id>[0-9]+)$', apiviews.BookChapterView.as_view()),
  url(r'^apis/booksections/?$', apiviews.BookSectionSetView.as_view()),
  url(r'^apis/booksections/(?P<id>[0-9]+)$', apiviews.BookSectionView.as_view()),
  url(r'^apis/persons/?$', apiviews.PersonSetView.as_view()),
  url(r'^apis/persons/(?P<id>[0-9]+)$', apiviews.PersonView.as_view()),
  url(r'^apis/hadithtags/?$', apiviews.HadithTagSetView.as_view()),
  url(r'^apis/hadithtags/(?P<id>\w+)$', apiviews.HadithTagView.as_view()),
  url(r'^apis/hadiths/?$', apiviews.HadithSetView.as_view()),
  url(r'^apis/hadiths/(?P<id>([0-9]+|random))$', apiviews.HadithView.as_view()),
  url(r'^apis/chains/?$', apiviews.ChainSetView.as_view()),
  url(r'^apis/chains/(?P<id>[0-9]+)$', apiviews.ChainView.as_view()),
  url(r'^apis/users/?$', apiviews.UserSetView.as_view()),
  url(r'^apis/users/(?P<id>([0-9]+|current))$', apiviews.UserView.as_view()),
]
