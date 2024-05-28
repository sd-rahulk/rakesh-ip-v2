from django.shortcuts import get_object_or_404, render, redirect
from .models import Doctor, Patient, Appointment
from .forms import DoctorForm, PatientForm, AppointmentForm

def delete_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        doctor.delete()
        return redirect('list_doctors')  # Redirect to a list view of doctors after deletion
    return render(request, 'hms/delete_doctor.html', {'doctor': doctor})

def edit_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('list_doctors')
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'hms/edit_doctor.html', {'form': form})

def doctors(request):
    query = request.GET.get('q')

    if query:
        # Perform a search query based on the provided query
        doctors = Doctor.objects.filter(name__icontains=query)
    else:
        # If no query is provided, return all doctors
        doctors = Doctor.objects.all()

    return render(request, 'doctors_search_results.html', {'doctors': doctors, 'query': query})

def home(request):
    return render(request, 'hms/home.html')

def list_doctors(request):
    doctors = Doctor.objects.all()
    return render(request, 'hms/doctors.html', {'doctors': doctors})

def add_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_doctors')
    else:
        form = DoctorForm()
    return render(request, 'hms/add_doctor.html', {'form': form})

def list_patients(request):
    patients = Patient.objects.all()
    return render(request, 'hms/patients.html', {'patients': patients})

def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_patients')
    else:
        form = PatientForm()
    return render(request, 'hms/add_patient.html', {'form': form})

def list_appointments(request):
    appointments = Appointment.objects.all()
    return render(request, 'hms/appointments.html', {'appointments': appointments})

def add_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_appointments')
    else:
        form = AppointmentForm()
    return render(request, 'hms/add_appointment.html', {'form': form})
