from django.contrib.admin.views.decorators import staff_member_required
from django.conf.urls import patterns, url
from mezzanine_advanced_pages.views import add_blocktoregion

urlpatterns = patterns('',
    url(r'^add_blocktoregion', staff_member_required(add_blocktoregion), name='add-block-to-region')
)
