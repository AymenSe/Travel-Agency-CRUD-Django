from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet #, GenericViewSet
# from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from home.models import *
from home.serializers import *


# ---- views ---- #

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

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



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #



# Other API
class OtherList(APIView):
    """
    List all Others, or create a new Other.
    """
    def get(self, request, format=None):
        other = Other.objects.filter(is_active=True)
        serializer = OtherSerializer(other, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OtherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class OtherDetail(APIView):
    """
    Retrieve, update or delete a Other instance.
    """
    def get_object(self, pk):
        try:
            return Other.objects.get(pk=pk)
        except Other.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        other = self.get_object(pk)
        if other.is_active == False:
            content = {'please move along': 'nothing to see here'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        serializer = OtherSerializer(other)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        other = self.get_object(pk)
        serializer = OtherSerializer(other, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        other = self.get_object(pk)
        if other.is_active == True: 
            other.is_active = False
            other.save()
        serializer = OtherSerializer(other, data=request.data)
        if serializer.is_valid():
            serializer.save()
        print(serializer.data)
        return Response(status=status.HTTP_204_NO_CONTENT)
 
# ------------ Fin Other API


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# # TempHotelReservation API
# class TempHotelReservationList(APIView):
#     """
#     List all TempHotelReservations, or create a new TempHotelReservation.
#     """
#     def get(self, request, format=None):
#         temp_hotel_reservation = TempHotelReservation.objects.filter(is_active=True)
#         serializer = TempHotelReservationSerializer(temp_hotel_reservation, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = TempHotelReservationSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# class TempHotelReservationDetail(APIView):
#     """
#     Retrieve, update or delete a TempHotelReservation instance.
#     """
#     def get_object(self, pk):
#         try:
#             return TempHotelReservation.objects.get(pk=pk)
#         except TempHotelReservation.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         temp_hotel_reservation = self.get_object(pk)
#         if temp_hotel_reservation.is_active == False:
#             content = {'please move along': 'nothing to see here'}
#             return Response(content, status=status.HTTP_404_NOT_FOUND)
#         serializer = TempHotelReservationSerializer(temp_hotel_reservation)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         temp_hotel_reservation = self.get_object(pk)
#         serializer = TempHotelReservationSerializer(temp_hotel_reservation, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         temp_hotel_reservation = self.get_object(pk)
#         if temp_hotel_reservation.is_active == True: 
#             temp_hotel_reservation.is_active = False
#             temp_hotel_reservation.save()
#         serializer = TempHotelReservationSerializer(temp_hotel_reservation, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         print(serializer.data)
#         return Response(status=status.HTTP_204_NO_CONTENT)
 
# # ------------ Fin TempHotelReservation API

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# Ticket API
class TicketList(APIView):
    """
    List all Tickets, or create a new Ticket.
    """
    def get(self, request, format=None):
        ticket = Ticket.objects.filter(is_active=True)
        serializer = TicketSerializer(ticket, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class TicketDetail(APIView):
    """
    Retrieve, update or delete a Ticket instance.
    """
    def get_object(self, pk):
        try:
            return Ticket.objects.get(pk=pk)
        except Ticket.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        ticket = self.get_object(pk)
        if ticket.is_active == False:
            content = {'please move along': 'nothing to see here'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        serializer = TicketSerializer(ticket)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        ticket = self.get_object(pk)
        serializer = TicketSerializer(ticket, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        ticket = self.get_object(pk)
        if ticket.is_active == True: 
            ticket.is_active = False
            ticket.save()
        serializer = TicketSerializer(ticket, data=request.data)
        if serializer.is_valid():
            serializer.save()
        print(serializer.data)
        return Response(status=status.HTTP_204_NO_CONTENT)
 
# ------------ Fin Ticket API

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# TravelHotelReservation API
class TravelHotelReservationList(APIView):
    """
    List all TravelHotelReservations, or create a new TravelHotelReservation.
    """
    def get(self, request, format=None):
        travel_hotel_reservation = TravelHotelReservation.objects.filter(is_active=True)
        serializer = TravelHotelReservationSerializer(travel_hotel_reservation, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TravelHotelReservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class TravelHotelReservationDetail(APIView):
    """
    Retrieve, update or delete a TravelHotelReservation instance.
    """
    def get_object(self, pk):
        try:
            return TravelHotelReservation.objects.get(pk=pk)
        except TravelHotelReservation.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        travel_hotel_reservation = self.get_object(pk)
        if travel_hotel_reservation.is_active == False:
            content = {'please move along': 'nothing to see here'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        serializer = TravelHotelReservationSerializer(travel_hotel_reservation)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        travel_hotel_reservation = self.get_object(pk)
        serializer = TravelHotelReservationSerializer(travel_hotel_reservation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        travel_hotel_reservation = self.get_object(pk)
        if travel_hotel_reservation.is_active == True: 
            travel_hotel_reservation.is_active = False
            travel_hotel_reservation.save()
        serializer = TravelHotelReservationSerializer(travel_hotel_reservation, data=request.data)
        if serializer.is_valid():
            serializer.save()
        print(serializer.data)
        return Response(status=status.HTTP_204_NO_CONTENT)
 
# ------------ Fin TravelHotelReservation API

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Visa API
class VisaList(APIView):
    """
    List all Visas, or create a new Visa.
    """
    def get(self, request, format=None):
        visa = Visa.objects.filter(is_active=True)
        serializer = VisaSerializer(visa, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = VisaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class VisaDetail(APIView):
    """
    Retrieve, update or delete a Visa instance.
    """
    def get_object(self, pk):
        try:
            return Visa.objects.get(pk=pk)
        except Visa.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        visa = self.get_object(pk)
        if visa.is_active == False:
            content = {'please move along': 'nothing to see here'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        serializer = VisaSerializer(visa)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        visa = self.get_object(pk)
        serializer = VisaSerializer(visa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        visa = self.get_object(pk)
        if visa.is_active == True: 
            visa.is_active = False
            visa.save()
        serializer = VisaSerializer(visa, data=request.data)
        if serializer.is_valid():
            serializer.save()
        print(serializer.data)
        return Response(status=status.HTTP_204_NO_CONTENT)
 
# ------------ Fin Visa API

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Client API
class ClientList(APIView):
    """
    List all Clients, or create a new Client.
    """
    def get(self, request, format=None):
        client = Client.objects.filter(is_active=True)
        serializer = ClientSerializer(client, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ClientDetail(APIView):
    """
    Retrieve, update or delete a Client instance.
    """
    def get_object(self, pk):
        try:
            return Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        client = self.get_object(pk)
        if client.is_active == False:
            content = {'please move along': 'nothing to see here'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        client = self.get_object(pk)
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        client = self.get_object(pk)
        if client.is_active == True: 
            client.is_active = False
            client.save()
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
        print(serializer.data)
        return Response(status=status.HTTP_204_NO_CONTENT)
 
# ------------ Fin Client API


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Country API
class CountryList(APIView):
    """
    List all Countrys, or create a new Country.
    """
    def get(self, request, format=None):
        country = Country.objects.filter(is_active=True)
        serializer = CountrySerializer(country, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CountryDetail(APIView):
    """
    Retrieve, update or delete a Country instance.
    """
    def get_object(self, pk):
        try:
            return Country.objects.get(pk=pk)
        except Country.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        country = self.get_object(pk)
        if country.is_active == False:
            content = {'please move along': 'nothing to see here'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        serializer = CountrySerializer(country)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        country = self.get_object(pk)
        serializer = CountrySerializer(country, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        country = self.get_object(pk)
        if country.is_active == True: 
            country.is_active = False
            country.save()
        serializer = CountrySerializer(country, data=request.data)
        if serializer.is_valid():
            serializer.save()
        print(serializer.data)
        return Response(status=status.HTTP_204_NO_CONTENT)
 
# ------------ Fin Country API


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Region API
class RegionList(APIView):
    """
    List all Regions, or create a new Region.
    """
    def get(self, request, format=None):
        region = Region.objects.filter(is_active=True)
        serializer = RegionSerializer(region, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RegionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class RegionDetail(APIView):
    """
    Retrieve, update or delete a Region instance.
    """
    def get_object(self, pk):
        try:
            return Region.objects.get(pk=pk)
        except Region.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        region = self.get_object(pk)
        if region.is_active == False:
            content = {'please move along': 'nothing to see here'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        serializer = RegionSerializer(region)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        region = self.get_object(pk)
        serializer = RegionSerializer(region, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        region = self.get_object(pk)
        if region.is_active == True: 
            region.is_active = False
            region.save()
        serializer = RegionSerializer(region, data=request.data)
        if serializer.is_valid():
            serializer.save()
        print(serializer.data)
        return Response(status=status.HTTP_204_NO_CONTENT)
 
# ------------ Fin Region API


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# City API
class CityList(APIView):
    """
    List all Citys, or create a new City.
    """
    def get(self, request, format=None):
        city = City.objects.filter(is_active=True)
        serializer = CitySerializer(city, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CityDetail(APIView):
    """
    Retrieve, update or delete a City instance.
    """
    def get_object(self, pk):
        try:
            return City.objects.get(pk=pk)
        except City.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        city = self.get_object(pk)
        if city.is_active == False:
            content = {'please move along': 'nothing to see here'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        serializer = CitySerializer(city)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        city = self.get_object(pk)
        serializer = CitySerializer(city, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        city = self.get_object(pk)
        if city.is_active == True: 
            city.is_active = False
            city.save()
        serializer = CitySerializer(city, data=request.data)
        if serializer.is_valid():
            serializer.save()
        print(serializer.data)
        return Response(status=status.HTTP_204_NO_CONTENT)
 
# ------------ Fin City API

# class InsuranceViewSet(ModelViewSet):
#     queryset = Insurance.objects.all()
#     serializer_class = InsuranceSerializer

# class OmraViewSet(ModelViewSet):
#     queryset = Omra.objects.all()
#     serializer_class = OmraSerializer

# class OrganizedJourneyViewSet(ModelViewSet):
#     queryset = OrganizedJourney.objects.all()
#     serializer_class = OrganizedJourneySerializer

# class OtherViewSet(ModelViewSet):
#     queryset = Other.objects.all()
#     serializer_class = OtherSerializer

# class TempHotelReservationViewSet(ModelViewSet):
#     queryset = TempHotelReservation.objects.all()
#     serializer_class = TempHotelReservationSerializer

# class TicketViewSet(ModelViewSet):
#     queryset = Ticket.objects.all()
#     serializer_class = TicketSerializer

# class TravelHotelReservationViewSet(ModelViewSet):
#     queryset = TravelHotelReservation.objects.all()
#     serializer_class = TravelHotelReservationSerializer

# class VisaViewSet(ModelViewSet):
#     queryset = Visa.objects.all()
#     serializer_class = VisaSerializer


# class ClientViewSet(ModelViewSet):
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer
