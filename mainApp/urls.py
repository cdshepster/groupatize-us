from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index,  name='index'),
	url(r'^login/', views.login, name='login'),
	url(r'^groupatize/', views.groupatize, name='groupatize'),
	url(r'^logout/', views.logout, name='logout'),
	url(r'^signup/', views.create_account, name='create_account'),
	url(r'^create/createEvent/', views.create_event, name='create_event'),
	url(r'^create/', views.redir_create_event_page, name='create_event_page'),
	url(r'^join/', views.join_event, name='join_event'),
	url(r'^event/editProject', views.edit_project_idea, name='edit_project'),
	url(r'^event/editEvent', views.edit_event, name='edit_event'),
	url(r'^event/(?P<event_id>[0-9]+)/rate', views.rate_project_ideas, name='rate_event'),
	url(r'^event/(?P<event_id>[0-9]+)/submitratings/', views.submit_ratings, name='submit_ratings'),
	url(r'^event/(?P<event_id>[0-9]+)', views.event_page, name='event_page'),
	url(r'^dashboard/', views.dashboard_page, name='dashboard_page'),
	url(r'^results/(?P<event_id>[0-9]+)', views.show_results, name='show_results')
]
