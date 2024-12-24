from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    posted_date = models.DateField()
    updated_at = models.DateField(null=True, blank=True)  # Updated at (if available)
    details_url = models.URLField()
    salary = models.CharField(max_length=255, null=True, blank=True)  # Compensation
    job_type = models.CharField(max_length=100, null=True, blank=True)  # Employment type
    is_remote = models.BooleanField(default=False)  # Whether the job is remote
    employer_type = models.CharField(max_length=100, null=True, blank=True)  # Type of employer (e.g., corporation, agency)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['title', 'company'], name='unique_job')
        ]  # New style unique constraint


    def __str__(self):
        return self.title
