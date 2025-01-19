from django.http import HttpResponse
from django.template import loader
from configuration.models import Institute
from configuration.utils import get_database_connection


def members(request):
  template = loader.get_template('myfirst.html')

  connection = get_database_connection('preetam.com')
  if connection:
    print("Connection is done")
  else:
    print("Connection failed")
  connection.cursor().execute("SELECT * FROM club.member")
  return HttpResponse(template.render())