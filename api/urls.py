from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    url(r'pizza/$', views.PizzaList.as_view()),
    url(r'pizza/(?P<pk>[0-9]+)/$', views.PizzaDetails.as_view()),
    url(r'topping/$', views.ToppingsList.as_view()),
    url(r'topping/(?P<pk>[0-9]+)/$', views.ToppingDetails.as_view()),
    url(r'pizzatype/(?P<pk>[0-9]+)/$', views.PizzaType.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
