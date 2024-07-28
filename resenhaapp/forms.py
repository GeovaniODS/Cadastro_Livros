from django.forms import ModelForm
from .models import leituras

class leiturasform(ModelForm):
    class Meta:
        model = leituras
        fields = '__all__'