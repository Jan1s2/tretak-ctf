from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# app for ctf-like challenges with cve, cwe filtering and an exploit database and with player support

# Create your models here.
class Cve(models.Model):
    cve_id = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    cvss = models.FloatField(blank=True, null=True)
    published_date = models.DateField(blank=True, null=True)
    cwe = models.ManyToManyField('Cwe')
    class Meta:
        ordering = ['cve_id']
        verbose_name = 'CVE'
        verbose_name = 'CVEs'
    def __str__(self):
        return f"{self.cve_id}"

class Cwe(models.Model):
    cwe_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    class Meta:
        ordering = ['cwe_id']
        verbose_name = 'CWE'
        verbose_name = 'CWEs'
    def __str__(self):
        return f"{self.cwe_id}: {self.name}"

class Exploit(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    exploit_code = models.TextField()
    cve = models.ManyToManyField('Cve')
    class Meta:
        ordering = ['name']
        verbose_name = 'Exploit'
        verbose_name = 'Exploits'
    def __str__(self):
        return f"{self.name}"

class Challenge(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    cve = models.ManyToManyField('Cve')
    cwe = models.ManyToManyField('Cwe')
    image = models.ImageField(upload_to='images/', verbose_name='Image', null=True, blank=True)
    score = models.PositiveIntegerField()
    difficulty = models.PositiveIntegerField()

    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        ordering = ['category', 'name']
        verbose_name = 'Challenge'
        verbose_name = 'Challenges'
    def __str__(self):
        return f"{self.name}"

class Flag(models.Model):
    challenge = models.ForeignKey('Challenge', on_delete=models.CASCADE)
    flag = models.CharField(max_length=100)
    hint = models.TextField(blank=True, null=True)
    class Meta:
        ordering = ['flag']
        verbose_name = 'Flag'
        verbose_name = 'Flags'
    def __str__(self):
        return f"{self.flag}"


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    class Meta:
        ordering = ['name']
        verbose_name = 'Category'
        verbose_name = 'Categories'
    def __str__(self):
        return f"{self.name}"

# class containing information for k8s manifest
class Manifest(models.Model):
    name = models.CharField(max_length=100)
    challenge = models.ForeignKey('Challenge', on_delete=models.CASCADE)
    manifest = models.TextField()
    class Meta:
        ordering = ['name']
        verbose_name = 'Manifest'
        verbose_name = 'Manifests'
    def __str__(self):
        return f"{self.name}"
