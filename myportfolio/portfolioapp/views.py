from django.template import loader
from django.http import HttpResponse
from .models import Test

def test(request):
    mypersons = Test.objects.all().values()
    template = loader.get_template('persons.html')
    context = {
        'mypersons': mypersons,
    }
    return HttpResponse(template.render(context, request))

