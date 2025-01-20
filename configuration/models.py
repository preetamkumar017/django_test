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



class InternalUser(models.Model):
    institute_id = models.IntegerField()
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255, null=True, blank=True)
    suspended = models.BooleanField(default=False)
    created_by = models.IntegerField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_by = models.IntegerField(null=True, blank=True)
    modified_on = models.DateTimeField(auto_now=True)
    password_changed_on = models.DateField(null=True, blank=True)
    created_by_type = models.CharField(max_length=255, null=True, blank=True)
    modified_by_type = models.CharField(max_length=255, null=True, blank=True)
    security_ques = models.CharField(max_length=255, null=True, blank=True)
    security_ques_ans = models.CharField(max_length=255, null=True, blank=True)
    consecutive_failed_attempt = models.IntegerField(null=True, blank=True)
    last_failed_attempt_on = models.DateTimeField(null=True, blank=True)

    # Custom Primary Key
    class Meta:
        unique_together = ('institute_id', 'username')
        db_table = 'framework"."internal_user'  # Specify schema and table name
        managed = False


    def __str__(self):
        return f'{self.username} (Institute ID: {self.institute_id})'
        
    def increment_failed_attempts(self):
        self.consecutive_failed_attempt += 1
        self.last_failed_attempt_on = timezone.now()
        self.save()

    def reset_failed_attempts(self):
        self.consecutive_failed_attempt = 0
        self.save()

    def is_account_suspended(self):
        return self.suspended
