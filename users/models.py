from django.db import models


class User(models.Model):   #пользователь
    idUser = models.IntegerField(unique=True)
    email = models.EmailField(max_length=255, unique=True, null=False)
    bill = models.IntegerField()
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)


class Bet(models.Model):  #ставка
    idBet = models.IntegerField(unique=True)
    size = models.IntegerField(null=False)
    result = models.BooleanField(null=False)


class Fight(models.Model):  #бой
    idFight = models.IntegerField(unique=True)
    date = models.DateField(null=False)
    time = models.TimeField(null=False)
    boxer1 = models.TextField(max_length=255, null=False)
    boxer2 = models.TextField(max_length=255, null=False)

    def __str__(self):
        return 'Fight {}'.format(self.title)


class Boxer(models.Model):  #Боксёр
    idBoxer = models.IntegerField(unique=True)
    title = models.TextField(max_length=255)
    boxer_first_name = models.CharField(max_length=255, null=False)
    boxer_last_name = models.CharField(max_length=255, null=False)
