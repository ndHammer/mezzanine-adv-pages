from django.contrib.staticfiles.storage import staticfiles_storage
from django import forms
from mezzanine.conf import settings

tinymce_js = ()

_path = "mezzanine_advanced_pages/js/tinymce/js/tinymce/tinymce.min.js"
_tinymce_js = (staticfiles_storage.url(_path), settings.TINYMCE_SETUP_JS)


class InlineTinyMceWidget(forms.Textarea):
    """
    Setup the JS files and targetting CSS class for a textarea to
    use TinyMCE.
    """

    class Media:
        js = _tinymce_js

    def __init__(self, *args, **kwargs):
        super(InlineTinyMceWidget, self).__init__(*args, **kwargs)
        self.attrs["class"] = "mceEditor"