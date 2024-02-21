from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import request
from django.shortcuts import redirect, render
from django.views.generic import ListView

from .forms import CommentForm
from .models import Project, Sprint


class TrackProjectView(LoginRequiredMixin, ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'company/track-project.html'
    form_class = CommentForm
    success_url = '/track-project/'  # Set your desired success URL

    def get_queryset(self):
        return Project.objects.filter(company=self.request.user.my_company)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class
        # Include sprints for each project
        for project in context['project_list']:
            project.sprints = project.sprint_set.all()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # Create the comment instance, associating it with the correct sprint
            sprint_id = request.POST.get('sprint')
            sprint = Sprint.objects.get(id=sprint_id)
            comment = form.save(commit=False)
            comment.sprint = sprint

            # Access the company based on your model relationships
            if hasattr(request.user, 'my_company'):  # Check if 'my_company' field exists
                comment.company = request.user.my_company
            else:
                comment.company = request.user.companies.first()  # Assuming one company per user

            comment.save()
            return redirect(self.success_url)
        else:
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return render(self, self.template_name, context)


class StartProjectView(ListView):
    model = Project
    template_name = 'company/start-a-project.html'
