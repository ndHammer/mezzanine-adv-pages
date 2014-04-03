from django.contrib.auth.models import User
from django import template
from django.template import loader
import logging
from mezzanine_blocks.models import ImageBlock, RichBlock, Block



register = template.Library()
logger = logging.getLogger(__name__)


def block_region(context, page, region):
    try:
        flatblocks = context['flatblocks']
    except:
        flatblocks = {}
    blocks = page.advancedpage.getblockbyregion(region)
    #import pdb;pdb.set_trace()
    if blocks is not None:
        flatblocks[region] = ""
        for block in blocks:
            if block.__class__.__name__ == "ImageBlock":
                template_name = 'blocks/image_block.html'
                region_id = block.region.get(image_block=block, region=region, page=page).id
            elif block.__class__.__name__ == "RichBlock":
                template_name = 'blocks/block.html'
                region_id = block.region.get(richtext_block=block, region=region, page=page).id
            else:
                template_name = 'blocks/block.html'
                region_id = block.region.get(block=block, region=region).id
            new_ctx = template.Context({})
            new_ctx.update(context)
            new_ctx.update({'flatblock':block, 'block_region_id': region_id})
            tmpl = loader.get_template(template_name)
            flatblocks[region] += tmpl.render(new_ctx)
    else:
        flatblocks[region] = ""
        return context
    ret_ctx = template.Context({})
    ret_ctx.update(context)
    ret_ctx.update({'renderedflatblocks': flatblocks, 'region': region})
    return ret_ctx

register.inclusion_tag('regions/block_region.html', takes_context=True)(block_region)

def list_available_blocks():
    new_ctx = template.Context({})
    new_ctx.update({
        'ImageBlocks': ImageBlock.objects.all(),
        'RichBlocks': RichBlock.objects.all(),
        'Blocks': Block.objects.all()
        })
    return new_ctx

register.inclusion_tag('regions/avail_blocks.html')(list_available_blocks)  