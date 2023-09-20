from django.forms import ModelForm
from main.models import Item, Category

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        exclude = ['id']

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        exclude = ['id']