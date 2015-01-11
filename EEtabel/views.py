from django.shortcuts import render
from django_tables2   import RequestConfig
from .models import Summoners
from .tables import PersonTable

# TÖÖTAB!!
#def EEtabel(request):
#    output = list(Summoners.objects.all())
#    return render_to_response('EEtabel/eetabel.html', {'output': output})

#def EEtabel(request):
#    queryset = Summoners.objects.all()
#    table = SimpleTable(queryset)
#    return render_to_response('EEtabel/eetabel.html', {"table": table},
#                              context_instance=RequestContext(request))

def people(request):
    table = PersonTable(Summoners.objects.all())
    table.order_by = "-TotalLP"
    #RequestConfig(request).configure(table)
    return render(request, 'EEtabel/eetabel.html', {'table': table})
