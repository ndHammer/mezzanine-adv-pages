from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from mezzanine_blocks.models import ImageBlock, RichBlock
from django.http import HttpResponseRedirect
from mezzanine_advanced_pages.models import RegionBlocks, AdvancedPage
from django.core.urlresolvers import reverse
import uuid

# Create your views here.
@require_http_methods(["POST"])
def add_blocktoregion(request):
    #import pdb;pdb.set_trace()
    if request.POST['submit'] == 'richtext':
        advpage = AdvancedPage.objects.get(pk=request.POST['page_id'])
        richtext = RichBlock(content='New Text Block', title=".".join((advpage.slug, request.POST['region'], str(uuid.uuid1()))))
        richtext.save()
        regionblock = RegionBlocks(region=request.POST['region'], page=advpage, richtext_block=richtext, order=1);
        regionblock.save()
        
    if request.POST['submit'] == 'imageblock':
        advpage = AdvancedPage.objects.get(pk=request.POST['page_id'])
        imageblock = ImageBlock(title=".".join((advpage.slug, request.POST['region'], str(uuid.uuid1()))))
        imageblock.save()
        regionblock = RegionBlocks(region=request.POST['region'], page=advpage, image_block=imageblock, order=1);
        regionblock.save()
    return HttpResponseRedirect(reverse('page', args=(advpage.slug,)))