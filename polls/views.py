from django.shortcuts import render, redirect
from django.utils import timezone
from django.http import HttpResponseRedirect
from .forms import MyModelForm
from django.views.generic import TemplateView

class AboutView(TemplateView):
    template_name = "polls/thanks.html"

def add_model(request):

    if request.method == "POST":
        form = MyModelForm(request.POST)
        if form.is_valid():

            # commit=False means the form doesn't save at this time.
            # commit defaults to True which means it normally saves.
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return HttpResponseRedirect('/polls/thanks')
    else:
        form = MyModelForm()

    return render(request, "polls/polls.html", {'form': form})