from django.db import models
from django.conf import settings
from phone_field import PhoneField
from django.utils import timezone

#I understand why this array may be important, but why is it in the tables file? (Initially) - LG
# I see your use of it in a model, but I don't believe that this hardcode is necessary. Appropriate for application features, but for scalability & clean code there is another solution - LG
WEEKDAYS = [
  (1, ("Monday")),
  (2, ("Tuesday")),
  (3, ("Wednesday")),
  (4, ("Thursday")),
  (5, ("Friday")),
  (6, ("Saturday")),
  (7, ("Sunday")),
]

# Create your models here.
class Usertype(models.Model):
    name = models.CharField(max_length=128)
    def __str__(self):
        return self.name

class ArtArea(models.Model):    
    name = models.CharField(max_length=128)
    def __str__(self):
         return self.name

class Tutor(models.Model):
    skill = models.ForeignKey(ArtArea, on_delete=models.CASCADE)
    weekday = models.IntegerField(
        choices=WEEKDAYS,
        unique=True
    )
    from_hour = models.TimeField()
    to_hour = models.TimeField()
    def __str__(self):
        return self.skill.name
    # def __str__(self):
    #     return self.skill

class Household(models.Model):
    participant_first_name = models.CharField(max_length=128)
    participant_last_name = models.CharField(max_length=128)
    participant_relationship = models.CharField(max_length=128)
    hospital_id = models.IntegerField()
    birthday = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        string = self.participant_last_name + " (" + self.participant_relationship +")"
        # string = self.participant_last_name
        return string

class User(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(blank=True, unique=True)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    user_type_id = models.ForeignKey(Usertype, on_delete=models.CASCADE)
    tutor_id = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    household_id = models.ForeignKey(Household,on_delete=models.CASCADE)
    def __str__(self):
        return self.first_name

class Program(models.Model):
    name = models.CharField(max_length=128)






