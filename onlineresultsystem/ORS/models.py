from django.db import models

class User(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    loginId = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def to_json(self):
        data = {
            'id': self.id,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'loginId': self.loginId,
            'password': self.password
        }
        return data
    class Meta:
        db_table = "ORS_USER"

class developer(models.Model):
    developer_name=models.CharField(max_length=50)
    department=models.CharField(max_length=50)
    project=models.CharField(max_length=50)
    status=models.CharField(max_length=50)
    submitting_date=models.DateField()

    def to_developer(self):
        data = {
            'id': self.id,
            'developer_name': self.developer_name,
            'department': self.department,
            'project': self.project,
            'status': self.status,
            'submitting_date':self.submitting_date
        }
        return data
    class Meta:
        db_table = "ORS_developer"