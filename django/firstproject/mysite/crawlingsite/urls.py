from django.urls import path
#from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
        path('', views.index, name='index'),

#    path('', views.post_list, name='post_list'),
#    path('delivery_food.html', TemplateView.as_view(template_name="crawlingsite/delivery_food.html"), name='delivery_food'),
    #path('delivery_food', views.delivery_food, name='delivery_food'),
#    path('delivery_time.html', TemplateView.as_view(template_name="crawlingsite/delivery_time.html"), name='delivery_time'),
    #url(r'^delivery_food', TemplateView.as_view(template_name="crawlingsite/delivery_food.html"), name='delivery_food')
]
