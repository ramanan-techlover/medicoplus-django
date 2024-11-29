from django.shortcuts import render
from django.http import HttpResponse
from db_connection import db  # Import the db connection

Patient_collection = db['patients']  # Access the 'patients' collection

def home(request):
    return render(request, 'index.html')

def doctors(request):
    return render(request, 'doctors.html')

def login(request):
    return render(request, 'login.html')

def healthcard(request):
    return render(request, 'healthcard.html')

def medicine(request):
    return render(request, 'medicine.html')

def laboratory(request):
    return render(request, 'laboratory.html')

def onlineconsultation(request):
    return render(request, 'onlineconsultation.html')

def psychiatry(request):
    return render(request, 'psychiatry.html')

def gynecology(request):
    return render(request, 'gynecology.html')

def pulmonology(request):
    return render(request, 'pulmonology.html')

def orthopedics(request):
    return render(request, 'orthopedics.html')

def pediatrics(request):
    return render(request, 'pediatrics.html')

def osteology(request):
    return render(request, 'osteology.html')

def blog1(request):
    return render(request, 'blog1.html')

def blog2(request):
    return render(request, 'blog2.html')

def blog3(request):
    return render(request, 'blog3.html')

def privacy_policy(request):
    return render(request, 'pp.html')

def join_as_doctor(request):
    return render(request, 'joinasdoctor.html')

def terms_and_conditions(request):
    return render(request, 'termsandconditions.html')



def add_patient(request):
    # Add a patient record to the MongoDB collection
    patient_record = {
        "unique_id": 5546729503, 
        "name": "Bobby Jackson", 
        "age": 30, 
        "gender": "Male", 
        "blood_type": "B-", 
        "medical_condition": "Cancer", 
        "admission_date": "2024-01-31", 
        "discharge_date": "2024-02-02", 
        "prescribed_drugs": "aspirin", 
        "test_results": "Normal", 
        "doctor": "doctor1"
    }
    Patient_collection.insert_one(patient_record)
    return HttpResponse("Patient added successfully!")


Patient_collection = db['patients']  # Access the 'patients' collection

def nfc_scan(request, card_id):
    try:
        # Convert card_id to int if it's numeric in the database
        try:
            card_id = int(card_id)  # Ensure the card_id is an integer if stored as such in MongoDB
        except ValueError:
            return render(request, 'patient_not_found.html', {'error_message': "Invalid NFC Card ID", 'card_id': card_id})

        # Query the patient from MongoDB by unique_id
        patient = Patient_collection.find_one({"unique_id": card_id})

        if patient:
            # Patient found, render the patient details page
            return render(request, 'patient_details.html', {'patient': patient})
        else:
            # If patient is not found, render a "not found" page with a message
            return render(request, 'patient_not_found.html', {
                'error_message': "No patient record found for the scanned NFC card.",
                'card_id': card_id
            })
    
    except Exception as e:
        # Handle any potential errors (e.g., database connection issues)
        return render(request, '404.html')
