from django.contrib.admin.views.decorators import staff_member_required
from django.conf.urls import patterns, url
from mezzanine_advanced_pages import views

urlpatterns = patterns('',
    url(r'^add_blocktoregion', staff_member_required(views.add_blocktoregion), name='add-block-to-region'),
    url(r'^delete_block', staff_member_required(views.delete_block), name='advpage-block-delete')
)
