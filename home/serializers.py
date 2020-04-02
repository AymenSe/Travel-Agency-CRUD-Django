from rest_framework import serializers
from home.models import *
from drf_writable_nested.serializers import WritableNestedModelSerializer



class InsuranceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Insurance
		fields = '__all__'

class OmraSerializer(serializers.ModelSerializer):
	class Meta:
		model = Omra
		fields = '__all__'


class OrganizedJourneySerializer(serializers.ModelSerializer):
	class Meta:
		model = OrganizedJourney
		fields = '__all__'

class OtherSerializer(serializers.ModelSerializer):
	class Meta:
		model = Other
		fields = '__all__'


class TempHotelReservationSerializer(serializers.ModelSerializer):
	class Meta:
		model = TempHotelReservation
		fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
	class Meta:
		model = Ticket
		fields = '__all__'

class TravelHotelReservationSerializer(serializers.ModelSerializer):
	class Meta:
		model = TravelHotelReservation
		fields = '__all__'

class VisaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Visa
		fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
	class Meta:
		model = Client
		fields = '__all__'



class ServiceSerializer(WritableNestedModelSerializer):
	client = ClientSerializer(many=True) # m2m
	insurance = InsuranceSerializer() # o2o
	omra = OmraSerializer() # o2o
	organized_journey = OrganizedJourneySerializer() # o2o
	other = OtherSerializer() # o2o
	temp_hotel_reservation = TempHotelReservationSerializer() # o2o
	ticket = TicketSerializer() # o2o
	travel_hotel_reservation = TravelHotelReservationSerializer() # o2o
	visa = VisaSerializer() # o2o

	class Meta:
		model = Service
		fields = '__all__'

