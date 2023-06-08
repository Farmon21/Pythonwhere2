from django import forms
from .models import Order, Review, RATE_CHOICES


class OrderForm(forms.Form):
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}),
                              label="Write your address")
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}),
                            label="Write your phone")

    class Meta:
        model = Order
        fields = ['phone', 'address']


class RateForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea'}), label='Leave your review here')
    rate = forms.ChoiceField(choices=RATE_CHOICES, required=True, label='Rate product from 1 to 5')

    class Meta:
        model = Review
        fields = ('text', 'rate')
