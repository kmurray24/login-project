from django.contrib import admin
from .models import Expert, Period, Case, Claim

admin.site.register(Period)
admin.site.register(Case)
admin.site.register(Expert)
admin.site.register(Claim)
