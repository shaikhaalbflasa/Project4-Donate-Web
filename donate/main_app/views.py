from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# new function to change status of donation to unavailable

#class based view -> They create form for you
#This view handles both get and post requests
class DonateCreate(LoginRequiredMixin, CreateView):
  model = Donate
  # form fields below
  fields = ['item_image', 'date', 'time', 'location', 'num', 'typeofDonate',]
  success_url='/Donate/'


  def form_valid(self, form):
    form.instance.user = self.request.user 
    return super().form_valid(form)

class DonateUpdate(UpdateView):
  model = Donate
  fields = ['item_image','date', 'time', 'location', 'num',]

class DonateDelete(DeleteView):
  model = Donate
  success_url = '/Donate/'


# Create your views here.

# Define the home view
def home(request):
  return render(request, 'home.html')

def index(request):
  return render(request, 'index.html')

def contactus(request):
  return render(request, 'contactus.html')


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

def donate_collect(request, pk):
  d = Donate.objects.get(id=pk)
  d.status = False
  d.save()
  return redirect('index_donate')

def add_photo(request, cat_id):
	# photo-file was the "name" attribute on the <input type="file">
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    # need a unique "key" for S3 / needs image file extension too
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    # just in case something goes wrong
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      # build the full url string
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      # we can assign to cat_id or cat (if you have a cat object)
      photo = Photo(url=url, Donate_id=Donate_id)
      photo.save()
    except:
      print('An error occurred uploading file to S3')
  return redirect('detail', Donate_id=Donate_id)

# u = User.objects.get(id=request.user.id)
# u.profile.donor







