from django import template
  
register = template.Library()
  
@register.filter()
def get_absolute_url(link,request):
    return request.build_absolute_uri(link)