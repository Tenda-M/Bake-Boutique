from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category

from .models import Review

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

################### Review #############
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'maxlength': 100}),
        }
    
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) > 100:
            raise forms.ValidationError('Review cannot exceed 100 characters.')
        return content
