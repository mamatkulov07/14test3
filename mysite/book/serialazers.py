from rest_framework import serializers
from .models import *


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class MemberSerializers(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'


class LoanSerializers(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'


class FineSerializers(serializers.ModelSerializer):
    class Meta:
        model = Fine
        fields = '__all__'


class ReservationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
