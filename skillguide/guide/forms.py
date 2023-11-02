from django.forms import ModelForm
from django.forms.widgets import TextInput
from .models import SkillColor


class MyModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(MyModelForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields["color"].widget = TextInput(
                attrs={"type": "color", "title": self.instance.color}
            )
            self.fields["background"].widget = TextInput(
                attrs={"type": "color", "title": self.instance.background}
            )

    class Meta:
        model = SkillColor
        fields = "__all__"
        widgets = {
            "background": TextInput(attrs={"type": "color"}),
            "color": TextInput(attrs={"type": "color"}),
        }