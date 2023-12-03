from django.views.generic import TemplateView
from .models import Claim
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.template.defaulttags import register

class TimeEntry(TemplateView):
     template_name = "timeentry.html"


class Home(TemplateView):
     model = Claim
     template_name = "home.html"

     def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)

          claim_summary  = Claim.get_claim_summary(self)
          context['claim_summary']  = claim_summary
          return context

     @method_decorator(login_required)
     def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
     
     @register.filter
     def get_value(dictionary, key):
          return dictionary.get(key)