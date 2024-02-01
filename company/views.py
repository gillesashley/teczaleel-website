from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from .forms import CommentForm
from .models import Project


class TrackProjectView(LoginRequiredMixin, ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'company/track-project.html'
    form_class = CommentForm
    success_url = '/track-project/'  # Set your desired success URL
