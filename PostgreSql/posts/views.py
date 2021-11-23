from django.shortcuts import render,redirect
from . import forms
from django.core.exceptions import ValidationError
from .models import Users

# Create your views here.
def home(request):
  users = Users.objects.order_by('-id').all()
  return render(
    request,'home.html',context={
      'users':users
    }
  )

def regist(request):
  regist_form = forms.RegistForm(request.POST or None, request.FILES or None)
  if regist_form.is_valid():
    try:
      regist_form.save()
      return redirect('posts:home')
    except ValidationError as e:
      regist_form.add_error('password',e)

  return render(request, 'regist.html', context={
    'regist_form' : regist_form
  })