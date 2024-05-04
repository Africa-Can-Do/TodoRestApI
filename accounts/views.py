from django.http import JsonResponse
from django.views.generic.edit import FormView
from django.contrib.auth import login
from .forms import CustomUserCreationForm

class RegisterView(FormView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = '/home'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        # Prepare the response data
        response_data = {
            'email': user.email,
            'firstname': user.firstname,
            'lastname': user.lastname,
            'phone': user.phone,
            'department': user.department.name, # Assuming department is a ForeignKey
            'username': user.username,
        }
        return JsonResponse(response_data, status=201)
