from django.db import models
from mezzanine.pages.models import Page
from mezzanine_blocks.models import RichBlock, ImageBlock, Block
# Create your models here.

class AdvancedPage(Page):
    layout = models.CharField(max_length=100, default="default")
    image_blocks = models.ManyToManyField(ImageBlock, through='RegionBlocks')
    richtext_blocks = models.ManyToManyField(RichBlock, through='RegionBlocks')
    blocks = models.ManyToManyField(Block, through='RegionBlocks')
    
    @property
    def get_layout(self):
        return "layouts/"+self.layout+".html"
    
    def getblockbyregion(self, region):
        blocks = self.richtext_blocks.all()
        return blocks
    
class RegionBlocks(models.Model):
    page = models.ForeignKey(AdvancedPage)
    image_block = models.ForeignKey(ImageBlock, null=True)
    richtext_block = models.ForeignKey(RichBlock, null=True)
    block = models.ForeignKey(Block, null=True)
    region = models.CharField(max_length=100)
    order = models.IntegerField()