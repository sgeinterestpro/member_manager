from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns=[
    url('^index$',views.get_index),
    url('^get_edit$',views.get_edit),
    url('^host$',views.get_host),
    url('^apply_get/(\d+)$',views.apply_get),
    url('^apply_hand$',views.apply_hand),
    url('^apply_list$',views.apply_list),
    url('^apply_cancel/(\d+)$',views.apply_cancel),
    url('^tree$',views.menu_tree),
]
