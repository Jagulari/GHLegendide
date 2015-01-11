from django import forms
from .models import MyModel

from django.core.exceptions import ValidationError
from lolPy import RiotApiClient
key = "b607eef2-c0ca-403b-b7af-6a1343574766"
client = RiotApiClient.RiotApiClient(key, "euw")

class MyModelForm(forms.ModelForm):

    class Meta:

        model = MyModel
        fields = ('title', )

    def clean_title(self):
        title = self.cleaned_data['title']
        try:
            name = client.search(title).name
        except:
            raise ValidationError("Sellist kasutajat ei ole olemas.")
        if (title != name):
            raise ValidationError("Kontrolli suuri ja väikeseid tähti nimes.")

        return title
