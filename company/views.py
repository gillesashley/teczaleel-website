from django.shortcuts import get_object_or_404
from django.views.generic import ListView, CreateView
from .models import Project, Sprint, Comment
from .forms import CommentForm


class TrackProjectView(ListView, CreateView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'company/track-project.html'
    form_class = CommentForm
    success_url = '/track-project/'  # Set your desired success URL

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project_list = Project.objects.all()

        # Fetch all sprints and comments for each project
        project_data = []
        for project in project_list:
            sprints = Sprint.objects.filter(project=project)
            sprint_data = []
            for sprint in sprints:
                comments = Comment.objects.filter(sprint=sprint)
                sprint_data.append({'sprint': sprint, 'comments': comments})
            project_data.append({'project': project, 'sprints': sprint_data})

        context['project_data'] = project_data
        return context

    def form_valid(self, form):
        form.instance.sprint = get_object_or_404(Sprint, pk=self.kwargs['sprint_id'])
        form.instance.company = self.request.user.company  # Assuming you have a user and company relationship
        return super().form_valid(form)
