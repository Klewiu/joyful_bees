from django.shortcuts import render
from apps.customers.models import Customer
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.


def customers (request):
    context = {
        'title':'Admin - Lista klientów',
        'customers': Customer.objects.all(),
        'recievers': Customer.email_all(),
    }

    if request.user.is_authenticated and request.user.is_superuser:
        return render(request, 'customers/customers.html', context)
    else:
        return redirect('page-home')

# def manage_customers (request):
#     context = {
#         'title':'Admin - Zarządzanie klientami',
#         'customers': Customer.objects.all(),
#     }

#     if request.user.is_authenticated and request.user.is_superuser:
#         return render(request, 'customers/manage_customers.html', context)
#     else:
#         return redirect('page-home')
    

# CLASS BASE VIEW FOR CUSTOMERS #

class CustomersView (ListView):

  def get (self, request, *args, **kwargs):
  
    context = {
        'customers': Customer.objects.all(),
        'title':'ADMIN - lista klientów',
      }
    return render (request,'customers/manage_customers.html', context)

class CustomersDetailView(DetailView):
  model=Customer
  template_name = 'customers/customers_detail.html'


class CustomersCreateView (LoginRequiredMixin, CreateView):
  model = Customer
  fields = ['name', 'email', 'tel','address']
  template_name = 'customers/customers_create.html'

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

class CustomersUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  model=Customer
  template_name = 'customers/customers_create.html'
  fields = ['name', 'email', 'tel','address']

  def form_valid(self, form):
    # form.instance.author = self.request.user
    return super().form_valid(form)

#checks for currently logged  user to update posts related to current user
#   def test_func(self):
#     post = self.get_object()
#     if self.request.user == post.author:
#       return True
#     else:
#       return False

class CustomersDeleteView(LoginRequiredMixin, UserPassesTestMixin,  DeleteView):
  model=Customer
  template_name = 'pages/customers_delete.html'

#   def test_func(self):
#     post = self.get_object()
#     if self.request.user == post.author:
#       return True
#     else:
#       return False

  success_url = '/customers/'