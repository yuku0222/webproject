from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render

from django.views.generic import TemplateView, ListView

from django.views.generic import TemplateView

from django.views.generic import CreateView

from django.urls import reverse_lazy

from .forms import ProductForm

from django.utils.decorators import method_decorator

from django.contrib.auth.decorators import login_required

from .models import Product

from django.views.generic import DetailView

from django.views.generic import DeleteView


class IndexView(ListView):

    template_name = 'index.html'

    queryset = Product.objects.order_by()

    paginate_by = 9



class UserView(ListView):

    template_name = 'index.html'

    paginate_by = 9

    def get_queryset(self):

        user_id = self.kwargs['user']

        user_list = Product.objects.filter(
            user=user_id).order_by('-last_updated_at')
        
        return user_list

class WebSuccessView(TemplateView):

    template_name = "web_success.html"

@method_decorator(login_required, name='dispatch')
class CreateWebView(CreateView):

    form_class = ProductForm

    template_name = "web.html"

    success_url = reverse_lazy('web:web_done')

    def form_valid(self, form):

        webdate = form.save(commit=False)

        webdate.user = self.request.user

        webdate.save()

        return super().form_valid(form)
    
class NameView(ListView):

    template_name = 'index.html'

    paginate_by = 9

    def get_queryset(self):
        name_id = self.kwargs['name']

        name = Product.objects.filter(
            name=name_id).order_by('-last_updated_at')
        return name
    
class DetailView(DetailView):

    template_name = 'detail.html'

    model = Product


class MypageView(ListView):

    template_name = 'mypage.html'

    paginate_by = 9

    def get_queryset(self):

        queryset = Product.objects.filter(
            user=self.request.user).order_by('-last_updated_at')
        
        return queryset
    
class WebDeleteView(DeleteView):

    model = Product

    template_name = 'web_delete.html'

    success_url = reverse_lazy('web:mypage')

    def delete(self, request, *args,  **kwargs):

        return super().delete(request, *args, **kwargs)
    
    
