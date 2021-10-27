from django.shortcuts import render
from apps.products.models import Product
from apps.pages.models import Site_description
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django_filters.views import FilterView
from .filters import ProductFilter
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from .forms import NewProductForm

# Create your views here.
def products(request):
    
    context = {
        'title':'Produkty',
        'products': Product.objects.all(),
        'site_description': Site_description.objects.all(),
    }
    return render (request,'products/products.html', context)

# def products_list(request):
    
#     context = {
#         'title':'Admin - Lista produktów',
#         'products': Product.objects.all(),
#     }

#     if request.user.is_authenticated and request.user.is_superuser:
#         return render (request,'products/products_list.html', context)
#     else:
#         return redirect('page-home')


# CLASS BASE VIEW FOR CUSTOMERS #

# Class that add functionality to another class ("Mixin") to check if user is admin or staff member #
class AdminStaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

# Class that shows all products with filtration - only for admin #
class ProductsView (AdminStaffRequiredMixin, FilterView):
    model=Product
    template_name = 'products/products_list.html'
    filterset_class = ProductFilter

    def get_queryset(self):
      qs = self.model.objects.all()
      product_filtered_list = ProductFilter(self.request.GET, queryset=qs)
      return product_filtered_list.qs

class ProductsDetailView(AdminStaffRequiredMixin, DetailView): 
  model=Product
  template_name = 'products/products_detail.html'

class ProductsCreateView (AdminStaffRequiredMixin, LoginRequiredMixin, CreateView):
  model = Product
  fields = ['name', 'description', 'price','promotion','availability','image']
  template_name = 'products/products_create.html'

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)
 
class ProductsUpdateView(AdminStaffRequiredMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  model=Product
  template_name = 'products/products_create.html'
  fields = ['name', 'description', 'price','promotion','availability','image']

  def form_valid(self, form):
    return super().form_valid(form)

class ProductsDeleteView(AdminStaffRequiredMixin, LoginRequiredMixin, UserPassesTestMixin,  DeleteView):
  model=Product
  template_name = 'products/products_delete.html'
  success_url = '/products_list/'