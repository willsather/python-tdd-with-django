from django.db import models


class Penguin(models.Model):
    class Sex(models.TextChoices):
        MALE = 'male'
        FEMALE = 'female'
        NA = 'NA'

    island = models.CharField(max_length=50)
    sex = models.CharField(max_length=6, choices=Sex.choices, default='NA')
    bill_length_mm = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)
    bill_depth_mm = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)
    flipper_length_mm = models.IntegerField(default=0)
    body_mass_g = models.IntegerField(default=0)

    def formatted_data(self):
        return {'bill_length_mm': self.bill_length_mm, 'bill_depth_mm': self.bill_depth_mm,
                'flipper_length_mm': self.flipper_length_mm, 'body_mass_g': self.body_mass_g,
                'island_Dream': self.island == 'Dream', 'island_Torgersen': self.island == 'Torgersen',
                'sex_male': self.sex == 'MALE'}
