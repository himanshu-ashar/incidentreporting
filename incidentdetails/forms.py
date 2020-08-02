from .models import Incident
from django import forms
from .models import SUB_INCIDENT_CHOICES
# from django.contrib.auth.models import User
from django.contrib.admin.widgets import AdminDateWidget, AdminSplitDateTime, AdminTimeWidget
from tempus_dominus.widgets import DateTimePicker
from django.urls import reverse_lazy

class IncidentReportForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = '__all__'
        widgets = {'date_time_of_incident':DateTimePicker(
            options={
                'useCurrent': True,
                'collapse': False,
            },
            attrs={
                'append': 'fa fa-calendar',
                'icon_toggle': True,
            }
        )}
        #widgets = {'myDateTimeField': forms.DateTimeInput(attrs={'id':'datetimepicker12'})}

    # def __init__(self,*args,**kwargs):
    #     super(IncidentReportForm,self).__init__(*args,**kwargs)
    #     #print(reported_by)
    #     self.fields['sub_incident_types']= forms.MultipleChoiceField(choices=SUB_INCIDENT_CHOICES, widget=forms.CheckboxSelectMultiple())
    #     self.fields['date_time_of_incident'] = forms.DateTimeField(widget=DateTimePicker(
    #         options={
    #             'useCurrent': True,
    #             'collapse': False,
    #         },
    #         attrs={
    #             'append': 'fa fa-calendar',
    #             'icon_toggle': True,
    #         }
    #     ))           #forms.DateTimeField(widget=AdminDateWidget())    #(widget=forms.SplitDateTimeWidget())
        #self.fields['date_time_of_incident'] = forms.DateTimeField(widget=forms.DateTimeInput())
        #self.fields['reported_by'].initial = reported_by
