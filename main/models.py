from django.db import models
import uuid
# Create your models here.

class About(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    nama=models.CharField(max_length=100)
    lahir=models.DateField(blank=True,null=True)
    ALMAMATER_CHOICE=[
        ('Universitas Indonesia','universitas indonesia'),
        ('Universitas Gajah Mada','universitas gajah mada'),
        ('Institut Teknologi Bandung', 'institut teknologi bandung'),
        ('Universitas Monash','universitas monash')
    ]
    almamater=models.CharField(choices=ALMAMATER_CHOICE,null=True,blank=True,max_length=255)
    genre=models.CharField(null=True,blank=True)
    INSTRUMEN={
        ('Vokal','vokal'),
        ('RAP', 'rap'),
        ('Lainnya','lainnya')
    }
    instrumen=models.CharField(choices=INSTRUMEN,blank=True,null=True)
    label=models.CharField(max_length=200)
    description=models.TextField()