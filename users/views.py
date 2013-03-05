from users.models import User,UserIdentity,UserCategory,UserInscription
from bs4 import BeautifulSoup
import urllib2
from django.http import HttpResponse, HttpResponseRedirect
from dateutil.parser import *

def intraAuth(request):
    sid, uid = request.GET.get("_sid", False), request.GET.get("_uid", False)
    if sid and uid:
        try:
            URL_CHECK = 'http://www.ulb.ac.be/commons/check?_type=normal&_sid=%s&_uid=%s'
            verifier = urllib2.urlopen(URL_CHECK % (sid, uid))
            xml = verifier.read()
        except urllib2.URLError as e:
            raise
            #log reason
        except urllib2.HTTPError as e:
            raise
            #log code and reason
        # response = HttpResponse()
        # response.write(xml)
        # return response
        try:
            values = parseXml(xml)
            user = createUser(**values)
        except:
            raise Exception("problems while parsing xml")
        login(request, user)
        return HttpResponseRedirect('/')

    else:
        from django.http import HttpResponse
        return HttpResponse('Missing params',status=418)

def login(request):
    return HttpResponseRedirect('https://www.ulb.ac.be/commons/intranet?_prt=ulb:facultes:sciences:p402&_ssl=on&_appl=http://'+request.META['HTTP_HOST']+'/user/auth&_prtm=redirect')

def createUser(netid, last_name, first_name, email, xml, birth, identites):
    try:
        user = User.objects.get(netid=netid)
    except:
        user = User.objects.create_user(netid,email)
        user.last_name = last_name
        user.first_name = last_name
        user.birth = birth
        # for identite in identites:
            #for incription in identity
            #for mandat in identity
            #for categorie in identity
    user.xml = xml
    user.save()

    return user

def parseXml(xml):
    soup = BeautifulSoup(xml)
    if soup.intranet.session.user['access'] == 'yes':
        raise Exception("No access !")
    netid = soup.intranet.session.username.text
    last_name = soup.intranet.session.user.nom.text
    first_name = soup.intranet.session.user.prenom.text
    birth = parse(soup.intranet.session.user.datenaissance.text)
    email = (soup.intranet.session.user.email.text).lower()
    #for identity in soup.intranet.session.user('identity'):
        #for incription in identity
        #for mandat in identity
        #for categorie in identity
    return {
        'netid' : netid,
        'last_name': last_name,
        'first_name': first_name,
        'email':email,
        'xml':xml,
        'birth': birth,
        'identites' : []
    }

