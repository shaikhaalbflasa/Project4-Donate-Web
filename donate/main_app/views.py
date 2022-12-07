from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView


#class based view -> They create form for you
#This view handles both get and post requests
class DonateCreate(LoginRequiredMixin, CreateView):
  model = Donate
  # form fields below
  fields = ['item_image', 'date', 'time', 'location', 'num', 'typeofDonate']
  success_url='/Donate/'


  def form_valid(self, form):
    form.instance.user = self.request.user 
    return super().form_valid(form)

class DonateUpdate(UpdateView):
  model = Donate
  fields = ['item_image','date', 'time', 'location', 'num']

class DonateDelete(DeleteView):
  model = Donate
  success_url = '/Donate/'


# Create your views here.

# Define the home view
def home(request):
  return render(request, 'home.html')

def index(request):
  return render(request, 'index.html')

def signup_donor(request):
  # u = request.user.profile.first()
  p = Profile.objects.filter(user_id=request.user.id)
  print(p)
  if p.exists():
    return redirect('home')  
  if request.method == 'GET':
    return render(request, 'registration/signup_donor.html')
  print(request.POST)
  p = Profile(
    user_id=request.user.id,
    donor=request.POST.get('donor'),
    company=request.POST.get('company')
    )
  p.save()
  return redirect('home')


# Define the about view
def about(request):
  return render(request, 'about.html')

def signup (request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('signup_donor')
    else:
      error_message = 'Invalid sign up , try again'
    
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
    
@login_required
def Donate_index(request):
  donate = Donate.objects.filter(user=request.user)
  return render(request, 'Donate/index.html', { 'Donate': donate})

def Donate_detail(request, Donate_id):
  donate = Donate.objects.get(id=Donate_id)
 
  return render(request, 'Donate/detail.html', {'Donate': donate })

def index_donate(request):
  donate = Donate.objects.all()
  return render(request, 'Donate/index.html', { 'Donate': donate})




# u = User.objects.get(id=request.user.id)
# u.profile.donor







