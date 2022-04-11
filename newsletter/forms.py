from django import forms

class NewsLetterForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your email'
            }
        )
    )
    subject = forms.CharField(
        label='Subject',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your subject'
            }
        )
    )
    message = forms.CharField(
        label='Message',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your message'
            }
        )
    )