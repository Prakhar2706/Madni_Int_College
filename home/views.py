from django.shortcuts import render,HttpResponse
from home.models import Event,News,Announcement,Floating
from gallery.models import Gallery
from faculty.models import Faculty
from admission.models import Admission_Form
from home.forms import AdmissionForm
from about.models import About
from initiative.models import Initiative
from challenge.models import Challenge
from career.models import Career
from tables.models import Table

# Create your views here.
def index(request):
    EventData=Event.objects.all().order_by('Event_month')
    NewsData=News.objects.all().order_by('News_name')
    AnnouncementData=Announcement.objects.all().order_by('Announcement_name')
    FloatingData=Floating.objects.all()
    data={
        'EventData':EventData,
        'NewsData': NewsData,
        'AnnouncementData':AnnouncementData,
        'FloatingData': FloatingData
    }    
    return render(request,'index.html',data)
def about(request):
    AboutData=About.objects.all()
    data={
        'AboutData':AboutData
    }
    return render(request,'about.html',data)
def academic_council(request):
    ChallengeData=Challenge.objects.all()
    data={
        'ChallengeData':ChallengeData
    }
    return render(request,'academic_council.html',data)
def career(request):
    CareerData=Career.objects.all()
    data={
        'CareerData':CareerData
    }
    return render(request,'career.html',data)
def directors_message(request):
    return render(request,'directors_message.html')
def faculty(request):
    FacultyData=Faculty.objects.all()
    data={
        'FacultyData':FacultyData
    }
    return render(request,'faculty.html',data)
def faq(request):
    return render(request,'faq.html')
def form(request):
    if request.method == 'POST':
        form = AdmissionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
           # return redirect('success')  
    else:
        form = AdmissionForm()
    return render(request,'form.html',{'form': form})
def gallery(request):
    GalleryData=Gallery.objects.all()
    data={
        'GalleryData': GalleryData
    }
    return render(request,'gallery.html',data)
def library(request):
    return render(request,'library.html')
def rti(request):
    return render(request,'rti.html')
def student_corner(request):
    return render(request,'student_corner.html')
def initial(request):
    InitiativeData=Initiative.objects.all()
    data={
        'InitiativeData' :InitiativeData
    }
    return render(request,'initial.html',data) 
def time_table(request):
    TimeData=Table.objects.all()
    data={
        'TimeData': TimeData
    }
    return render(request,'time_table.html',data)   
