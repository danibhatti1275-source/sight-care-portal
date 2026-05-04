from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import BookingForm
from .models import EyeDisease, SelfAssessmentQuestion, UserAssessment

def home(request):
    return render(request, 'portal/home.html')

def disease_list(request):
    diseases = EyeDisease.objects.all().order_by('order')
    return render(request, 'portal/disease_list.html', {'diseases': diseases})

def disease_detail(request, slug):
    disease = get_object_or_404(EyeDisease, slug=slug)
    return render(request, 'portal/disease_detail.html', {'disease': disease})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'portal/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'portal/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def self_assessment(request):
    if request.method == 'POST':
        # Get selected symptoms from checkboxes
        selected_symptoms = request.POST.getlist('symptoms')
        
        # Get all diseases
        all_diseases = EyeDisease.objects.all()
        
        # Find matching diseases based on symptoms
        matching_results = []
        
        for disease in all_diseases:
            # Get disease symptoms as list
            disease_symptoms_list = [s.strip().lower() for s in disease.symptoms.split('\n') if s.strip()]
            
            # Count matches
            match_count = 0
            for selected in selected_symptoms:
                selected_clean = selected.strip().lower()
                for symptom in disease_symptoms_list:
                    if selected_clean in symptom or symptom in selected_clean:
                        match_count += 1
                        break
            
            # If any match found, add to results
            if match_count > 0:
                matching_results.append({
                    'disease': disease,
                    'match_score': match_count
                })
        
        # Sort by match score (highest first)
        matching_results.sort(key=lambda x: x['match_score'], reverse=True)
        
        return render(request, 'portal/assessment_result.html', {
            'possible_conditions': matching_results[:3]
        })
    
    diseases = EyeDisease.objects.all().order_by('order')
    return render(request, 'portal/self_assessment.html', {'diseases': diseases})

def prevention_guide(request):
    return render(request, 'portal/prevention_guide.html')

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            if request.user.is_authenticated:
                booking.user = request.user
            booking.save()
            messages.success(request, 'Appointment request sent successfully. We will contact you soon.')
            return redirect('booking')
    else:
        form = BookingForm()
    return render(request, 'portal/booking.html', {'form': form})