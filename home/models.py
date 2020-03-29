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
# from phone_field import PhoneField




# class CancelPayment(models.Model):
#     date = models.DateField(db_column='Date')  # Field name made lowercase.
#     id_user = models.ForeignKey(User, models.DO_NOTHING, db_column='id_user')
#     comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.
#     id_payment = models.ForeignKey('Payment', models.DO_NOTHING, db_column='id_payment')

#     class Meta:
#         managed = True
#         db_table = 'cancel_payment'
#         unique_together = (('id', 'id_user', 'id_payment'),)




class CancelService(models.Model):
    id_service = models.ForeignKey('Service', models.DO_NOTHING, db_column='id_service')
    id_user = models.ForeignKey(User, models.DO_NOTHING, db_column='id_user')
    penalty = models.PositiveIntegerField(blank=True, null=True)
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'cancel_service'
        unique_together = (('id', 'id_service', 'id_user'),)


class Refund(models.Model):
    amount = models.PositiveIntegerField(blank=True, null=True)
    cancel_service_id = models.OneToOneField("CancelService", models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'refund'



class Client(models.Model):
    idclient = models.AutoField(db_column='idClient', primary_key=True)  # Field name made lowercase.
    clienfirstname_ar = models.CharField(db_column='ClienFirstname_Ar', max_length=45)  # Field name made lowercase.
    lastname_ar = models.CharField(db_column='LastName_Ar', max_length=45)  # Field name made lowercase.
    firstname_fr = models.CharField(db_column='Firstname_Fr', max_length=45)  # Field name made lowercase.
    lastname_fr = models.CharField(db_column='LastName_Fr', max_length=45)  # Field name made lowercase.
    passeport_id = models.CharField(db_column='Passeport_id', unique=True, max_length=45, blank=True, null=True)  # Field name made lowercase.
    telephonenb = models.PositiveIntegerField(db_column='TelephoneNb')  # Field name made lowercase.
    e_mail_fabebook = models.CharField(db_column='E-mail/Fabebook', unique=True, max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_place_of_birth = models.CharField(db_column='Date/Place_of_Birth', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    user_iduser = models.ForeignKey(User, models.DO_NOTHING, db_column='User_idUser')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'client'
        unique_together = (('idclient', 'user_iduser'),)
    
    def __str__(self):
        return f'{self.firstname_fr} {self.lastname_fr}'


# it's Oooook
class Insurance(models.Model):
    # id = models.PositiveIntegerField(primary_key=True)
    number = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'insurance'


# it's Oooook 
class Omra(models.Model):
    WITHFOOD = 'WF' # choice with food
    WITHOUTFOOD = 'WIF' # choice without food
    FOOD_CHOICES = [
        (WITHFOOD, 'برنامج عمرة مع الأكل'),
        (WITHOUTFOOD, 'برنامج عمرة بدون الأكل'),
    ]

    # id = models.PositiveIntegerField(primary_key=True)
    food_field = models.CharField(max_length=45, choices=FOOD_CHOICES, default=WITHFOOD, blank=True, null=True)  # +++++++++++++.
    duration = models.PositiveIntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    hotel_name = models.CharField(max_length=45, blank=True, null=True)
    area = models.CharField(max_length=45, blank=True, null=True)
    distance_from_haram = models.PositiveIntegerField(blank=True, null=True)
    room_size = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'omra'

# it's Oooook
class OrganizedJourney(models.Model):
    # id = models.PositiveIntegerField(primary_key=True)
    country = CountryField(blank_label='(إختر الدولة)')  # ++++++++++++++++++
    duration = models.PositiveIntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    room_type = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'organized_journey'

# it's Ooook
class Other(models.Model):
    # id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    details = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'other'


class Payment(models.Model):
    id_payment = models.AutoField(db_column='Id_Payment', primary_key=True)  # Field name made lowercase.
    sum_payment = models.PositiveIntegerField()
    date = models.DateField()
    id_service = models.ForeignKey('Service', models.DO_NOTHING, db_column='id_service')
    user_iduser = models.ForeignKey(User, models.DO_NOTHING, db_column='User_idUser')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'payment'
        unique_together = (('id_payment', 'id_service', 'user_iduser'),)


class Service(models.Model):
    user_iduser = models.ForeignKey(User, models.DO_NOTHING, db_column='User_idUser')  # Field name made lowercase.
    request_date = models.DateTimeField(blank=True, null=True)
    country = CountryField(blank_label='(إختر الدولة)')  # ++++++++++++++++++
    insurance = models.OneToOneField(Insurance, models.DO_NOTHING, blank=True, null=True)
    omra = models.OneToOneField(Omra, models.DO_NOTHING, blank=True, null=True)
    organized_journey = models.OneToOneField(OrganizedJourney, models.DO_NOTHING)
    other = models.OneToOneField(Other, models.DO_NOTHING, blank=True, null=True)
    temp_hotel_reservation = models.OneToOneField('TempHotelReservation', models.DO_NOTHING, blank=True, null=True)
    temp_ticket = models.BooleanField(blank=True, null=True)
    ticket = models.OneToOneField('Ticket', models.DO_NOTHING, blank=True, null=True)
    travel_hotel_reservation = models.OneToOneField('TravelHotelReservation', models.DO_NOTHING, blank=True, null=True)
    visa = models.OneToOneField('Visa', models.DO_NOTHING, blank=True, null=True)
    visa_rdv = models.BooleanField(blank=True, null=True)
    visa_request_form = models.BooleanField(blank=True, null=True)
    client = models.ManyToManyField("Client")


    class Meta:
        managed = True
        db_table = 'service'
        unique_together = (('id', 'user_iduser'),)

    def __str__(self):
        return f'service to client {self.country}'


# class ServiceClient(models.Model):
#     id_service = models.OneToOneField(Service, models.DO_NOTHING, db_column='id_service', primary_key=True)
#     id_client = models.ForeignKey(Client, models.DO_NOTHING, db_column='id_client')
#     id_user = models.ForeignKey(User, models.DO_NOTHING, db_column='id_user')
#     # id = models.CharField(max_length=45)

#     class Meta:
#         managed = True
#         db_table = 'service_client'
#         unique_together = (('id_service', 'id_user', 'id_client'),) # , 'id'


class TempHotelReservation(models.Model):
#   id = models.PositiveIntegerField(primary_key=True)
    type_of = models.CharField(max_length=7)

    class Meta:
        managed = True
        db_table = 'temp_hotel_reservation'


# class TempTicket(models.Model):
# #   id = models.PositiveIntegerField(primary_key=True)
# models.BooleanField(_(""))

#     class Meta:
#         managed = True
#         db_table = 'temp_ticket'



class Ticket(models.Model):
    CHANGETK = 'CHTK' # change ticket
    ADDTK = 'ADTK' # add ticket
    TICKET_CHOICES = [
        (ADDTK, 'حجز تذكـرة'),
        (CHANGETK, 'تغيير تذكـرة'),
    ]
    type_of = models.CharField(max_length=45, choices=TICKET_CHOICES, default=ADDTK)  # ++++++++ 
    number = models.PositiveIntegerField(unique=True) # رمز التذكرة 

    class Meta:
        managed = True
        db_table = 'ticket'


# it's Ooook
class TravelHotelReservation(models.Model):
#   id = models.PositiveIntegerField(primary_key=True)
    country = CountryField(blank_label='(إختر الدولة)')  # ++++++++++++++++++
    City = models.CharField(max_length=45) # ++++++++++++++++++
    reservation_number = models.PositiveIntegerField(unique=True)

    class Meta:
        managed = True
        db_table = 'travel_hotel_reservation'


#class User(models.Model):
#    iduser = models.PositiveIntegerField(db_column='idUser', primary_key=True)  # Field name made lowercase.
#    username = models.CharField(max_length=45)
#    password = models.CharField(max_length=45)
#
#    class Meta:
#        managed = True
#        db_table = User


class Visa(models.Model):
#   id = models.PositiveIntegerField(primary_key=True)
    duration = models.PositiveIntegerField(blank=True, null=True)
    single_voyage_field = models.PositiveIntegerField(db_column='single_voyage?', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    country = CountryField(blank_label='(إختر الدولة)', default='PS') # ++++++++++++++++++

    class Meta:
        managed = True
        db_table = 'visa'


# class VisaRdv(models.Model):
# #   id = models.PositiveIntegerField(primary_key=True)

#     class Meta:
#         managed = True
#         db_table = 'visa_rdv'


# class VisaRequestForm(models.Model):
# #   id = models.PositiveIntegerField(primary_key=True)

#     class Meta:
#         managed = True
#         db_table = 'visa_request_form'


class Inquiry(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    phone = models.CharField(max_length=45)
    facebook = models.CharField(max_length=45, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    Service = models.CharField(max_length=45)
    inquirycol = models.CharField(max_length=50)
    answered = models.BooleanField()
    comments = models.TextField(blank=True, null=True) 


    class Meta:
        managed = True
        db_table = 'inquiry'

    def __str__(self):
        return f'inquiry of client {self.first_name} {self.last_name}'
