from django.contrib import admin

# Register your models here.
from home.models import * 


# admin.site.register(Client) because when user add a service, he should adds a client 
admin.site.register(Service)
# admin.site.register(ServiceClient)
admin.site.register(Omra)
admin.site.register(Insurance)
admin.site.register(OrganizedJourney)
admin.site.register(Payment)
admin.site.register(TempHotelReservation)
admin.site.register(Ticket)
admin.site.register(Other)
admin.site.register(TravelHotelReservation)
admin.site.register(Visa)
# admin.site.register(VisaRdv)
# admin.site.register(VisaRequestForm)
admin.site.register(CancelService)
admin.site.register(Refund)
