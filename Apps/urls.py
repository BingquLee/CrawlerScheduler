from django.conf.urls import url
from django.urls import include

from Apps.Jobs.views import Jobs

urlpatterns = [
    url(r'jobs/', Jobs.as_view()),
]
