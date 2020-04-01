from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from home.views import \
    OtherViewSet, TempHotelReservationViewSet, TicketViewSet, TravelHotelReservationViewSet, \
    VisaViewSet, ClientViewSet

from home import views


router = routers.DefaultRouter()
# router.register(r'services', ServiceViewSet)
# router.register(r'insurances', InsuranceViewSet)
# router.register(r'omras', OmraViewSet)
# router.register(r'organizedjourneys', OrganizedJourneyViewSet)
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
    
    # service api urls 
    path('services/', views.ServiceList.as_view()),
    path('services/<int:pk>/', views.ServiceDetail.as_view()),

    # insurance api urls
    path('insurances/', views.InsuranceList.as_view()),
    path('insurances/<int:pk>/', views.InsuranceDetail.as_view()),

    # omra api urls
    path('omras/', views.OmraList.as_view()),
    path('omras/<int:pk>/', views.OmraDetail.as_view()),

    # organizedjourney api urls
    path('organizedjourneys/', views.OrganizedJourneyList.as_view()),
    path('organizedjourneys/<int:pk>/', views.OrganizedJourneyDetail.as_view()),
]