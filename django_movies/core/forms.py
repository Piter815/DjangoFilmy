from django import forms
from datetime import date
from core.models import Genre, Movies
from django.core.exceptions import ValidationError


def capitalized_validator(value):
    if value[0].islower():
        raise ValidationError('Value must be capitalized!')


def new_validator(value):
    if value == "Funny":
        raise ValidationError('Its not that funny...')


class PastMonthField(forms.DateField):
    def validate(self, value):
        super().validate(value)
        if value >= date.today():
            raise ValidationError('Only past dates are allowed!')

    def clean(self, value):
        result = super().clean(value)
        return date(year=result.year, month=result.month, day=1)


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = '__all__'

    title = forms.CharField(validators=[capitalized_validator, new_validator])
    rating = forms.IntegerField(min_value=1, max_value=10)
    released = PastMonthField()
