
from django import forms


class GreetingForm(forms.Form):

    name = forms.CharField(
        label="Your name",
        max_length=50,
        min_length=2,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter your name",
            }
        )
    )
