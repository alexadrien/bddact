from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=2)


class Currency(models.Model):
    name = models.CharField(max_length=3)
    countries_available = models.ManyToManyField(Country)


# class CountryCurrency(models.Model):
#     country = models.ForeignKey(Country, on_delete=models.CASCADE)
#     currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
#     is_allowed = models.BooleanField()


class User(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    favorites_currencies = models.ManyToManyField(Currency)


# class UserCurrency(models.Model):
#     currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     is_favorite = models.BooleanField()


class OrderType(models.Model):
    name = models.CharField(max_length=4)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.ForeignKey(OrderType, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    amount = models.FloatField()
    target_rate = models.FloatField()


class Tax(models.Model):
    country_1 = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country_1')
    country_2 = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country_2')
    rate = models.FloatField()


