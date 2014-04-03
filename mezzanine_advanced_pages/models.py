from django.db import models
from mezzanine.pages.models import Page
from mezzanine_blocks.models import RichBlock, ImageBlock, Block
from django.conf import settings
import os
import platform
# Create your models here.

def get_layout_choices():
    static_root = os.path.join(settings.PROJECT_ROOT.strip("/"), 'templates', 'layouts');
    layouts = []
    if platform.system() == "Windows":
        list_dir = static_root
    else:
        list_dir = "/"+static_root
    for file in os.listdir(list_dir):
        if file.endswith(".html"):
            layouts.append((os.path.splitext(file)[0], os.path.splitext(file)[0]))
    return layouts


    

LAYOUT_CHOICES = get_layout_choices();

class AdvancedPage(Page):
    layout = models.CharField(max_length=100, choices=LAYOUT_CHOICES)
    image_blocks = models.ManyToManyField(ImageBlock, through='RegionBlocks')
    richtext_blocks = models.ManyToManyField(RichBlock, through='RegionBlocks')
    blocks = models.ManyToManyField(Block, through='RegionBlocks')
    
    @property
    def get_layout(self):
        return "layouts/"+self.layout+".html"
    
    def getblockbyregion(self, region):
        blocks = RegionBlocks.objects.filter(region=region, page_id=self.id)
        retblocks = []
        if blocks:
            for block in blocks:
                if block.image_block:
                   retblocks.append(block.image_block)
                if block.richtext_block:
                   retblocks.append(block.richtext_block)
                if block.block:
                   retblocks.append(block.block) 
        return retblocks

class RegionBlocks(models.Model):
    page = models.ForeignKey(AdvancedPage)
    image_block = models.ForeignKey(ImageBlock, null=True, related_name="region")
    richtext_block = models.ForeignKey(RichBlock, null=True, related_name="region")
    block = models.ForeignKey(Block, null=True, related_name="region")
    region = models.CharField(max_length=100)
    order = models.IntegerField()   