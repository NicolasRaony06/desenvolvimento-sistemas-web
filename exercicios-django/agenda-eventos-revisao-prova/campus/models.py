from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=200)
    capacity = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Local"
        verbose_name_plural = "Locais"

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=75, unique=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['name']

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=75)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey('Location', on_delete=models.PROTECT, related_name="events")
    categories = models.ManyToManyField("Category", blank=True, related_name="events")

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
        ordering = ['start_date']

    def remaining_spaces(self):
        return self.location.capacity - self.registrations.count()

    def __str__(self):
        return self.title

class Activity(models.Model):
    title = models.CharField(max_length=100)
    speaker = models.CharField(max_length=75)
    schedule = models.TimeField()
    event = models.ForeignKey("Event", on_delete=models.CASCADE, related_name='activities')

    class Meta:
        verbose_name = "Atividade"
        verbose_name_plural = "Atividades"
        ordering = ['schedule']

    def __str__(self):
        return self.title

class Registration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    registrated_at = models.DateTimeField(auto_now_add=True)
    event = models.ForeignKey("Event", on_delete=models.CASCADE, related_name='registrations')

    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'

    def __str__(self):
        return self.name

class Report(models.Model):
    present = models.PositiveIntegerField()
    observations = models.TextField(null=True, blank=True)
    event = models.OneToOneField("Event", on_delete=models.CASCADE, related_name='report')

    class Meta:
        verbose_name = 'Relatório'
        verbose_name_plural = 'Relatórios'

    def __str__(self):
        return self.event
