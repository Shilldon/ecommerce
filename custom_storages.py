from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

# this class deals with where static files will be saved on S3
class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION
    
# this class will deal with where media files will be saved on S3

class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION 

    