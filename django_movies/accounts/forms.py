from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Column, Row, Submit
from django import forms
from datetime import date
from core.models import Genre, Movies
from django.core.exceptions import ValidationError


from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, UserCreationForm
)
from django.db.transaction import atomic
from django.forms import CharField, Form, Textarea
from accounts.models import Profile


class SubmittableForm(Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper
        self.helper.layout = Layout(*self.files, Submit('submit', 'Submit'))

class SubmittableAuthenticationForm(SubmittableForm, AuthenticationForm):
    pass

class SubmittablePasswordchangeForm(SubmittableForm,PasswordChangeForm):
    pass



# class MovieForm(forms.ModelForm):
#     class Meta:
#         model = Movies
#         fields = '__all__'
#
#     title = forms.CharField(validators=[capitalized_validator, new_validator])
#     rating = forms.IntegerField(min_value=1, max_value=10)
#     released = PastMonthField()
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.layout = Layout(
#             'title',
#             Row(Column('genre'), Column('rating'), Column('released')),
#             'director',
#             'description',
#             'country',
#             Submit('submit','Submit'),
#
#         )
