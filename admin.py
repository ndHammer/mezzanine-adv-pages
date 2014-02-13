from django.contrib import admin
from mezzanine.pages.admin import PageAdmin, DisplayableAdminForm
from mezzanine_advanced_pages.models import AdvancedPage
from mezzanine.boot import fields
from copy import deepcopy
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


admin.site.register(AdvancedPage, AdvancedPageAdmin)