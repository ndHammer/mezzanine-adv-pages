from django.contrib import admin
from mezzanine.pages.admin import PageAdmin, DisplayableAdminForm
from mezzanine_advanced_pages.models import AdvancedPage, RegionBlocks
from mezzanine.boot import fields
from copy import deepcopy
from pdb import Pdb
import pdb
# Register your models here.

advpage_extra_fieldsets = ((None, {"fields": ("layout",)}),)

class AdvancedPageAdminForm(DisplayableAdminForm):
    
    def clean_slug(self):
        """
        Save the old slug to be used later in PageAdmin.model_save()
        to make the slug change propagate down the page tree.
        """
        self.instance._old_slug = self.instance.slug
        return self.cleaned_data['slug']

class AdvancedPageAdmin(PageAdmin):
    form = AdvancedPageAdminForm
    fieldsets = deepcopy(PageAdmin.fieldsets) + advpage_extra_fieldsets
    
    def save_model(self, request, obj, form, change):
        """
        Override the save method to remove all connected blocks
        otherwise they would be orphaned. This is a cheap way to do this
        would be better to have it tell the user what block were orphaned
        and have them choose where they should go
        """
        #RegionBlocks.objects.filter(page=obj.id).delete()
        super(PageAdmin, self).save_model(request, obj, form, change)


admin.site.register(AdvancedPage, AdvancedPageAdmin)