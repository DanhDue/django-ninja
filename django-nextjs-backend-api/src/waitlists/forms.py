from django import forms
from django.utils import timezone

from .models import WaitlistEntry


class WaitlistEntryCreationForm(forms.ModelForm):
    # email = forms.EmailField()
    class Meta:
        model = WaitlistEntry
        fields = ["email"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        today = timezone.now().day
        qs = WaitlistEntry.objects.filter(
            email=email,
            created_at__day=today,
        )
        if qs.count() > 1:
            raise forms.ValidationError("Cannot enter this email again.")
        # if email.endswith("@gmail.com"):
        #     raise forms.ValidationError("Cannot use gmail")
        return email
