'''
Serializers.py
'''
from rest_framework import serializers
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.db.models import Sum, Q, F, Value
from django.db.models.functions import Coalesce
from django.urls import reverse_lazy
from .models import Property
from .conf import PropertyTypeChoices, SpecificationChoices

class PropertySerializer(serializers.ModelSerializer):

    class Meta:
        model =  Property
        fields = ('description', 'cost', 'specifictions', 'location', 'property_type', )

    def __init__(self, *args, **kwargs):
        super(PropertySerializer, self).__init__(*args, **kwargs)
        context = kwargs.get('context', None)
        self.request = context['request']

    def create(self, validated_data):
        property = Property.objects.create(**validated_data)
        return property
