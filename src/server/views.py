#from django.conf import settings
from django.http import HttpResponseServerError, HttpResponseNotFound
from django.template import RequestContext, loader


def server_error(request, html='server/500.html'):
    """
    500 error handler.
    """
    template = loader.get_template(html)
    context = RequestContext(request)
    return HttpResponseServerError(template.render(context))

def not_found(request, html='server/404.html'):
    """
    404 error handler.
    """
    template = loader.get_template(html)
    context = RequestContext(request)
    return HttpResponseNotFound(template.render(context))