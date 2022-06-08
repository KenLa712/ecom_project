import email
from django.db import models
from sqlalchemy import ForeignKey
from django.contrib.auth.models import User

class Kunde(models.Model):
    vorname = models.CharField(max_length=200, null=True)
    nachname = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)
    adresse = models.CharField(max_length=200)
    
    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = "1. Kunden"

class Bestellung(models.Model):
    bestelldatum = models.DateTimeField(auto_now_add=True)
    bestellsumme = models.FloatField(null = False)
    kunde = models.ForeignKey(Kunde, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = "2. Bestellungen"

class Zahlung(models.Model):
    summe = models.FloatField()
    zahlungsart = models.CharField(max_length=100, null=False)
    zahlungsdatum = models.DateTimeField()

    def __str__(self):
        return str(self.id)

class Produkt(models.Model):
    name = models.CharField(max_length=200)
    preis = models.FloatField()
    kategorie = models.CharField(max_length=200)
    produktbild = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.produktbild.url
        except:
            url = ''
        return url 
    
    class Meta:
        verbose_name_plural = "3. Produkte"

class Warenkorb(models.Model):
    zwischensumme = models.FloatField(null=True)
    kunde = models.ForeignKey(Kunde, on_delete=models.SET_NULL, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "5. Warenkörbe"

class WarenkorbProdukt(models.Model):
    warenkorb = models.ForeignKey(Warenkorb, on_delete=models.SET_NULL, null=True, blank=True)
    produkt = models.ForeignKey(Produkt, on_delete=models.SET_NULL, null=True)
    anzahl = models.IntegerField()

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = "4. Warenkorbprodukte"

class BestellungProdukt(models.Model):
    warenkorb = models.ForeignKey(Bestellung, on_delete=models.SET_NULL, null=True, blank=True)
    produkt = models.ForeignKey(Produkt, on_delete=models.SET_NULL, null=True)
    anzahl = models.IntegerField()

    def __str__(self):
        return str(self.id)