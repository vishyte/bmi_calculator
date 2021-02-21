from django.shortcuts import render



def bmi(request):

    Height = float(request.GET.get('Height', 1))
    Weight = float(request.GET.get('Weight', 1))

    bmi = float(Weight/(Height**2))

    return render(request, 'Bmi_cal/bmi.html',{"bmi": bmi})

def home (request):
    return render(request, 'Bmi_cal/Home.html')


