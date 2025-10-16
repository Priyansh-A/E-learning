from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse

from .models import Course


def subdomain_course_middleware(get_response):
    def middleware(request):
        host = request.get_host()
        host_parts = host.split('.')
        
        # Only process if we have a real subdomain (not www, not localhost, etc.)
        if len(host_parts) > 2 and host_parts[0] not in ['www', 'localhost', '127']:
            try:
                course = get_object_or_404(Course, slug=host_parts[0])
                course_url = reverse('course_detail', args=[course.slug])
                url = '{}://{}{}'.format(
                    request.scheme, '.'.join(host_parts[1:]), course_url
                )
                return redirect(url)
            except Exception as e:
                # If anything fails, just continue normal processing
                print(f"Middleware error: {e}")
                pass
                
        response = get_response(request)
        return response

    return middleware
