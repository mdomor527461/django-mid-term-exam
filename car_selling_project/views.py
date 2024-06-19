from django.http import HttpResponse
from django.shortcuts import render,redirect
from car.models import CarModel,Order
from brand.models import BrandModel
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.generic.edit import UpdateView
from .forms import EditUserForm





def home(request,slug = None):
    data = CarModel.objects.all()
    
    if slug is not None: 
        brand = BrandModel.objects.get(slug = slug)   
        data = CarModel.objects.filter(brand = brand) 
    brands = BrandModel.objects.all() 
    return render(request, 'base.html', {'data' : data, 'brands':brands})

class SignUpView(FormView):
    template_name = 'signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Your account has been created successfully. You can now log in.')
        return super().form_valid(form)

class LoginView(LoginView):
    template_name = 'signup.html'
    
    def get_success_url(self):
       return reverse_lazy('homepage')
    
    def form_valid(self,form):
        messages.success(self.request,'logged in successfully')
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.success(self.request,'logged in information is incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
    
@login_required
def user_logout(request):
    messages.warning(request,'Log out successfully')
    logout(request)
    return redirect('login')

method_decorator(login_required,name = 'dispatch')
class EditUserView(UpdateView):
    model = User
    form_class = EditUserForm
    template_name = 'edit_profile.html'
    success_url = reverse_lazy('profile')  # Adjust the success URL to your needs

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, 'Your profile has been updated successfully.')
        return super().form_valid(form)

@login_required
def profile(request):
    order = Order.objects.filter(userId = request.user.id)
    
    cars = []
    for id in order:
        print(id.carId,id.userId)
        cars.append(CarModel.objects.get(pk = id.carId))
    return render(request,'profile.html',{'cars' : cars})