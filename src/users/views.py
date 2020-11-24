from django.views.generic import CreateView, View
from django.contrib.auth import get_user_model
from django.template.response import TemplateResponse
from django.urls import reverse_lazy

from .forms import SignupForm, UserSettingsForm


User = get_user_model()

class SignupView(CreateView):
    template_name = 'registration/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('login')


class UserSettingsView(View):
    template_name = 'users/settings.html'
    form_class = UserSettingsForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()

        context = {
            'form': form
        }

        return TemplateResponse(request, template=self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)

        context = {
            'form': form
        }

        if form.is_valid():
            form.save(user=request.user)
            return TemplateResponse(request, template=self.template_name, context=context)

        context['errors'] = form.errors
        return TemplateResponse(request, template=self.template_name, context=context)
