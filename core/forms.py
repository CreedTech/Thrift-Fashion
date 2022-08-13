from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from .models import Contact, Feedback
from django.core.mail import send_mail
from django.conf import settings


PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'PayStack')
)


class ContactForm(forms.ModelForm):
    fullName = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={
            "placeholder": "Your name",
            "class": "form-control",
        }
    ))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            "placeholder": "Your email",
            "class": "form-control",
        }
    ))
    subject = forms.CharField(max_length=100,
                              widget=forms.TextInput(
                                  attrs={
                                      "placeholder": "Subject",
                                      "class": "form-control",
                                  }
                              ))
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Message",
                "class": "form-control",
                "row": 8,
                "column": 20
            }
        )
    )

    class Meta:
        model = Contact
        fields = '__all__'

    def get_info(self):

        # Cleaned data
        cl_data = super().clean()

        name = cl_data.get('name').strip()
        from_email = cl_data.get('email')
        subject = cl_data.get('subject')

        msg = f'{name} with email {from_email} said:'
        msg += f'\n"{subject}"\n\n'
        msg += cl_data.get('message')

        return subject, msg

    def send(self):

        subject, msg = self.get_info()

        send_mail(
            subject=subject,
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.RECIPIENT_ADDRESS]
        )


class FeedbackForm(forms.ModelForm):
    fullName = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={
            "placeholder": "Your name",
            "class": "form-control",
        }
    ))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            "placeholder": "Your email",
            "class": "form-control",
        }
    ))
    subject = forms.CharField(max_length=100,
                              widget=forms.TextInput(
                                  attrs={
                                      "placeholder": "Subject",
                                      "class": "form-control",
                                  }
                              ))
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Message",
                "class": "form-control",
                "row": 8,
                "column": 20
            }
        )
    )

    class Meta:
        model = Feedback
        fields = '__all__'


class CheckoutForm(forms.Form):
    shipping_address = forms.CharField(required=False)
    shipping_address2 = forms.CharField(required=False)
    shipping_country = CountryField(blank_label='(select country)').formfield(
        required=False,
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100',
        }))
    shipping_zip = forms.CharField(required=False)

    billing_address = forms.CharField(required=False)
    billing_address2 = forms.CharField(required=False)
    billing_country = CountryField(blank_label='(select country)').formfield(
        required=False,
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100',
        }))
    billing_zip = forms.CharField()

    same_billing_address = forms.BooleanField(required=False)
    set_default_shipping = forms.BooleanField(required=False)
    use_default_shipping = forms.BooleanField(required=False)
    set_default_billing = forms.BooleanField(required=False)
    use_default_billing = forms.BooleanField(required=False)

    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_CHOICES)


class CouponForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Promo code',
        'aria-label': 'Recipient\'s username',
        'aria-describedby': 'basic-addon2'
    }))


class RefundForm(forms.Form):
    ref_code = forms.CharField()
    message = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 4
    }))
    email = forms.EmailField()


class PaymentForm(forms.Form):
    stripeToken = forms.CharField(required=False)
    save = forms.BooleanField(required=False)
    use_default = forms.BooleanField(required=False)
