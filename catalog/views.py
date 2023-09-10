from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from pytils.translit import slugify

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Blog, Version


# Create your views here.
class HomeListView(ListView):
    model = Product
    extra_context = {'title': 'SkyStore Главная'}


class ProductDetailView(DetailView):
    model = Product
    extra_context = {'title': 'Информация о товаре'}


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:homepage')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)

        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:product_details', args=[self.object.pk])


class ProductDeleteView(DeleteView):
    model = Product
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
