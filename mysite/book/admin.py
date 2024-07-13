from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

admin.site.register(UserProfile)
admin.site.register(Member)
admin.site.register(Loan)
admin.site.register(Fine)
admin.site.register(Reservation)


@admin.register(Book)
class ProductAdmin(TranslationAdmin):
    list_display = ("title", "author")

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
