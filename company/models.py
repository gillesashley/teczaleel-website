from django.db import models


class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Company(Base):
    name = models.CharField('Company Name', max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name


class ProjectCoordinator(Base):
    name = models.CharField("Project Coordinator", max_length=100)
    position = models.CharField(max_length=100)
    email = models.EmailField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Project(Base):
    PROJECT_STATUS_CHOICES = (
        (1, 'In Progress'),
        (2, 'Complete'),
        (3, 'On Hold'),
        (4, 'Cancelled'),
    )

    PROGRESS_PERCENT_CHOICES = (
        (0, 0),
        (25, 25),
        (50, 50),
        (75, 75),
        (100, 100),
    )

    name = models.CharField('Project Name', max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    status = models.IntegerField(choices=PROJECT_STATUS_CHOICES, default=1)
    progress_percent = models.IntegerField(choices=PROGRESS_PERCENT_CHOICES, null=True, default=0)
    project_coordinator = models.ForeignKey(ProjectCoordinator, on_delete=models.CASCADE, blank=True, null=True, )

    def __str__(self):
        return self.name

    def get_status_display_value(self):
        return dict(Project.PROJECT_STATUS_CHOICES)[self.status]


class Sprint(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.company} on {self.sprint}'
