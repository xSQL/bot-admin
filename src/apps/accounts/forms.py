from django import forms
from django.forms import widgets
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from django.template import loader
from django.utils.safestring import mark_safe

User = get_user_model()

class PictureWidget(widgets.FileInput):
    template_name = 'widgets/picture.html'


class UserSignupForm(auth_forms.UserCreationForm):
    """..."""
    terms = forms.BooleanField(
        error_messages={
            'required': _('You must accept the terms and conditions')
        },
        label=_('Terms & Conditions')
    )
    class Meta:
        model = User
        fields = ('email',)


class UserModelForm(forms.ModelForm):
    """..."""
    class Meta:
        model = User
        fields = ('first_name', 'middle_name', 'last_name', 'phone', 'city', \
            'photo', 'position'
        )
        widgets = {
            'first_name': widgets.TextInput(attrs={
                'placeholder': _('First name')
            }),
            'middle_name': widgets.TextInput(attrs={
                'placeholder': _('Middle name')
            }),
            'last_name': widgets.TextInput(attrs={
                'placeholder': _('Last name')
            }),
            #'photo': widgets.FileInput()

        }
