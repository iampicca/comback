from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.core.mail import send_mail
# Create your models here.

class UserProfileManager(BaseUserManager):
    """Because our fields are different from django's regular profile"""

    def create_user(self, email, password=None):
        """Creates a new user profile object."""

        if not email:
            raise ValueError('Users must have an email address.')

        email = self.normalize_email(email)
        user = self.model(email=email)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new superuser with given details"""
        user = self.create_user(email, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='email address', error_messages ={"non_field_errors": ["Invalid email address"]}, max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_customer = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email])


class CustomerProfile(User):
    """Represents a 'regular user profile' inside our system."""
    MALE = 'm'
    FEMALE = 'f'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    user = models.OneToOneField(User, null=False, parent_link=True, limit_choices_to = { 'is_customer':True}, on_delete=models.CASCADE, related_name = 'customer_profile')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES,default=MALE)
    verified = models.BooleanField(default=False)
    date_registered = models.DateField(auto_now_add=True)

    def get_full_name(self):
        """Used to get a user's full name."""
        return (self.first_name," ",self.last_name)

    def get_short_name(self):
        """Used to get user's short name."""
        return self.first_name

    def __str__(self):
        return self.email

class StaffProfile(User):
    """Represents a 'staff profile' inside our system."""
    MALE = 'm'
    FEMALE = 'f'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    user = models.OneToOneField(User, null=False, parent_link=True, limit_choices_to = { 'is_staff':True}, on_delete=models.CASCADE, related_name = 'staff_profile')
    business_id = models.ForeignKey('Business', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES,default=MALE)
    verified = models.BooleanField(default=False)
    date_registered = models.DateField(auto_now_add=True)

    def get_full_name(self):
        """Used to get a user's full name."""
        return (self.first_name+" "+self.last_name)

    def get_short_name(self):
        """Used to get user's short name."""
        return self.first_name

    def __str__(self):
        return self.email

class Business(models.Model):
    name = models.CharField(max_length=255)
    linked_to=models.CharField(max_length=255)

    def __str__(self):
        return self.name

class AdminBusProfile(User):
    """Represents a 'business admin profile' inside our system."""
    MALE = 'm'
    FEMALE = 'f'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )

    user = models.OneToOneField(User, null=False, parent_link=True, limit_choices_to = { 'is_admin':True}, on_delete=models.CASCADE, related_name = 'admin_bus_profile')
    business_id = models.ForeignKey('Business', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES,default=MALE)
    verified = models.BooleanField(default=False)
    date_registered = models.DateField(auto_now_add=True)

    def get_full_name(self):
        """Used to get a user's full name."""
        return (self.first_name+" "+self.last_name)

    def get_short_name(self):
        """Used to get user's short name."""
        return self.first_name

    def __str__(self):
        return self.email

class AdminProfile(User):
    """Represents a 'Comback admin profile' inside our system."""
    MALE = 'm'
    FEMALE = 'f'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )

    user = models.OneToOneField(User, null=False, parent_link=True, limit_choices_to = { 'is_superuser':True}, on_delete=models.CASCADE, related_name = 'comback_admin_profile')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES,default=MALE)
    verified = models.BooleanField(default=False)
    date_registered = models.DateField(auto_now_add=True)

    def get_full_name(self):
        """Used to get a user's full name."""
        return (self.first_name+" "+self.last_name)

    def get_short_name(self):
        """Used to get user's short name."""
        return self.first_name

    def __str__(self):
        return self.email

class Feedback(models.Model):
    answer = models.CharField(max_length=255)
    rating = models.IntegerField()
    made_by = models.ForeignKey('CustomerProfile', on_delete = models.CASCADE)
    made_to = models.ForeignKey('Business',on_delete=models.CASCADE)
    date_made = models.DateField(auto_now_add=True)
    anonymous = models.BooleanField(default=False)

    def __str__(self):
        return self.answer

class Complain(models.Model):
    REGULAR = 'customer'
    INHOUSE = 'staff'
    COMPLAIN_CHOICES = (
        (REGULAR, 'Regular'),
        (INHOUSE, 'Inhouse'),
    )
    message = models.TextField()
    made_by = models.ForeignKey('CustomerProfile', on_delete = models.CASCADE)
    made_to = models.ForeignKey('Business',on_delete=models.CASCADE)
    linked_to = models.CharField(max_length=255, null=True)
    type = models.CharField(max_length=2, choices=COMPLAIN_CHOICES,default=REGULAR)
    date_made = models.DateField(auto_now_add=True)
    anonymous = models.BooleanField(default=False)

    def __str__(self):
        return self.message

class Appeal(models.Model):
    complain = models.ForeignKey('Complain', on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return self.complain
