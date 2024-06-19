from django.shortcuts import render
from django.views.generic import DetailView
from . import models,forms
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import CarModel, Comment
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@login_required
def car_detail(request, car_id):
    car = get_object_or_404(CarModel, id=car_id)
    comments = car.comments.all()

    if request.method == 'POST':
        form = forms.CommentedForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.car = car
            comment.save()
            return redirect('details', car_id=car.id)
    else:
        form = forms.CommentedForm()

    return render(request, 'car_detail.html', {
        'car': car,
        'comments': comments,
        'form': form
    })

@login_required
def postupdate(request,id):
    post = models.CarModel.objects.get(pk = id)
    post.quantity -= 1
    post.save()
    
    order = models.Order(carId = id , userId = request.user.id)
    order.save()
    
    return redirect('details',id)