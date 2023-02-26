from django.conf import settings
from django.db import models
from med_care.models import MedicalCareProfile
from work.models import Work


class Application(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    carer = models.ForeignKey(
        MedicalCareProfile, on_delete=models.CASCADE, related_name="applicant_list"
    )
    job = models.ForeignKey(Work, on_delete=models.CASCADE, related_name="job_list")

    class Meta:
        unique_together = ["carer", "job"]
        # ordering = ('-created_at',)

    def __str__(self):
        return f"{self.job}"
