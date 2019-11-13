from django.db import models

class InboxModel(models.Model):
    senders = models.IntegerField(primary_key=True)
    messages = models.TextField()
class OrganizationModel(models.Model):
    org_id = models.IntegerField(primary_key=True)
    org_name = models.CharField(max_length=30)
    org_address = models.TextField()
    org_country = models.CharField(max_length=30)
    org_state = models.CharField(max_length=20)
    org_city = models.CharField(max_length=20)
    org_email = models.EmailField(max_length=50)
    org_password = models.CharField(max_length=10)
    org_contact = models.IntegerField(10)

class DonorModel(models.Model):
    donor_name = models.CharField(max_length=30)
    donor_userid = models.CharField(max_length=30)
    donor_password = models.CharField(max_length=30)
    donor_gender = models.CharField(max_length=8)
    donor_email = models.EmailField(max_length=50)
    donor_contact = models.IntegerField(10)
    donor_bloodgroup = models.CharField(max_length=30)
    donor_state = models.CharField(max_length=20)
    donor_city = models.CharField(max_length=20)
    donor_age = models.IntegerField(2)
    donor_weight = models.IntegerField(2)
    donor_donatedate = models.DateField()
