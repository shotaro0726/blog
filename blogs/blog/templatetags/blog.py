from django import template
from django.utils.safestring import mark_safe
import markdown
from markdownx.utils import markdownify
from markdownx.settings import (
    MARKDOWNX_MARKDOWN_EXTENSIONS,
    MARKDOWNX_MARKDOWN_EXTENSION_CONFIGS
)
from markdown.extensions import Extension
from blog.models import Category, Tag
from blog.forms import PostSearchForm

register = template.Library()

@register.inclusion_tag('blog/category_and_tag_list.html')
def create_category_and_tag_list():
    return {
        'category_list': Category.objects.all(),
        'tag_list': Tag.objects.all(),
    }

@register.inclusion_tag('blog/search_form.html')
def create_search_form(request):
    form = PostSearchForm(request.GET or None)
    return {'form': form}

@register.simple_tag
def url_replace(request, field, value):
    url_dict = request.GET.copy()
    url_dict[field] = str(value)
    return url_dict.urlencode()

@register.filter
def markdown_to_html(text):
    return mark_safe(markdownify(text))

class EscapeHtml(Extension):
    def extendMarkdown(self, md):
        md.preprocessors.deregister('html_block')
        md.inlinePatterns.deregister('html')

@register.filter
def markdown_to_html_with_escape(text):
    extensions = MARKDOWNX_MARKDOWN_EXTENSIONS + [EscapeHtml()]
    html = markdown.markdown(text, extensions=extensions, extension_configs=MARKDOWNX_MARKDOWN_EXTENSION_CONFIGS)
    return mark_safe(html)
