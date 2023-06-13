from django.shortcuts import redirect

def auth_middleware(get_response):
    def middleware(request):
        if not request.session.get('user'):
            return redirect('index')
        response = get_response(request)
        return response
    return middleware