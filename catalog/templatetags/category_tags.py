from django import template
from ..models import Category

register = template.Library()

@register.inclusion_tag("catalog/dropdown-category.html")
def show_caregories():
    categories = Category.objects.all()
    return {"categories": categories}
