from .models import Book
from modeltranslation.translator import TranslationOptions, register


@register(Book)
class BookTranslationOptions(TranslationOptions):
    fields = ('title', 'author')