from django.db import models
import uuid

class Report(models.Model):

    LANGUAGE_CHOICES = [
        ('zulu',      'Zulu'),
        ('xhosa',     'Xhosa'),
        ('sotho',     'Sotho'),
        ('afrikaans', 'Afrikaans'),
        ('english',   'English'),
    ]

    MODE_CHOICES = [
        ('standard',   'Standard Mode'),
        ('simplified', 'Simplified Mode'),
    ]

    ISSUE_CHOICES = [
        ('pothole',     'Pothole'),
        ('water_leak',  'Water Leak'),
        ('waste',       'Uncollected Waste'),
        ('electricity', 'Electricity Outage'),
        ('other',       'Other'),
    ]

    STATUS_CHOICES = [
        ('Received',       'Received'),
        ('Under Review',   'Under Review'),
        ('In Progress',    'In Progress'),
        ('Resolved',       'Resolved'),
    ]

    reference_number = models.CharField(max_length=20, unique=True, blank=True)
    language         = models.CharField(max_length=20,  choices=LANGUAGE_CHOICES, default='english')
    mode             = models.CharField(max_length=20,  choices=MODE_CHOICES,     default='standard')
    issue_type       = models.CharField(max_length=50,  choices=ISSUE_CHOICES)
    address          = models.CharField(max_length=255)
    description      = models.TextField()
    phone_number     = models.CharField(max_length=15)
    submitted_at     = models.DateTimeField(auto_now_add=True)
    status           = models.CharField(
                           max_length=50,
                           choices=STATUS_CHOICES,
                           default='Received'
                       )

    def save(self, *args, **kwargs):
        if not self.reference_number:
            self.reference_number = 'CM-' + str(uuid.uuid4()).upper()[:8]
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.reference_number} — {self.get_issue_type_display()} — {self.status}"