from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    # url(r'^home', views.HomeView.as_view(), name='index'),
    # url(r'^contactMail', views.ContactView.as_view(), name='contactMail'),
    # url(r'^contactMail', views.HomeView.as_view(), name='contactMail'),

    url(r'^$', views.home, name='home'),
    url(r'^home', views.home, name='home'),
    url(r'^educationPage', views.educationPage, name='educationPage'),
    url(r'^experiencePage', views.experiencePage, name='experiencePage'),
    url(r'^aboutPage', views.aboutPage, name='aboutPage'),
    url(r'^contactPage', views.contactPage, name='contactPage'),
    url(r'^contactMessage', views.contactMessage, name='contactMessage'),
]