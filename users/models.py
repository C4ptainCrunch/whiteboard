from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import UserManager

class User(AbstractBaseUser):
    netid = models.CharField(max_length=20,unique=True)
    comment = models.CharField(null=True,max_length=1000)
    xml = models.CharField(max_length=10000)
    birth = models.DateField()
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    email = models.EmailField()

    USERNAME_FIELD = 'netid'
    REQUIRED_FIELDS = ('last_name','first_name','email')
    objects = UserManager()

    def to_dict(self):
        """Return self as a dict."""
        return {
            'netid':self.netid,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'full_name': self.first_name+' '+self.last_name,
            'birth': str(self.birth),
        }

class UserIdentity(models.Model):
    matricule = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        unique_together = ("matricule", "user")

class UserCategory(models.Model):
    slug = models.CharField(max_length=100)
    identity = models.ForeignKey(UserIdentity)

    class Meta:
        unique_together = ("slug", "identity")

class UserInscription(models.Model):
    slug = models.CharField(max_length=100)
    identity = models.ForeignKey(UserIdentity)

    class Meta:
        unique_together = ("slug", "identity")
