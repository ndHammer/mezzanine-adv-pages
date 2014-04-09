from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_protect
from mezzanine_blocks.models import ImageBlock, RichBlock, Block
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
        block_title = request.POST['block_title']
        richtext = RichBlock(content='New Text Block', title=block_title)
        richtext.save()
        regionblock = RegionBlocks(region=request.POST['region'], page=advpage, richtext_block=richtext, order=1);
        regionblock.save()
    elif request.POST['submit'] == 'imageblock':
        advpage = AdvancedPage.objects.get(pk=request.POST['page_id'])
        imageblock = ImageBlock(title=block_title)
        imageblock.save()
        regionblock = RegionBlocks(region=request.POST['region'], page=advpage, image_block=imageblock, order=1);
        regionblock.save()
    else:
        advpage = AdvancedPage.objects.get(pk=request.POST['page_id'])
        params = request.POST['submit'].split('__')
        if params[0] == 'richblock':
            block = RichBlock.objects.get(pk=params[1])
            regionblock = RegionBlocks(region=request.POST['region'], page=advpage, richtext_block=block, order=1);
        elif params[0] == 'block':
            block = Block.objects.get(pk=params[1])
            regionblock = RegionBlocks(region=request.POST['region'], page=advpage, block=block, order=1);
        elif params[0] == 'imageblock':
            block = ImageBlock.objects.get(pk=params[1])
            regionblock = RegionBlocks(region=request.POST['region'], page=advpage, image_block=block, order=1);
        regionblock.save()
    return HttpResponseRedirect(reverse('page', args=(advpage.slug,)))

@require_http_methods(["POST"])
@csrf_protect
def delete_block(request):
    """
        Delete Function
        @todo: this may need some work to find the proper region
        
    """
    #import pdb;pdb.set_trace()
    advpage = AdvancedPage.objects.get(pk=request.POST['page_id'])
    blockregion = RegionBlocks(pk=request.POST['block_region_id'])
    blockregion.delete()
    return HttpResponseRedirect(reverse('page', args=(advpage.slug,)))