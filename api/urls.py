from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    url(r'pizza/$', views.PizzaList.as_view(), name='pizza'),
    url(r'pizza/(?P<pk>[0-9]+)/$', views.PizzaDetails.as_view(), name='pizzadetails'),
    url(r'addtoppings/(?P<pk>[0-9]+)/$', views.AddToppings.as_view(), name='addtoppings'),
    url(r'topping/$', views.ToppingsList.as_view(), name='topping'),
    url(r'topping/(?P<pk>[0-9]+)/$', views.ToppingDetails.as_view(), name='toppingdetails'),
    url(r'pizzatype/(?P<pk>[0-9]+)/$', views.PizzaType.as_view(), name='pizzatype'),
    url(r'menu/$', views.PizzaMenu.as_view(), name='pizzamenu'),
    # url(r'menu/(?P<pk>[0-9]+)/$', views.PizzaMenu.as_view(), name='pizzamenudetails'),
    # url(r'pizzad/(?P<pk>[0-9]+)/$', views.PizzaDetailView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
