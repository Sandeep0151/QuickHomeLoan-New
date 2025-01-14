from django.urls import path, re_path
from .views import *
from django.views.generic import TemplateView


urlpatterns = [

    path("homeloan", homeloan, name="homeloan"),
    path("form", form, name="form"),
    path("property", property, name="property"),
    #path('api/save-loan-application/', LoanApplicationView.as_view(), name='save-loan-application'),
    path('api/save-property-details/', save_property_details, name='save_property_details'),
    path('api/credit-score/', CreditScoreView.as_view(), name='credit_score'),
    path('emi-calculator/', emi_calculator, name='emi_calculator'),
    path('emi-calculator2/', emi_calculator2, name='emi_calculator2'),
    path("calculator/", part_payment_calculator, name="part_payment_calculator"),
    path("eligibility/", eligibility, name="eligibility"),
    path('api/loan-application/', LoanApplicationView.as_view(), name='loan-application'),
    path('api/contact/', ContactFormView.as_view(), name='contact_form'),
    path('api/get-csrf-token/', csrf_token_view, name='get-csrf-token'),
    re_path(r'^.*$', index, name='index'),


]