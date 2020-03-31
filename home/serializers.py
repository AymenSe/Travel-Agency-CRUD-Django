from rest_framework import serializers
from home.models import *

class ServiceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Service
		fields = '__all__'


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