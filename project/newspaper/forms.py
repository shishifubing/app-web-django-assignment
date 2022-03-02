from django.forms import Form, DateField
from .widgets import BootstrapDatePickerInput, XDSoftDatePickerInput


class DateFormBootstrap(Form):
    publication_date = DateField(
        input_formats=['%d/%m/%Y'],
        widget=BootstrapDatePickerInput())


class DateFormXDSoft(Form):
    date = DateField(
        input_formats=['%d/%m/%Y'],
        widget=XDSoftDatePickerInput()
    )
