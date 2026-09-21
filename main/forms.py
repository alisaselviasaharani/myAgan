from django.forms import ModelForm, TextInput, URLInput, Select
from main.models import Collection



class CollectionForm(ModelForm):
    class Meta:
        model = Collection

        fields = [
            "judul",
            "jenis",
            "label",
            "link",
        ]

        labels = {
            "judul": "Judul Lagu",
            "jenis": "Jenisnya apa",
            "label": "Label",
            "link": "Link video",
        }

        widgets = {
            "judul": TextInput(
                attrs={
                    "placeholder": "Judulnya apa",
                    "maxlength": 255,
                }
            ),

            "jenis": Select(
                attrs={
                    "class": "form-control",
                }
            ),

            "label": TextInput(
                attrs={
                    "placeholder": "Nama label",
                }
            ),

            "link": URLInput(
                attrs={
                    "placeholder": "https://youtube.com/...",
                }
            ),
        }

