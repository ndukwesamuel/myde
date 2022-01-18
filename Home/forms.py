from django.forms import ModelForm
from Home.models import TodoData



class TodoForm(ModelForm):
    class Meta:
        model = TodoData
        fields  = '__all__'
        # field = ['name', 'due_date']