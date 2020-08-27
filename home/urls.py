from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from home import views


# router = routers.DefaultRouter()
# router.register(r'services', ServiceViewSet)
# router.register(r'insurances', InsuranceViewSet)
# router.register(r'omras', OmraViewSet)
# router.register(r'organizedjourneys', OrganizedJourneyViewSet)
# router.register(r'others', OtherViewSet)
# router.register(r'temphotelreservations', TempHotelReservationViewSet)
# router.register(r'tickets', TicketViewSet)
# router.register(r'travelhotelreservations', TravelHotelReservationViewSet)
# router.register(r'visas', VisaViewSet)
# router.register(r'clients', ClientViewSet)




'''  ---------------------------------------  '''
app_name = 'home'
urlpatterns = [
    # service api urls 
    path('services/', views.ServiceList.as_view(), name="services"),
    path('services/<int:pk>/', views.ServiceDetail.as_view()),

    # insurance api urls
    path('insurances/', views.InsuranceList.as_view(), name="insurances"),
    path('insurances/<int:pk>/', views.InsuranceDetail.as_view()),

    # omra api urls
    path('omras/', views.OmraList.as_view(), name="omras"),
    path('omras/<int:pk>/', views.OmraDetail.as_view()),

    # organizedjourney api urls
    path('organizedjourneys/', views.OrganizedJourneyList.as_view(), name="organizedjourneys"),
    path('organizedjourneys/<int:pk>/', views.OrganizedJourneyDetail.as_view()),

    # other api urls
    path('others/', views.OtherList.as_view(), name="others"),
    path('others/<int:pk>/', views.OtherDetail.as_view()),

#    # temphotelreservation api urls
#     path('temphotelreservations/', views.TempHotelReservationList.as_view(), name="temphotelreservations"),
#     path('temphotelreservations/<int:pk>/', views.TempHotelReservationDetail.as_view()),
 
    # tickets api urls
    path('tickets/', views.TicketList.as_view(), name="tickets"),
    path('tickets/<int:pk>/', views.TicketDetail.as_view()),

    # travelhotelreservations api urls
    path('travelhotelreservations/', views.TravelHotelReservationList.as_view(), name="travelhotelreservations"),
    path('travelhotelreservations/<int:pk>/', views.TravelHotelReservationDetail.as_view()),

    # visas api urls
    path('visas/', views.VisaList.as_view(), name="visas"),
    path('visas/<int:pk>/', views.VisaDetail.as_view()), 

    # clients api urls
    path('clients/', views.ClientList.as_view(), name="clients"),
    path('clients/<int:pk>/', views.ClientDetail.as_view()),  

    # countries api urls
    path('countries/', views.CountryList.as_view(), name="countries"),
    path('countries/<int:pk>/', views.CountryDetail.as_view()),  

    # regions api urls
    path('regions/', views.RegionList.as_view(), name="regions"),
    path('regions/<int:pk>/', views.RegionDetail.as_view()),  

    # cities api urls
    path('cities/', views.CityList.as_view(), name="cities"),
    path('cities/<int:pk>/', views.CityDetail.as_view()),  
]

urlpatterns = format_suffix_patterns(urlpatterns)