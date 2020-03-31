from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from home.models import *
from home.serializers import *

# Create your views here.


def index(request):
    return render(request, "index.html", context={})






# ----- api views ------ #

class ServiceViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class InsuranceViewSet(ModelViewSet):
    queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializer

class OmraViewSet(ModelViewSet):
    queryset = Omra.objects.all()
    serializer_class = OmraSerializer

class OrganizedJourneyViewSet(ModelViewSet):
    queryset = OrganizedJourney.objects.all()
    serializer_class = OrganizedJourneySerializer

class OtherViewSet(ModelViewSet):
    queryset = Other.objects.all()
    serializer_class = OtherSerializer

class TempHotelReservationViewSet(ModelViewSet):
    queryset = TempHotelReservation.objects.all()
    serializer_class = TempHotelReservationSerializer

class TicketViewSet(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class TravelHotelReservationViewSet(ModelViewSet):
    queryset = TravelHotelReservation.objects.all()
    serializer_class = TravelHotelReservationSerializer

class VisaViewSet(ModelViewSet):
    queryset = Visa.objects.all()
    serializer_class = VisaSerializer


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer