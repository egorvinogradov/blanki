# coding:utf-8
from django.core.urlresolvers import reverse


def project_urls(request):
    _base_urls = [
        reverse('blanki-naoplatu'),
    ]
    full_path = request.get_full_path()
    for base_url in _base_urls:
        if full_path.startswith(base_url):
            return {'project_url': base_url}
    return {}
