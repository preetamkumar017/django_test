from django.db import models

class Institute(models.Model):
    domain_name = models.CharField(max_length=255, unique=True)
    database_name = models.CharField(max_length=255)
    database_user = models.CharField(max_length=255)
    database_password = models.CharField(max_length=255)
    database_host = models.CharField(max_length=255)
    database_port = models.CharField(max_length=10, default='5432')


    class Meta:
        db_table = 'config"."institute'  # Specify schema and table name
        managed = False

    def __str__(self):
        return self.domain_name
