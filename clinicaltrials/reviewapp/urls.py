from django.conf.urls.defaults import *
from django.contrib.auth.views import login, logout
from django.views.generic.list_detail import object_list, object_detail

from reviewapp.views import index, user_dump, new_submission, submissions_list, submission_detail
from reviewapp.models import Submission


submissions = {
   'queryset':Submission.objects.all()
}

urlpatterns = patterns('',
    url(r'^accounts/profile/$', submissions_list, name='reviewapp.userhome'),

    url(r'^accounts/submissionlist/$', submissions_list, name='reviewapp.submissionlist'), #same as accounts/profile

    url(r'^accounts/submission/(\d+)/$', submission_detail, 
        name='reviewapp.submission'),

    url(r'^accounts/newsubmission/$', new_submission,
        name='reviewapp.new_submission'),

    url(r'^accounts/userdump/$', user_dump),

    url(r'^accounts/login/$', login, dict(template_name='reviewapp/login.html'),
        name='reviewapp.login'),

    url(r'^accounts/logout/$', logout, dict(next_page='/'),
        name='reviewapp.logout'),
        
    url(r'^$', index, name='reviewapp.home'),  
)
