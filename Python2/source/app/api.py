import os
from datetime import datetime
from django.conf import settings
from django.db.models import Q
from django_filters import rest_framework as rest_filters
from rest_framework import generics, status, permissions

from rest_framework.response import Response
from django.db import transaction
from .models import Property
from .conf import PropertyTypeChoices, SpecificationChoices
from .serializers import PropertySerializer

class PropertyView(generics.ListCreateAPIView):
    serializer_class = PropertySerializer   
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        query_vars = Q(is_active=True)
        specification = self.request.GET.get('specification', None)
        property_type = self.request.GET.get('property_type', None)
        search_term = self.request.GET.get('search_term', None)
        if search_term:
            search_term_q = Q()
            for term in search_term.split():
                search_term_q = search_term_q | (
                    Q(location__icontains=term))
            query_vars = query_vars & search_term_q
        if specification:
            query_vars = query_vars & Q(specification=specification)
        if property_type:
            query_vars = query_vars & Q(property_type=property_type)
        return Property.objects.filter(query_vars)