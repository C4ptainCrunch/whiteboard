from users.models import User,UserIdentity,UserCategory,UserInscription
from django.core.management.base import BaseCommand
import datetime
import getpass

def input(field,default=None):
    if not default is None:
        tmp = raw_input('{0} ? [{1}] '.format(field,default))
    else:
        tmp = raw_input('{0} ? '.format(field))
    if not tmp:
        tmp = default
    return tmp

class Command(BaseCommand):
    help = """Adds a new user without using the netid"""
    def handle(self, *args, **options):
        netid = input('User',getpass.getuser())
        try:
            user = User.objects.get(netid=netid)
            print('User exists. Exit')
        except:
            user = User()
            user.netid = netid
            user.email = input('Email',netid+'@ulb.ac.be')
            user.first_name = input('Firstname','John')
            user.last_name = input('Lastname','Doe')
            user.birth = datetime.date(1993,5,24)
            user.set_unusable_password()
            user.xml = ''
            user.save()
