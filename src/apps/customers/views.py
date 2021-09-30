from django.shortcuts import render
from apps.customers.models import Customer
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django_filters.views import FilterView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .filters import OrderFilter
# Create your views here.

# CLASS BASE VIEW FOR CUSTOMERS #

# Class that add functionality to another class ("Mixin") to check if user is admin or staff member #
class AdminStaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

# Class that shows all customers - only for admin #
class CustomersView (AdminStaffRequiredMixin, FilterView):
    model=Customer
    template_name = 'customers/manage_customers.html'
    filterset_class = OrderFilter

    def get_queryset(self):
      qs = self.model.objects.all()
      customer_filtered_list = OrderFilter(self.request.GET, queryset=qs)
      return customer_filtered_list.qs

class CustomersDetailView(AdminStaffRequiredMixin, DetailView): 
  model=Customer
  template_name = 'customers/customers_detail.html'

class CustomersCreateView (AdminStaffRequiredMixin, LoginRequiredMixin, CreateView):
  model = Customer
  fields = ['name', 'email', 'tel','address']
  template_name = 'customers/customers_create.html'

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

class CustomersUpdateView(AdminStaffRequiredMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  model=Customer
  template_name = 'customers/customers_create.html'
  fields = ['name', 'email', 'tel','address']

  def form_valid(self, form):
    # form.instance.author = self.request.user
    return super().form_valid(form)

class CustomersDeleteView(AdminStaffRequiredMixin, LoginRequiredMixin, UserPassesTestMixin,  DeleteView):
  model=Customer
  template_name = 'customers/customers_delete.html'
  success_url = '/manage_customers/'


  