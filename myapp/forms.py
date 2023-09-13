from .models import Products_Review, Profile
from django import forms
from django.contrib.auth.models import User

class ProductsReviewForm(forms.ModelForm):
    class Meta:
        model = Products_Review
        fields = ('content', 'products', 'reviewer',)
        widgets = {'products': forms.HiddenInput(), 'reviewer': forms.HiddenInput()}

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image']