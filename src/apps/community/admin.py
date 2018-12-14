from django.contrib import admin

from .models import Extension, Synonym, Community


class ExtensionAdmin(admin.ModelAdmin):
    """..."""
    pass


class SynonymAdmin(admin.ModelAdmin):
    """..."""
    pass


class CommunityAdmin(admin.ModelAdmin):
    """..."""
    pass

admin.site.register(Extension, ExtensionAdmin)
admin.site.register(Synonym, SynonymAdmin)
admin.site.register(Community, CommunityAdmin)
