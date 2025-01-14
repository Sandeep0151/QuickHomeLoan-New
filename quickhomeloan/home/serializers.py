from rest_framework import serializers
from .models import *


class LoanApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanApplication
        fields = ['required_amount', 'need_time', 'bank_type', 'name', 'mobile']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'message']


class CreditScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditScore
        fields = '__all__'
