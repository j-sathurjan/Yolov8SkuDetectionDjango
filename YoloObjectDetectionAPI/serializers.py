from rest_framework import serializers
from .models import ImageUpload,Product

class ImageUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageUpload
        fields = ['image_file', 'confidence_threshold']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        field=['id','name','price','image']