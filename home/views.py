from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet #, GenericViewSet
# from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from home.models import *
from home.serializers import *


<<<<<<< HEAD
# ---- views ---- #
=======
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
>>>>>>> api

def index(request):
    return render(request, "index.html", context={})






# ----- api views ------ #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Service API
class ServiceList(APIView):
    """
    List all services, or create a new service.
    """
    def get(self, request, format=None):
        services = Service.objects.filter(is_active=True)
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ServiceDetail(APIView):
    """
    Retrieve, update or delete a service instance.
    """
    def get_object(self, pk):
        try:
            return Service.objects.get(pk=pk)
        except Service.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        service = self.get_object(pk)
        if service.is_active == False:
            content = {'please move along': 'nothing to see here'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        serializer = ServiceSerializer(service)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        service = self.get_object(pk)
        serializer = ServiceSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        service = self.get_object(pk)
        if service.is_active == True: 
            service.is_active = False
            service.save()
        serializer = ServiceSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
        print(serializer.data)
        return Response(status=status.HTTP_204_NO_CONTENT)
 
# ------------ Fin Service API

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Insurance API
class InsuranceList(APIView):
    """
    List all insurances, or create a new insurance.
    """
    def get(self, request, format=None):
        insurances = Insurance.objects.filter(is_active=True)
        serializer = InsuranceSerializer(insurances, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = InsuranceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class InsuranceDetail(APIView):
    """
    Retrieve, update or delete a insurance instance.
    """
    def get_object(self, pk):
        try:
            return Insurance.objects.get(pk=pk)
        except Insurance.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        insurance = self.get_object(pk)
        if insurance.is_active == False:
            content = {'please move along': 'nothing to see here'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        serializer = InsuranceSerializer(insurance)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        insurance = self.get_object(pk)
        serializer = InsuranceSerializer(insurance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        insurance = self.get_object(pk)
        if insurance.is_active == True: 
            insurance.is_active = False
            insurance.save()
        serializer = InsuranceSerializer(insurance, data=request.data)
        if serializer.is_valid():
            serializer.save()
        print(serializer.data)
        return Response(status=status.HTTP_204_NO_CONTENT)
 
# ------------ Fin Insurance API

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #



# Omra API
class OmraList(APIView):
    """
    List all Omras, or create a new Omra.
    """
    def get(self, request, format=None):
        omras = Omra.objects.filter(is_active=True)
        serializer = OmraSerializer(omras, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OmraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class OmraDetail(APIView):
    """
    Retrieve, update or delete a Omra instance.
    """
    def get_object(self, pk):
        try:
            return Omra.objects.get(pk=pk)
        except Omra.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        omra = self.get_object(pk)
        if omra.is_active == False:
            content = {'please move along': 'nothing to see here'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        serializer = OmraSerializer(omra)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        omra = self.get_object(pk)
        serializer = OmraSerializer(omra, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        omra = self.get_object(pk)
        if omra.is_active == True: 
            omra.is_active = False
            omra.save()
        serializer = OmraSerializer(omra, data=request.data)
        if serializer.is_valid():
            serializer.save()
        print(serializer.data)
        return Response(status=status.HTTP_204_NO_CONTENT)
 
# ------------ Fin Omra API


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #



# OrganizedJourney API
class OrganizedJourneyList(APIView):
    """
    List all OrganizedJourneys, or create a new OrganizedJourney.
    """
    def get(self, request, format=None):
        organized_journeys = OrganizedJourney.objects.filter(is_active=True)
        serializer = OrganizedJourneySerializer(organized_journeys, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OrganizedJourneySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class OrganizedJourneyDetail(APIView):
    """
    Retrieve, update or delete a OrganizedJourney instance.
    """
    def get_object(self, pk):
        try:
            return OrganizedJourney.objects.get(pk=pk)
        except OrganizedJourney.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        organized_journeys = self.get_object(pk)
        if organized_journeys.is_active == False:
            content = {'please move along': 'nothing to see here'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        serializer = OrganizedJourneySerializer(organized_journeys)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        organized_journeys = self.get_object(pk)
        serializer = OrganizedJourneySerializer(organized_journeys, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        organized_journeys = self.get_object(pk)
        if organized_journeys.is_active == True: 
            organized_journeys.is_active = False
            organized_journeys.save()
        serializer = OrganizedJourneySerializer(organized_journeys, data=request.data)
        if serializer.is_valid():
            serializer.save()
        print(serializer.data)
        return Response(status=status.HTTP_204_NO_CONTENT)
 
# ------------ Fin OrganizedJourney API



# class InsuranceViewSet(ModelViewSet):
#     queryset = Insurance.objects.all()
#     serializer_class = InsuranceSerializer

# class OmraViewSet(ModelViewSet):
#     queryset = Omra.objects.all()
#     serializer_class = OmraSerializer

# class OrganizedJourneyViewSet(ModelViewSet):
#     queryset = OrganizedJourney.objects.all()
#     serializer_class = OrganizedJourneySerializer

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
