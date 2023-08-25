from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from pytils.translit import slugify

from catalog.models import Product, Blog


# Create your views here.
class HomeListView(ListView):
    model = Product
    extra_context = {'title': 'SkyStore Главная'}


class ProductDetailView(DetailView):
    model = Product
    extra_context = {'title': 'Информация о товаре'}


class ProductCreateView(CreateView):
    model = Product
    fields = ('product_name', 'product_description', 'product_category', 'product_price', 'product_image')
    success_url = reverse_lazy('catalog:homepage')


def contacts(request):
    context = {'title': 'SkyStore Контакты'}
    return render(request, 'catalog/contacts.html', context)


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'body', 'image', 'is_published', 'views_count')
    success_url = reverse_lazy('catalog:blogs')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)


class BlogListView(ListView):
    model = Blog
    extra_context = {'title': 'Блоги'}

    def get_queryset(self, *args, **kwargs):
        query = super().get_queryset(*args, **kwargs)
        query = query.filter(is_published=True)

        return query


class BlogDetailView(DetailView):
    model = Blog
    extra_context = {'title': 'Блог'}

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()

        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'body', 'image', 'is_published', 'views_count')
    success_url = reverse_lazy('catalog:blogs')

    def get_success_url(self):
        return reverse('catalog:blog_details', args=[self.object.pk])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blogs')
