from django.db import models

class Film(models.Model):
    назва_фільму = models.CharField(max_length=255)
    жанр = models.CharField(max_length=50)
    тривалість = models.IntegerField()
    рейтинг = models.FloatField()

class Cinema(models.Model):
    назва_кінотеатру = models.CharField(max_length=255)
    ціни_на_квитки = models.FloatField()
    кількість_місць = models.IntegerField()
    адреса = models.CharField(max_length=255)
    телефон = models.CharField(max_length=15)

class FilmScreening(models.Model):
    код_фільму = models.ForeignKey(Film, on_delete=models.CASCADE)
    код_кінотеатру = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    дата_початку_показів = models.DateField()
    термін_показу = models.IntegerField()
