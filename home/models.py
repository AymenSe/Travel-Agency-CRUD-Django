# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from crum import get_current_user # this for current user







class CancelService(models.Model):
    id_service = models.ForeignKey('Service', models.DO_NOTHING, db_column='id_service')
    id_user = models.ForeignKey(User, models.DO_NOTHING, db_column='id_user')
    penalty = models.PositiveIntegerField(blank=True, null=True)
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.
    is_active = models.BooleanField(default=True)

    class Meta:
        managed = True
        db_table = 'cancel_service'
        unique_together = (('id', 'id_service', 'id_user'),)


class Refund(models.Model):
    amount = models.PositiveIntegerField(blank=True, null=True)
    cancel_service_id = models.OneToOneField("CancelService", models.DO_NOTHING, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        managed = True
        db_table = 'refund'



class Client(models.Model):
    idclient = models.AutoField(db_column='idClient', primary_key=True)  # Field name made lowercase.
    name_ar = models.CharField(db_column='name_ar', max_length=90)  # Field name made lowercase.
    name_fr = models.CharField(db_column='name_fr', max_length=90)  # Field name made lowercase.
    passport_id = models.CharField(db_column='Passeport_id', unique=True, max_length=45, blank=True, null=True)  # Field name made lowercase.
    telephone = models.CharField(db_column='TelephoneNb', max_length=45, default = None)  # Field name made lowercase.
    e_mail_facebook = models.CharField(db_column='E-mail/Fabebook', unique=True, max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    is_active = models.BooleanField(default=True)

    class Meta:
        managed = True
        db_table = 'client'
    
    def __str__(self):
        return f'{self.name_fr}'


# it's Oooook
class Insurance(models.Model):
    number = models.CharField(max_length=45, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        managed = True
        db_table = 'insurance'


# it's Oooook 
class Omra(models.Model):

    food = models.BooleanField(default=None, blank=True, null=True)  # +++++++++++++.
    duration = models.PositiveIntegerField(blank=True, null=True)
    start_date = models.DateField(auto_now_add=True, blank=True, null=True)
    hotel_name = models.CharField(max_length=90, blank=True, null=True)
#    area = models.CharField(max_length=45, blank=True, null=True)
#    distance_from_haram = models.PositiveIntegerField(blank=True, null=True)
    room_size = models.PositiveIntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        managed = True
        db_table = 'omra'

# it's Oooook
class OrganizedJourney(models.Model):
    # id = models.PositiveIntegerField(primary_key=True)
    country = CountryField(blank_label='(إختر الدولة)')  # ++++++++++++++++++
    duration = models.PositiveIntegerField(blank=True, null=True)
    start_date = models.DateField(auto_now_add=True, blank=True, null=True)
    room_type = models.PositiveIntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        managed = True
        db_table = 'organized_journey'

# it's Ooook
class Other(models.Model):
    # id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        managed = True
        db_table = 'other'


class Payment(models.Model):
#    id_payment = models.AutoField(db_column='Id_Payment', primary_key=True)  # Field name made lowercase.
    sum_payment = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
#    id_service = models.ForeignKey('Service', models.DO_NOTHING, db_column='id_service')
#    user_iduser = models.ForeignKey(User, models.DO_NOTHING, default=get_current_user, db_column='User_idUser')  # Field name made lowercase.
    is_active = models.BooleanField(default=True)

    class Meta:
        managed = True
        db_table = 'payment'
#        unique_together = (('id_payment', 'id_service', 'user_iduser'),)


class Service(models.Model):

    VOUCHER = 'voucher'
    NORMAL = 'normal' 
    CHOICES = [
        (VOUCHER, 'فاتورة'),
        (NORMAL, 'عادي'),
    ]

    user_iduser = models.ForeignKey(User, models.DO_NOTHING, default=get_current_user, db_column='User_idUser')  # Field name made lowercase.
    request_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
#    country = CountryField(blank_label='(إختر الدولة)', blank=True, null=True)  # ++++++++++++++++++
    insurance = models.OneToOneField(Insurance, models.DO_NOTHING, blank=True, null=True)
    omra = models.OneToOneField(Omra, models.DO_NOTHING, blank=True, null=True)
    organized_trip = models.OneToOneField('OrganizedJourney', models.DO_NOTHING, blank=True, null=True)
    other = models.OneToOneField(Other, models.DO_NOTHING, blank=True, null=True)
    temp_ticket = models.BooleanField(blank=True, null=True)
#    ticket = models.OneToOneField('Ticket', models.DO_NOTHING, blank=True, null=True)
    temp_hotel_reservation = models.CharField(max_length=45, choices=CHOICES, default=NORMAL)
    travel_hotel_reservation = models.OneToOneField('TravelHotelReservation', models.DO_NOTHING, blank=True, null=True)
    visa = models.OneToOneField('Visa', models.CASCADE, blank=True, null=True)
    visa_rdv = CountryField(blank_label='(إختر الدولة)', blank=True, null=True)
    visa_request_form = models.BooleanField(blank=True, null=True)
    client = models.ManyToManyField("Client")
    main_price = models.FloatField(blank=True, null=True)
    final_price = models.FloatField(blank=True, null=True)
    paid_price = models.ForeignKey('Payment', models.DO_NOTHING)
    is_active = models.BooleanField(default=True)


    class Meta:
        managed = True
        db_table = 'service'
        unique_together = (('id', 'user_iduser'),)

    def __str__(self):
        return f'service to client {self.request_date}'




# class Ticket(models.Model):
#     CHANGETK = 'CHTK' # change ticket
#     ADDTK = 'ADTK' # add ticket
#     TICKET_CHOICES = [
#         (ADDTK, 'حجز تذكـرة'),
#         (CHANGETK, 'تغيير تذكـرة'),
#     ]
#     type_of = models.CharField(max_length=45, choices=TICKET_CHOICES, default=ADDTK)  # ++++++++ 
#     number = models.PositiveIntegerField(unique=True) # رمز التذكرة 
#     is_active = models.BooleanField(default=True)

#     class Meta:
#         managed = True
#         db_table = 'ticket'


# it's Ooook
class TravelHotelReservation(models.Model):
#   id = models.PositiveIntegerField(primary_key=True)
    country = CountryField(blank_label='(إختر الدولة)')  # ++++++++++++++++++
    City = models.CharField(max_length=45) # ++++++++++++++++++
    reservation_number = models.PositiveIntegerField(unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        managed = True
        db_table = 'travel_hotel_reservation'




class Visa(models.Model):
#   id = models.PositiveIntegerField(primary_key=True)
    duration = models.PositiveIntegerField(blank=True, null=True)
    single_visit = models.BooleanField(default=True, blank=True, null=True) 
    country = CountryField(blank_label='(إختر الدولة)', default='PS') # ++++++++++++++++++
    is_active = models.BooleanField(default=True)

    class Meta:
        managed = True
        db_table = 'visa'



class Inquiry(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    phone = models.CharField(max_length=45)
    facebook = models.CharField(max_length=45, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    Service = models.CharField(max_length=45)
    inquirycol = models.CharField(max_length=50)
    answered = models.BooleanField(default=False, blank=True, null=True)
    comments = models.TextField(blank=True, null=True) 
    is_active = models.BooleanField(default=True)


    class Meta:
        managed = True
        db_table = 'inquiry'

    def __str__(self):
        return f'inquiry of client {self.first_name} {self.last_name}'

# Add some tables! 

class Country(models.Model):
    name = CountryField(blank_label='(إختر الدولة)')
    visa_rdv = models.BooleanField(default=False, blank=True, null=True)
    visa = models.BooleanField(default=False, blank=True, null=True)
    organized_trip = models.BooleanField(default=False, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        managed = True
        db_table = 'Country'

    def __str__(self):
        return f'Country: {self.name}'

class Region(models.Model):
    name = models.CharField(max_length=45)
    country = models.ForeignKey(Country, models.DO_NOTHING)
    visa_rdv = models.BooleanField(default=False, blank=True, null=True)
    visa = models.BooleanField(default=False, blank=True, null=True)
    organized_trip = models.BooleanField(default=False, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        managed = True
        db_table = 'Region'

    def __str__(self):
        return f'Region: {self.name}'  

class City(models.Model):
    name = models.CharField(max_length=45)
    region = models.ForeignKey(Region, models.DO_NOTHING)
    visa_rdv = models.BooleanField(default=False, blank=True, null=True)
    visa = models.BooleanField(default=False, blank=True, null=True)
    organized_trip = models.BooleanField(default=False, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        managed = True
        db_table = 'City'

    def __str__(self):
        return f'City: {self.name}'
    