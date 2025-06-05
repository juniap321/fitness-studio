from rest_framework import serializers
from .models import FitnessClass, Booking
from django.utils.timezone import get_current_timezone, make_aware
import pytz

class FitnessClassSerializer(serializers.ModelSerializer):
    datetime = serializers.SerializerMethodField()

    class Meta:
        model = FitnessClass
        fields = ['id', 'name', 'datetime', 'instructor', 'available_slots']

    def get_datetime(self, obj):
        request = self.context.get('request')
        tz = request.GET.get('timezone', 'Asia/Kolkata')  # Default IST
        try:
            target_tz = pytz.timezone(tz)
        except Exception:
            target_tz = pytz.timezone('Asia/Kolkata')
        return obj.datetime_ist.astimezone(target_tz).isoformat()

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'fitness_class', 'client_name', 'client_email']
