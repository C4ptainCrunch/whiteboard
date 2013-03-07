from users.models import User,UserIdentity,UserCategory,UserInscription
from django.core.management.base import BaseCommand
import datetime

class Command(BaseCommand):
    help = """Adds a new user without using the netid"""
    def handle(self, *args, **options):
        name = raw_input('User ? ')
        try:
            user = User.objects.get(netid=name)
            print('User exists. Exit')
        except:
            user = User()
            user.netid = name
            user.email = raw_input('Email ? ')
            user.last_name = raw_input('Lastname ? ')
            user.first_name = raw_input('Firstname ? ')
            user.birth = datetime.date(1993,5,24)
            user.set_unusable_password()
            user.xml = ''
            user.save()
