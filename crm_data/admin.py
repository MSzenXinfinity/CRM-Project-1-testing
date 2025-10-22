from django.contrib import admin
from crm_data.models import *
# Register your models here.

admin.site.register(Person)
admin.site.register(CallingSheet)
admin.site.register(Interested)
admin.site.register(Escalation)
admin.site.register(PaymentConfirmation)
admin.site.register(PaymentDone)