# from .models import Products as products 
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.views.decorators.csrf import csrf_protect
# from django.views.generic import DetailView
from django.views.generic.edit import FormMixin
from django.http import HttpResponse
from .models import Products, Category_goods, Order, Products_Review
from .forms import ProductsReviewForm, UserUpdateForm, ProfileUpdateForm
from .models import Order
from .models import Products
import plotly.express as px
import plotly.offline as po
import pandas as pd

def items(request):
    num_products = Products.objects.all().count()
    num_category = Category_goods.objects.all().count()
    num_order = Order.objects.all().count()
    num_review = Products_Review.objects.all().count()

    df = pd.DataFrame(
        dict(
            x=["products", "category_goods", "order", "products_review"],
            y=[num_products, num_category, num_order, num_review],
        )
    )
    fig = px.bar(df, x='x', y='y')
    bars = po.plot(fig, output_type='div')

    context = {
        'num_products': num_products,
        'num_category': num_category,
        'num_order': num_order,
        'num_review': num_review,
        "bars": bars
              }
    return render(request, 'myapp/items.html', context=context)

def index(request):
    product_objects = Products.objects.all()
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(title__icontains=item_name)
    paginator = Paginator(product_objects, 4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)
    return render(request,'myapp/index.html', {'product_objects':product_objects})

class ProductsDetailView(FormMixin,generic.DetailView):
    model = Products
    template_name = 'myapp/detail.html'
    form_class= ProductsReviewForm
    context_object_name = 'product_object'

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.id})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.products = self.object
        form.instance.reviewer = self.request.user
        form.save()
        return super(ProductsDetailView, self).form_valid(form)

def checkout(request):
    if request.method == "POST":
        items = request.POST.get('items',"")
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        address = request.POST.get('address',"")
        city = request.POST.get('city',"")
        zipcode = request.POST.get('zipcode',"")
        total = request.POST.get('total',"")
        order = Order(items=items,name=name,email=email,address=address,city=city,zipcode=zipcode,total=total)
        order.save()
    return render(request,'myapp/checkout.html')

@csrf_protect
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojo vardas {username} uzimtas!')
                return  redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, f' El. pastas  {email} uzimtas!')
                    return redirect('register')
                else:
                    User.objects.create_user(username=username, email=email, password=password)
                    messages.info(request, f' Vartotojas  {username} uzregistruotas!')
                    return redirect('login')
        else:
            messages.error(request, 'Slaptazodziai nesutampa!')
            return redirect('register')
    return render(request, 'register.html')

@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Profilis atnaujintas")
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'myapp/profile.html', context)



