# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from .models import Product

# Create a model serializer
class ProductSerializer(serializers.HyperlinkedModelSerializer):
	# specify model and fields
	class Meta:
		model = Product
		fields = ('sno', 'title_string','mrp','discountedPrice','rating','review_count','available','ram','os','importer','timestamp')
