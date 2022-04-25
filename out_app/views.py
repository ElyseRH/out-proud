from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
# from django.views.generic import TemplateView, ListView
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django import forms
from .models import Page, User, ViewerAccess
from .forms import WritePageForm, AllowViewerForm

from django.http import HttpResponse
from cloudinary.forms import cl_init_js_callbacks  


# view for creator's profile
class CreatorView(generic.ListView):

    # model = Page
    queryset = Page.objects.all()
    template_name = "creator_profile.html"
    paginate_by = 3   


class WritePage(generic.CreateView):
    
    def get(self, request, *args, **kwargs):

        return render(
            request,
            "write_page.html",
            {"page_form": WritePageForm}
        )

    def post(self, request, *args, **kwargs):
        page_form = WritePageForm(request.POST, request.FILES)

        if page_form.is_valid():
            write_page = page_form.save(commit=False)
            write_page.user = request.user
            write_page.save()
            return redirect('creator_profile')
        else:
            page_form = WritePageForm()
        
        return render(
            request,
            "write_page.html",
            {
                "page_form": page_form
            }
        )


class AllowViewer(View):

    def get(self, request):
        return render(
            request,
            "allow_viewer.html",
            {
                "viewer_form": AllowViewerForm()
            }
        )

    def post(self, request):
        
        viewer_form = AllowViewerForm(request.POST)

        if viewer_form.is_valid():
            form = viewer_form.save(commit=False)
            form.creator = request.user
            form.save()
            send_mail(
                request.POST['first_name'],
                request.POST['email'],
                request.POST['shown_name']
            )
        else:
            viewer_form = AllowViewerForm()
        
        return redirect(
            "creator_profile",
            )


class EditPage(View):

    def get(self, request, slug):
        page_to_edit = Page.objects.get(slug=slug)
        edit_page_form = WritePageForm(instance=page_to_edit)
        return render(
            request,
            "edit_page.html",
            {
                "edit_page_form": edit_page_form
            }
        )  

    def post(self, request, slug):
        if request.method == "POST":
            page_to_edit = Page.objects.get(slug=slug)
            edit_page_form = WritePageForm(request.POST, request.FILES, instance=page_to_edit)
            if edit_page_form.is_valid():
                edit_page_form.save()
                return redirect('creator_profile')
        return render(
            request,
            "edit_page.html",
            {
                "edit_page_form": edit_page_form
            }
        ) 


def creator_page(request, slug):
    page = get_object_or_404(Page, slug=slug)

    return render(
        request,
        "creator_page.html",
        {
            "page": page
        }
    )


def resources(request):
    return render(request, "resources.html")


def landing_page(request):
    return render(request, "index.html")


# def upload(request):
#   context = dict( cloudinary_form = WritePageForm())

#   if request.method == 'POST':
#     form = WritePageForm(request.POST, request.FILES)
#     context['posted'] = form.instance
#     if form.is_valid():
#         form.save()

#   return render(request, 'write_page.html', context)
