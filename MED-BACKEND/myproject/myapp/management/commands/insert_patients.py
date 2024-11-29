from django.core.management.base import BaseCommand
from myapp.models import Patient, Doctor
import datetime

# Define the Command class
class Command(BaseCommand):
    help = 'Insert sample patient and doctor data'

    def handle(self, *args, **kwargs):
        # Insert doctor data
        doctor1 = Doctor.objects.filter(name="Matthew Smith", age=40, gender="Male").first()

        # If no such doctor exists, create a new one
        if not doctor1:
            doctor1 = Doctor.objects.create(name="Matthew Smith", age=40, gender="Male", specialization="Cardiologist")

        unique_id = "5546729503"

        # Check if a patient with the same unique_id already exists
        if not Patient.objects.filter(unique_id=unique_id).exists():
            # If not, create the patient
            patient1 = Patient.objects.create(
                unique_id=unique_id, 
                name="Bobby Jackson", 
                age=30, 
                gender="Male", 
                blood_type="B-", 
                medical_condition="Cancer", 
                admission_date=datetime.date(2024, 1, 31), 
                discharge_date=datetime.date(2024, 2, 2), 
                prescribed_drugs="aspirin", 
                test_results="Normal", 
                doctor=doctor1
            )
            self.stdout.write(self.style.SUCCESS(f"Patient {patient1.name} created successfully."))
        else:
            self.stdout.write(self.style.WARNING(f"Patient with unique_id {unique_id} already exists."))
