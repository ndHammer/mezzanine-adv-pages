from django.contrib.auth.models import User
from django import template
from django.template import loader
import logging


register = template.Library()
logger = logging.getLogger(__name__)

def block_region(context, page, region):
    blocks = page.advancedpage.getblockbyregion(region)
    context.update({'flatblocks': blocks, 'region': region})
    return context

register.inclusion_tag('regions/block_region.html', takes_context=True)(block_region)

class AdvBlockNode(template.Node):
    """
    Needed a simple block display node, using templates
    and the available context
    """
    def __init__(self, block, template_name):
        self.block = block
        self.template_name = template_name
        

    def render(self, context):
        
        if self.block.__class__.__name__ == "ImageBlock":
            self.template_name = 'mezzanine_blocks/image_block.html'
        else:
            self.template_name = 'mezzanine_blocks/block.html'
        
        self.with_template = True
        
        if self.with_template:
            new_ctx = template.Context({})
            new_ctx.update(context)
                      
        if self.with_template:
            tmpl = loader.get_template(self.template_name)
            new_ctx.update({'flatblock':self.block})
            return tmpl.render(new_ctx)
        else:
            return self.block.content
        
        
def render_block(context, block, template_name=None):
    if template_name is not None:
        if not isinstance(template_name, str):
            raise template.TemplateSyntaxError('template_name is not a string')
    
    return AdvBlockNode(block, template_name)
    
register.simple_tag(takes_context=True)(render_block)