from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import login


class LoginView(View):
    """..."""
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *kwargs):
        """..."""
        print(request.user)
        post = request.POST
        auth_backend = ModelBackend()

        user = auth_backend.authenticate(
            request, post.get('email'), post.get('password')
        )
        
        print(user)

        login(request, user)
        
        return JsonResponse({'status': 'success'})
