from django.db import models
from django.core.validators import FileExtensionValidator

def upload_path(instance, filename):
    return f"uploads/{filename}"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    uploaded_file = models.FileField(upload_to=upload_path, null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  
    deleted_at = models.DateTimeField(null=True, blank=True, default=None)

    def __str__(self):
        return self.name

    # def clean(self):
    #     import os
    #     from django.core.exceptions import ValidationError

    #     if self.uploaded_file:
    #         ext = os.path.splitext(self.uploaded_file.name)[1]  
    #         valid_extensions = ['.pdf', '.png', '.jpeg', '.jpg']
    #         if ext.lower() not in valid_extensions:
    #             raise ValidationError("Only PDF, PNG, and JPEG files are allowed.")
