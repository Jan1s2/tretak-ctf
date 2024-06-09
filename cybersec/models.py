from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _

# app for ctf-like challenges with cve, cwe filtering and an exploit database and with player support

# Create your models here.
class Cve(models.Model):
    cve_id = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    cvss = models.FloatField(blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(10)])
    published_date = models.DateField(blank=True, null=True)
    cwe = models.ManyToManyField('Cwe')
    class Meta:
        ordering = ['cve_id']
        verbose_name = 'CVE'
        verbose_name_plural  = 'CVEs'
    def __str__(self):
        return f"{self.cve_id}"

class Cwe(models.Model):
    cwe_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    class Meta:
        ordering = ['cwe_id']
        verbose_name = 'CWE'
        verbose_name_plural = 'CWEs'
    def __str__(self):
        return f"{self.cwe_id}: {self.name}"

class Exploit(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    exploit_code = models.TextField()
    cve = models.ManyToManyField('Cve')
    class Meta:
        ordering = ['name']
        verbose_name = 'Exploit'
        verbose_name_plural  = 'Exploits'
    def __str__(self):
        return f"{self.name}"

class Challenge(models.Model):
    class Difficulites(models.TextChoices):
        EASY = 'EASY', _('Easy')
        MEDIUM = 'MEDIUM', _('Medium')
        HARD = 'HARD', _('Hard')
    category = models.ForeignKey('Category', on_delete=models.RESTRICT, related_name='challenges')
    cve = models.ManyToManyField('Cve', blank=True)
    cwe = models.ManyToManyField('Cwe', blank=True)
    image = models.ImageField(upload_to='images/', verbose_name='Image', null=True, blank=True)
    score = models.IntegerField(default=100,
                                        validators=[
                                            MinValueValidator(1),
                                            MaxValueValidator(100),
                                            ])

    difficulty = models.CharField(
        max_length=6,
        choices=Difficulites.choices,
        default=Difficulites.EASY,
    )

    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        ordering = ['category', 'name']
        verbose_name = 'Challenge'
        verbose_name_plural  = 'Challenges'
    def __str__(self):
        return f"{self.name}"

class Flag(models.Model):
    challenge = models.ForeignKey('Challenge', on_delete=models.CASCADE, related_name='flags')
    flag = models.CharField(max_length=100, unique=True)
    hint = models.TextField(blank=True, null=True)
    class Meta:
        ordering = ['flag']
        verbose_name = 'Flag'
        verbose_name_plural  = 'Flags'
    def __str__(self):
        return f"{self.flag}"


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    class Meta:
        ordering = ['name']
        verbose_name = 'Category'
        verbose_name_plural  = 'Categories'
    def __str__(self):
        return f"{self.name}"

class Writeup(models.Model):
    challenge = models.ForeignKey('Challenge', on_delete=models.CASCADE, related_name='writeups')
    writeup = models.TextField()
    class Meta:
        verbose_name = 'Writeup'
        verbose_name_plural  = 'Writeups'
    def __str__(self):
        return f"{self.challenge} - {' '.join(self.writeup.split()[:5])}..."

# class containing information for k8s manifest
# class Manifest(models.Model):
    # name = models.CharField(max_length=100)
    # challenge = models.ForeignKey('Challenge', on_delete=models.CASCADE)
    # manifest = models.TextField()
    # class Meta:
        # ordering = ['name']
        # verbose_name = 'Manifest'
        # verbose_name = 'Manifests'
    # def __str__(self):
        # return f"{self.name}"
