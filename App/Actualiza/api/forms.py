from django.forms import ModelForm

from users.models import Usuario

from django.contrib.auth.models import User

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'