from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    joined_date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'club"."member'  # Specify schema and table name
        managed = False
