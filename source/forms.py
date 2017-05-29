from django.forms import ModelForm

from source.models import Machine


class MachineForm(ModelForm):
    template_name = 'work/formset.html'

    class Meta:
        model = Machine
        fields = ['id', 'machine_name', 'port', 'state', 'machine_kind', 'machine_type']