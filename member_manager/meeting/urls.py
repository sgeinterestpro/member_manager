from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns=[
    url('^index$',views.get_index),
    url('^addmeeting$',views.add_meeting),
    url('^querymeetings$',views.query_meetings),
]
