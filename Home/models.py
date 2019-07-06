from django.db import models


class Agencies(models.Model):
    agency_id = models.AutoField(db_column='Agency_id', primary_key=True)
    name = models.CharField(db_column='Name', max_length=45)
    password = models.CharField(db_column='Password', max_length=255)
    address = models.CharField(db_column='Address', max_length=255)
    e_mail = models.CharField(db_column='E-Mail', max_length=45)
    commercial_id = models.CharField(max_length=45, blank=True, null=True)
    bio = models.TextField(db_column='Bio', blank=True, null=True)
    promo_code = models.CharField(db_column='Promo-Code', max_length=45, blank=True, null=True)
    photo_url = models.CharField(db_column='Photo_URL', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agencies'


class Follows(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING, db_column='User_id')
    agency = models.ForeignKey(Agencies, models.DO_NOTHING, db_column='Agency_id')

    class Meta:
        managed = False
        db_table = 'follows'
        unique_together = (('user', 'agency'),)


class Activity(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING, db_column='User_id')
    trip = models.ForeignKey('Trips', models.DO_NOTHING, db_column='Trip_id')
    type = models.IntegerField(db_column='Type')

    class Meta:
        managed = False
        db_table = 'activity'
        unique_together = (('user', 'trip'),)


class Phones(models.Model):
    agency = models.ForeignKey('Agencies', models.DO_NOTHING, db_column='Agency_id')
    phone = models.CharField(db_column='Phone', max_length=13)

    class Meta:
        managed = False
        db_table = 'phones'


class Response(models.Model):
    vote = models.ForeignKey('Vote', models.DO_NOTHING, db_column='Vote_id')
    user = models.ForeignKey('Users', models.DO_NOTHING, db_column='User_id')
    response_time = models.DateTimeField(db_column='Response_time')
    interested = models.IntegerField(db_column='Interested')

    class Meta:
        managed = False
        db_table = 'response'
        unique_together = (('vote', 'user'),)


class TripPhotos(models.Model):
    trip = models.ForeignKey('Trips', models.DO_NOTHING, db_column='Trip_id')
    url = models.CharField(db_column='URL', max_length=255)

    class Meta:
        managed = False
        db_table = 'trip_photos'
        unique_together = (('trip', 'url'),)


class Trips(models.Model):
    trip_id = models.AutoField(db_column='Trip_id', primary_key=True)
    agency = models.ForeignKey(Agencies, models.DO_NOTHING, db_column='Agency_id')
    name = models.CharField(db_column='Name', max_length=45)
    from_location = models.CharField(db_column='From_Location', max_length=45)
    to_location = models.CharField(db_column='To_Location', max_length=45)
    date_from = models.DateTimeField(db_column='Date_From')
    date_to = models.DateTimeField(db_column='Date_to')
    deadline = models.DateTimeField(db_column='Deadline')
    meals = models.CharField(db_column='Meals', max_length=45)
    price = models.FloatField(db_column='Price')
    description = models.TextField(db_column='Description')
    views = models.IntegerField(db_column='Views', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trips'


class Users(models.Model):
    user_id = models.AutoField(db_column='User_id', primary_key=True)
    name = models.CharField(db_column='Name', max_length=45)
    password = models.CharField(db_column='Password', max_length=255)
    e_mail = models.CharField(db_column='E-Mail', max_length=45)
    phone = models.CharField(db_column='Phone', max_length=13, blank=True, null=True)
    city = models.CharField(db_column='City', max_length=45, blank=True, null=True)
    photo_url = models.CharField(db_column='Photo_URL', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class Vote(models.Model):
    vote_id = models.AutoField(db_column='Vote_id', primary_key=True)
    agency = models.ForeignKey(Agencies, models.DO_NOTHING, db_column='Agency_id')
    name = models.CharField(db_column='Name', max_length=45)
    description = models.TextField(db_column='Description')
    photo_url = models.CharField(db_column='Photo_URL', max_length=255)

    class Meta:
        managed = False
        db_table = 'vote'
