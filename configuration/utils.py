from django.db import connections
from django.conf import settings

def get_database_connection(domain_name):
    # Fetch database details from Master DB
    from .models import Institute  # Ensure the model path is correct
    try:
        institute = Institute.objects.get(domain_name=domain_name)
    except Institute.DoesNotExist:
        raise ValueError(f"No Institute found with domain name {domain_name}")
    
    # Define default database options
    default_options = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': institute.database_name,
        'USER': institute.database_user,
        'PASSWORD': institute.database_password,
        'HOST': institute.database_host,
        'PORT': institute.database_port,
        'OPTIONS': {},  # Ensure OPTIONS is included
        'TIME_ZONE': 'Asia/Kolkata',  # Set a valid time zone
        'CONN_MAX_AGE': 600,  # Connection persistence duration in seconds
        'CONN_HEALTH_CHECKS': False,  # Disable health checks if not needed
        'ATOMIC_REQUESTS': False,  # Explicitly set this to False or True based on your requirements
         'AUTOCOMMIT': True,        # Add this key explicitly

    }

    # Add the new database connection dynamically
    if institute.database_name not in settings.DATABASES:
        settings.DATABASES[institute.database_name] = default_options
    
    # Return the database connection
    return connections[institute.database_name]
