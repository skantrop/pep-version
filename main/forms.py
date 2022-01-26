from datetime import datetime

from django import forms

from .models import Food


class RecipeForm(forms.ModelForm):
    created = forms.DateTimeField(initial=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), required=False)

    class Meta:
        model = Food
        # exclude = ('user', )
        fields = '__all__'






