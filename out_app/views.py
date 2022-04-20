from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from cloudinary.forms import cl_init_js_callbacks
from cloudinary.forms import CloudinaryFileField
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django import forms
from .models import Page, User, ViewerAccess
from .forms import WritePageForm, AllowViewerForm


# view for creator's profile
class CreatorView(generic.ListView):

    model = Page
    template_name = "creator_profile.html"
    paginate_by = 3


# class AllowViewer(View):

#     form_class = AllowViewerForm
#     initial = { "viewer_form": AllowViewerForm }
#     template_name = "allow_viewer.html"

#     def get(self, request, *args, **kwargs):
#         form = self.form_class(initial=self.initial)
#         return render(request, self.template_name, { "viewer_form": AllowViewerForm })

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         # if form.is_valid():
#         #     # <process form cleaned data>
            

#         return render(
#             request, 
#             self.template_name, 
#             {
#                 "viewer_form": AllowViewerForm 
#             },
#             # return HttpResponseRedirect('/creator_profile/')
#         )



class WritePage(View):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "write_page.html",
            {
                "page_form": WritePageForm()
            }
        )

    def post(self, request, *args, **kwargs):
        
        page_form = WritePageForm(request.POST, request.FILES)

        if page_form.is_valid():
            write_page = page_form.save(commit=False)
            write_page.user = request.user
            write_page.save()
        else:
            page_form = WritePageForm()
        
        return render(
            request,
            "creator_profile.html",
            {
                "page_form": page_form
            }
        )


class AllowViewer(View):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "allow_viewer.html",
            {
                "viewer_form": AllowViewerForm()
            }
        )

    def post(self, request, *args, **kwargs):
        
        viewer_form = AllowViewerForm(request.POST)

        if viewer_form.is_valid():
            form = viewer_form.save(commit=False)
            form.user = request.user
            form.save()
        else:
            viewer_form = AllowViewerForm()
        
        return render(
            request,
            "creator_profile.html",
            {
                "viewer_form": viewer_form
            }
        )


class EditPage(UpdateView):
    model = Page
    fields = ['title', 'text_content', 'image', 'link', 'link_title', 'status']
    template_name = "edit_page.html"
    success_url="/creator_profile"


class CreatorPage(TemplateView):

    template_name = "creator_page.html"

        
def resources(request):
    return render(request, "resources.html")


def landing_page(request):
    return render(request, "index.html")




