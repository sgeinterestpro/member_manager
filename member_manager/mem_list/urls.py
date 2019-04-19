
from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns=[
    url('^add$',views.get_add),
    url('^add_hand$',views.add_list),
    url('^member_list$',views.member_list),
    url('^member_edit/(\d+)$',views.member_edit),
    url('^edit_hand$',views.member_edit_hand),
    url('^delete/(\d+)$',views.member_delete),
    url('^user_list$',views.get_userlist),
    url('^hand_user_edit$',views.hand_user_edit),
    url('^get_user_edit/(\d+)$',views.get_user_edit),
    url('^delete_user/(\d+)$',views.delete_user),
    url('^apply_list$',views.apply_list),
    url('^apply_pass/(\d+)$',views.apply_pass),
    url('^refuse/(\d+)$',views.refuse),
    url('^refuse_hand$',views.refuse_hand),
]
