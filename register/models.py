from django.db import models


# Create your models here.
payment_OPTIONS = (
    ('semestralnie', 'Semestralnie'),
    ('za każde zajęcia', 'Za każde zajęcia'),
)
swietlica_OPTIONS = (
    ('tak', 'Tak'),
    ('nie', 'Nie'),
)


class ContactModel(models.Model):
    child_name = models.CharField(max_length=100, blank=False, null=False)
    child_class = models.CharField(max_length=20, blank=False, null=False)
    parent_name1 = models.CharField(max_length=100, blank=False, null=False)
    parent_name2 = models.CharField(max_length=100, blank=True)
    parent_phone_number1 = models.CharField(max_length=20, blank=False, null=False)
    parent_phone_number2 = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)

    swietlica = models.CharField(
        max_length=20,
        choices=swietlica_OPTIONS,
        blank=False
    )

    payment = models.CharField(
        max_length=20,
        choices=payment_OPTIONS,
        blank=False
    )

    def __str__(self):
        return f"{self.child_name} {self.parent_name1} {self.child_class}"
