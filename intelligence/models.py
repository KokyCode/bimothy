from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Gang(models.Model):
    """Gang organization model"""
    name = models.CharField(max_length=200)
    tag = models.CharField(max_length=10, help_text="Gang tag/abbreviation")
    color = models.CharField(max_length=7, default="#FF0000", help_text="Hex color code")
    territory = models.TextField(blank=True, help_text="Territory description")
    threat_level = models.CharField(
        max_length=20,
        choices=[
            ('LOW', 'Low'),
            ('MEDIUM', 'Medium'),
            ('HIGH', 'High'),
            ('CRITICAL', 'Critical'),
        ],
        default='MEDIUM'
    )
    founded_date = models.DateField(null=True, blank=True)
    member_count = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-threat_level', 'name']

    def __str__(self):
        return f"{self.name} ({self.tag})"


class GangMember(models.Model):
    """Gang member profile"""
    gang = models.ForeignKey(Gang, on_delete=models.CASCADE, related_name='members')
    name = models.CharField(max_length=200)
    alias = models.CharField(max_length=200, blank=True)
    rank = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(upload_to='members/', blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    known_associates = models.ManyToManyField('self', blank=True, symmetrical=True)
    criminal_record = models.TextField(blank=True)
    last_seen = models.DateTimeField(null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('ACTIVE', 'Active'),
            ('INACTIVE', 'Inactive'),
            ('WANTED', 'Wanted'),
            ('INCARCERATED', 'Incarcerated'),
            ('DECEASED', 'Deceased'),
        ],
        default='ACTIVE'
    )
    threat_level = models.CharField(
        max_length=20,
        choices=[
            ('LOW', 'Low'),
            ('MEDIUM', 'Medium'),
            ('HIGH', 'High'),
            ('CRITICAL', 'Critical'),
        ],
        default='LOW'
    )
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['gang', 'name']

    def __str__(self):
        return f"{self.name} - {self.gang.tag}"


class Incident(models.Model):
    """Incident report"""
    title = models.CharField(max_length=300)
    incident_type = models.CharField(
        max_length=50,
        choices=[
            ('ASSAULT', 'Assault'),
            ('ROBBERY', 'Robbery'),
            ('DRUG_TRAFFICKING', 'Drug Trafficking'),
            ('MURDER', 'Murder'),
            ('WEAPONS', 'Weapons Offense'),
            ('TERRITORY_DISPUTE', 'Territory Dispute'),
            ('OTHER', 'Other'),
        ]
    )
    gangs_involved = models.ManyToManyField(Gang, related_name='incidents', blank=True)
    members_involved = models.ManyToManyField(GangMember, related_name='incidents', blank=True)
    location = models.CharField(max_length=300)
    date_time = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    severity = models.CharField(
        max_length=20,
        choices=[
            ('LOW', 'Low'),
            ('MEDIUM', 'Medium'),
            ('HIGH', 'High'),
            ('CRITICAL', 'Critical'),
        ],
        default='MEDIUM'
    )
    status = models.CharField(
        max_length=20,
        choices=[
            ('OPEN', 'Open'),
            ('INVESTIGATING', 'Investigating'),
            ('CLOSED', 'Closed'),
        ],
        default='OPEN'
    )
    reported_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    evidence = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_time']

    def __str__(self):
        return f"{self.title} - {self.date_time.strftime('%Y-%m-%d')}"


class GangRelationship(models.Model):
    """Relationship between gangs"""
    gang_1 = models.ForeignKey(Gang, on_delete=models.CASCADE, related_name='relationships_as_gang1')
    gang_2 = models.ForeignKey(Gang, on_delete=models.CASCADE, related_name='relationships_as_gang2')
    relationship_type = models.CharField(
        max_length=20,
        choices=[
            ('ALLIED', 'Allied'),
            ('NEUTRAL', 'Neutral'),
            ('RIVAL', 'Rival'),
            ('WAR', 'At War'),
        ],
        default='NEUTRAL'
    )
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['gang_1', 'gang_2']

    def __str__(self):
        return f"{self.gang_1.tag} - {self.relationship_type} - {self.gang_2.tag}"


class CaseFile(models.Model):
    """Case file for investigations"""
    case_number = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=300)
    gangs = models.ManyToManyField(Gang, related_name='cases', blank=True)
    members = models.ManyToManyField(GangMember, related_name='cases', blank=True)
    lead_agent = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='lead_cases')
    team_members = models.ManyToManyField(User, related_name='case_team', blank=True)
    description = models.TextField()
    priority = models.CharField(
        max_length=20,
        choices=[
            ('LOW', 'Low'),
            ('MEDIUM', 'Medium'),
            ('HIGH', 'High'),
            ('URGENT', 'Urgent'),
        ],
        default='MEDIUM'
    )
    status = models.CharField(
        max_length=20,
        choices=[
            ('OPEN', 'Open'),
            ('ACTIVE', 'Active Investigation'),
            ('PENDING', 'Pending'),
            ('CLOSED', 'Closed'),
        ],
        default='OPEN'
    )
    opened_date = models.DateTimeField(default=timezone.now)
    closed_date = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True)
    image = models.ImageField(upload_to='case_files/', blank=True, null=True, help_text="Case file image/evidence")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-priority', '-opened_date']

    def __str__(self):
        return f"{self.case_number} - {self.title}"

