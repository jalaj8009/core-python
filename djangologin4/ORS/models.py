from django.db import models

# Create your models here.
class User(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    loginID = models.CharField(max_length=50)
    pass_word = models.CharField(max_length=50)

    # def to_json(self):
    #     data = {
    #         'id': self.id,
    #         'firstName': self.firstName,
    #         'lastName': self.lastName,
    #         'loginID': self.loginID,
    #         'password': self.pass_word
    #     }
    #     return data
    # class Meta:
    #     db_table = "SOS_USER"
