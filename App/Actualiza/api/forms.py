from django.forms import ModelForm

from users.models import Usuario
from .models import experimento, imagen, video

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

class ExperimentoForm(ModelForm):
    class Meta:
        model = experimento
        fields = '__all__'

class ImagenForm(ModelForm):
    class Meta:
        model = imagen
        fields = '__all__'

class VideoForm(ModelForm):
    class Meta:
        model = video
        fields = '__all__'