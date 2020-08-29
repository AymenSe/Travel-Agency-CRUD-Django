from rest_framework import serializers
from home.models import *
from drf_writable_nested.serializers import WritableNestedModelSerializer, NestedUpdateMixin, NestedCreateMixin


class PaymentSerializer(NestedCreateMixin ,NestedUpdateMixin, serializers.ModelSerializer):
	class Meta:
		model = Payment
		fields = ('sum_payment',)


class InsuranceSerializer(NestedCreateMixin ,NestedUpdateMixin, serializers.ModelSerializer):
	class Meta:
		model = Insurance
		fields = '__all__'

class OmraSerializer(NestedCreateMixin ,NestedUpdateMixin, serializers.ModelSerializer):
	class Meta:
		model = Omra
		fields = '__all__'


class OrganizedJourneySerializer(NestedCreateMixin ,NestedUpdateMixin, serializers.ModelSerializer):
	class Meta:
		model = OrganizedJourney
		fields = '__all__'

class OtherSerializer(NestedCreateMixin ,NestedUpdateMixin, serializers.ModelSerializer):
	class Meta:
		model = Other
		fields = '__all__'


# class TempHotelReservationSerializer(NestedCreateMixin ,NestedUpdateMixin, serializers.ModelSerializer):
# 	class Meta:
# 		model = TempHotelReservation
# 		fields = '__all__'


# class TicketSerializer(NestedCreateMixin ,NestedUpdateMixin, serializers.ModelSerializer):
# 	class Meta:
# 		model = Ticket
# 		fields = '__all__'

class TravelHotelReservationSerializer(NestedCreateMixin ,NestedUpdateMixin, serializers.ModelSerializer):
	class Meta:
		model = TravelHotelReservation
		fields = '__all__'

class VisaSerializer(NestedCreateMixin ,NestedUpdateMixin, serializers.ModelSerializer):
	class Meta:
		model = Visa
		fields = '__all__'

class ClientSerializer(NestedCreateMixin ,NestedUpdateMixin, serializers.ModelSerializer):
	class Meta:
		model = Client
		fields = '__all__'

class CountrySerializer(NestedCreateMixin ,NestedUpdateMixin, serializers.ModelSerializer):
	class Meta:
		model = Country
		fields = '__all__'

class RegionSerializer(NestedCreateMixin ,NestedUpdateMixin, serializers.ModelSerializer):
	country = CountrySerializer(required=False)
	class Meta:
		model = Region
		fields = '__all__'

class CitySerializer(NestedCreateMixin ,NestedUpdateMixin, serializers.ModelSerializer):
	region = RegionSerializer(required=False)
	class Meta:
		model = City
		fields = '__all__'

class ServiceSerializer(NestedCreateMixin ,NestedUpdateMixin, serializers.ModelSerializer):
	client = ClientSerializer(many=True) # m2m
	insurance = InsuranceSerializer(required=False) # o2o
	omra = OmraSerializer(required=False) # o2o
	organized_trip = OrganizedJourneySerializer(required=False) # o2o
	other = OtherSerializer(required=False) # o2o
#	temp_hotel_reservation = TempHotelReservationSerializer(required=False) # o2o
#	ticket = TicketSerializer(required=False) # o2o
	travel_hotel_reservation = TravelHotelReservationSerializer(required=False) # o2o
	visa = VisaSerializer(required=False) # o2o
	paid_price = PaymentSerializer(required=False)

	class Meta:
		model = Service
		fields = '__all__' 

