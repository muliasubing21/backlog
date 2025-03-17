from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    # Definisikan semua field secara eksplisit dengan required=True
    username = forms.CharField(
        max_length=150, 
        required=True, 
        help_text="Masukkan username Anda.", 
        error_messages={'required': 'Username harus diisi!'},
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        required=True, 
        help_text="Masukkan email Anda.", 
        error_messages={'required': 'Email harus diisi!'},
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True,
        help_text="Masukkan kata sandi Anda.",
        error_messages={'required': 'Password harus diisi!'},
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True,
        help_text="Masukkan kata sandi lagi untuk konfirmasi.",
        error_messages={'required': 'Konfirmasi password harus diisi!'}
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')