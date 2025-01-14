from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt
from .models import *
import json
import math
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework.decorators import api_view
from django.middleware.csrf import get_token

def csrf_token_view(request):
    return JsonResponse({'csrfToken': get_token(request)})


class ContactFormView(APIView):
    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Contact form submitted successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoanApplicationView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoanApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Application submitted successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def index(request):
    return render(request, "index.html")


def homeloan(request):
    return render(request, "homeloan.html")


def form(request):
    return render(request, "form.html")


def property(request):
    return render(request, "property.html")


@csrf_exempt
def save_property_details(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            property_details = PropertyDetails.objects.create(
                bhk=data['bhk'],
                budget=data['budget'],
                name=data['name'],
                phone=data['phone'],
                email=data['email'],
                city=data.get('city', ''),
                property_name=data.get('property_name', ''),
                area_pin_code=data.get('area_pin_code', ''),
            )
            return JsonResponse({'message': 'Property details saved successfully!'})
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=400)
    return JsonResponse({'message': 'Invalid request method'}, status=405)


def emi_calculator(request):
    return render(request, 'emi_calculator.html')


def emi_calculator2 ( request ) :
    return render ( request , "emi_calculator2.html" )


def part_payment_calculator(request):
    if request.method == "POST":
        # Input values
        loan_amount = float(request.POST.get("loan_amount"))
        interest_rate = float(request.POST.get("interest_rate")) / 12 / 100
        loan_tenure = int(request.POST.get("loan_tenure")) * 12  # Convert years to months
        pre_payment = float(request.POST.get("pre_payment"))

        # Calculate original EMI
        original_emi = (loan_amount * interest_rate * math.pow(1 + interest_rate, loan_tenure)) / (
            math.pow(1 + interest_rate, loan_tenure) - 1
        )

        # After part payment
        new_loan_amount = loan_amount - pre_payment
        revised_emi = (new_loan_amount * interest_rate * math.pow(1 + interest_rate, loan_tenure)) / (
            math.pow(1 + interest_rate, loan_tenure) - 1
        )

        # Calculate savings
        total_savings = (original_emi - revised_emi) * loan_tenure

        context = {
            "original_emi": round(original_emi, 2),
            "revised_emi": round(revised_emi, 2),
            "total_savings": round(total_savings, 2),
        }
        return render(request, "part_payment.html", context)
    return render(request, "part_payment.html")


def eligibility(request):
    return render(request, "eligibility.html")


class CreditScoreView(APIView):
    def post(self, request):
        serializer = CreditScoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Data saved successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


