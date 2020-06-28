from django.db import models
from django.utils import timezone
# Create your models here.

class Building(models.Model):
    objects = models.Manager()
    number = models.IntegerField()

    def __str__(self):
        return str(self.number) + "동"

class Floor(models.Model):
    objects = models.Manager()
    number = models.IntegerField()

    def __str__(self):
        return str(self.number) + "층"

class Room(models.Model):
    objects = models.Manager()
    number = models.IntegerField()

    def __str__(self):
        return str(self.number) + "호"

class Apartment(models.Model):
    objects = models.Manager()
    building = models.ForeignKey(Building, on_delete = models.CASCADE, blank=True)
    floor = models.ForeignKey(Floor, on_delete = models.CASCADE, blank=True)
    room = models.ForeignKey(Room, on_delete = models.CASCADE, blank=True)

    def __str__(self):
        return str(self.building.number)+"동 " + str(self.floor.number) + "0" + str(self.room.number)+"호"

class Resident(models.Model):
    objects = models.Manager()
    idx = models.BigAutoField(primary_key=True)
    uid = models.TextField(blank=False, null=False)
    pw = models.TextField(blank=False, null=False)
    name = models.CharField(max_length=10, blank=True, null=True)
    birth_year = models.IntegerField()
    room = models.ForeignKey(Apartment, on_delete = models.CASCADE, blank=True)

    def __str__(self):
        return self.name

class Visitor(models.Model):
    objects = models.Manager()
    idx = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True)
    date = models.DateTimeField(default=timezone.now)
    time = models.DurationField()
    visited = models.BooleanField(default=False)
    room = models.ForeignKey(Apartment, on_delete = models.CASCADE, blank=True)

    def __str__(self):
        return self.name

class EntranceLog(models.Model):
    objects = models.Manager()
    idx = models.BigAutoField(primary_key=True)
    date = models.DateTimeField(default=timezone.now)
    visitor_idx = models.ForeignKey(Visitor, models.DO_NOTHING, db_column='visitor_idx')

class Device(models.Model):
    MOBILE = 'mb'
    TABLET = 'tl'
    PC = 'pc'
    TYPE_CHOICES = [
        (MOBILE, '모바일'),
        (TABLET, '테블릿'),
        (PC, 'pc')
    ]
    objects = models.Manager()
    idx = models.BigAutoField(primary_key=True)
    device_type = models.CharField(
        max_length=10, 
        choices=TYPE_CHOICES,
        default=MOBILE
    )
    os = models.CharField(max_length=10, blank=True)
    version = models.CharField(max_length=10, blank=True)
    resident = models.ForeignKey(
		Resident, 
        on_delete = models.DO_NOTHING,
		related_name='resident',
		blank=True,
        null=True
	)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class QrAppApartment(models.Model):
    uid = models.TextField()
    building = models.ForeignKey('QrAppBuilding', models.DO_NOTHING)
    floor = models.ForeignKey('QrAppFloor', models.DO_NOTHING, blank=True, null=True)
    room = models.ForeignKey('QrAppRoom', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'qr_app_apartment'


class QrAppBuilding(models.Model):
    number = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'qr_app_building'


class QrAppDevice(models.Model):
    idx = models.BigAutoField(primary_key=True)
    uid = models.TextField()
    device_type = models.CharField(max_length=10, blank=True, null=True)
    os = models.CharField(max_length=100)
    version = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qr_app_device'


class QrAppEntrancelog(models.Model):
    idx = models.BigAutoField(primary_key=True)
    date = models.DateTimeField()
    visitor_idx = models.ForeignKey('QrAppVisitor', models.DO_NOTHING, db_column='visitor_idx')

    class Meta:
        managed = False
        db_table = 'qr_app_entrancelog'


class QrAppFloor(models.Model):
    number = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'qr_app_floor'


class QrAppResident(models.Model):
    idx = models.BigAutoField(primary_key=True)
    uid = models.TextField()
    pw = models.TextField()
    name = models.CharField(max_length=10)
    birth_year = models.IntegerField()
    apartment = models.ForeignKey(QrAppApartment, models.DO_NOTHING, blank=True, null=True)
    salt = models.CharField(max_length=100, blank=True, null=True)
    hash = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qr_app_resident'


class QrAppRoom(models.Model):
    number = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'qr_app_room'


class QrAppVisitRequestList(models.Model):
    idx = models.BigAutoField(primary_key=True)
    resident_uid = models.TextField(blank=True, null=True)
    visitor_uid = models.TextField(blank=True, null=True)
    permit = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qr_app_visit_request_list'


class QrAppVisitor(models.Model):
    idx = models.BigAutoField(primary_key=True)
    uid = models.TextField()
    pw = models.TextField()
    name = models.CharField(max_length=10)
    birth_year = models.IntegerField()
    apartment = models.ForeignKey(QrAppApartment, models.DO_NOTHING, blank=True, null=True)
    salt = models.CharField(max_length=45, blank=True, null=True)
    hash = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qr_app_visitor'


class QrAppVisitorVisitrequest(models.Model):
    idx = models.BigAutoField(primary_key=True)
    uid = models.TextField()
    name = models.TextField(blank=True, null=True)
    building_id = models.IntegerField(blank=True, null=True)
    floor = models.IntegerField(blank=True, null=True)
    room_id = models.IntegerField(blank=True, null=True)
    visit_purpose = models.CharField(max_length=100, blank=True, null=True)
    permit = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'qr_app_visitor_visitRequest'