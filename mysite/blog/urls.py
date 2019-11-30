from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
	path('', views.post.list, name = 'post_list'),
	path('<int:year>/<int:month>/<int:day>/<slug:post>/',
		view.post_details, name='post_details')
]