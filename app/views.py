from django.shortcuts import render

# Create your views here.
from .models import step_count, calories_burnt, distance_covered, heart_rate;

# Send data from model to template through view.py
def dashboard_view(request):

    Count = step_count.objects.all()
    Joule = calories_burnt.objects.all()
    KM = distance_covered.objects.all()
    BPM = heart_rate.objects.all()

    context = {
        "Count" : Count,
        "Joule": Joule,
        "KM" : KM,
        "BPM" : BPM,
    }
    # template path changed from chartapp/index to app/index
    return render(request, 'app/index.html', context)

# This code snippet is used to refresh the data on the dashboards.
import subprocess
from django.http import JsonResponse

def run_database_script(request):
    result = subprocess.run(["python", "database.py"], capture_output=True, text=True)
    return JsonResponse({"stdout": result.stdout, "stderr": result.stderr})


