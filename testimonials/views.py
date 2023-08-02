from django.shortcuts import render, get_object_or_404, redirect
from .models import Testimonials
from .forms import TestimonialForm


def testimonial_list(request):
    testimonials = Testimonials.objects.filter(status=1)
    return render(request, 'testimonials/testimonial_list.html', {'testimonials': testimonials})


def testimonial_detail(request, slug):
    testimonial = get_object_or_404(Testimonials, slug=slug)
    return render(request, 'testimonials/testimonial_detail.html', {'testimonial': testimonial})


def add_testimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('testimonial_list')
    else:
        form = TestimonialForm()

    return render(request, 'testimonials/testimonial_form.html', {'form': form})


def edit_testimonial(request, slug):
    testimonial = get_object_or_404(Testimonials, slug=slug)
    if request.method == 'POST':
        form = TestimonialForm(request.POST, instance=testimonial)
        if form.is_valid():
            form.save()
            return redirect('testimonial_detail', slug=slug)
    else:
        form = TestimonialForm(instance=testimonial)

    return render(request, 'testimonials/testimonial_form.html', {'form': form})
