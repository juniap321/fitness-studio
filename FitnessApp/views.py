from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FitnessClass, Booking
from .serializers import FitnessClassSerializer, BookingSerializer
from django.utils import timezone
from django.shortcuts import get_object_or_404
import logging

logger = logging.getLogger(__name__)

class ClassListView(APIView):
    def get(self, request):
        classes = FitnessClass.objects.filter(datetime_ist__gte=timezone.now()).order_by('datetime_ist')
        serializer = FitnessClassSerializer(classes, many=True, context={'request': request})
        return Response(serializer.data)

class BookClassView(APIView):
    def post(self, request):
        class_id = request.data.get('class_id')
        client_name = request.data.get('client_name')
        client_email = request.data.get('client_email')

        if not all([class_id, client_name, client_email]):
            return Response({"error": "Missing required fields."}, status=status.HTTP_400_BAD_REQUEST)
        fitness_class = get_object_or_404(FitnessClass, id=class_id)
        if fitness_class.available_slots <= 0:
            return Response({"error": "No slots available."}, status=status.HTTP_400_BAD_REQUEST)

        booking = Booking.objects.create(
            fitness_class=fitness_class,
            client_name=client_name,
            client_email=client_email
        )

        fitness_class.available_slots -= 1
        fitness_class.save()

        logger.info(f"Booking successful for {client_email} in class {fitness_class.name}")
        return Response({"message": "Booking successful"}, status=status.HTTP_201_CREATED)

class BookingListView(APIView):
    def get(self, request):
        email = request.GET.get('email')
        if not email:
            return Response({"error": "Email is required."}, status=status.HTTP_400_BAD_REQUEST)

        bookings = Booking.objects.filter(client_email=email)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)
