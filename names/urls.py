from django.urls import path,include
from . import views

urlpatterns = [
	path('',views.Index , name='Index'),
	path('<pk>/',views.person_detail,name='person_detail'),
	path('add/new_person',views.add_name,name='add_name'),
	path('<pk>/add/',views.add_post,name='add_post'),
	path('all/posts',views.all_post,name='all_post'),
]