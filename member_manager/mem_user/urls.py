
from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns=[
    url('^register$',views.get_register),
    url('^register_hand$',views.post_register),
    url('^login$',views.login_get),
    url('^login_hand$',views.login_post),
    url('^logout$',views.user_logout),
    url('^.*',views.login_get),
]
