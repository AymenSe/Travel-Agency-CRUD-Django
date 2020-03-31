from django.urls import path, include
from rest_framework import routers

from home.views import ServiceViewSet, InsuranceViewSet, OmraViewSet, OrganizedJourneyViewSet, \
    OtherViewSet, TempHotelReservationViewSet, TicketViewSet, TravelHotelReservationViewSet, \
    VisaViewSet, ClientViewSet


router = routers.DefaultRouter()
router.register(r'services', ServiceViewSet)
router.register(r'insurances', InsuranceViewSet)
router.register(r'omras', OmraViewSet)
router.register(r'organizedjourneys', OrganizedJourneyViewSet)
router.register(r'others', OtherViewSet)
router.register(r'temphotelreservations', TempHotelReservationViewSet)
router.register(r'tickets', TicketViewSet)
router.register(r'travelhotelreservations', TravelHotelReservationViewSet)
router.register(r'visas', VisaViewSet)
router.register(r'clients', ClientViewSet)




'''  ---------------------------------------  '''
app_name = 'home'
urlpatterns = [
    path('', include(router.urls)),
]