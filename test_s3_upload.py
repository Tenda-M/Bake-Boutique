import os
from django.conf import settings
from django.core.files.base import ContentFile
from storages.backends.s3boto3 import S3Boto3Storage

def test_s3_upload():
    try:
        # Debugging
        print(f"STATICFILES_LOCATION in settings: {hasattr(settings, 'STATICFILES_LOCATION')}")
        print(f"STATICFILES_LOCATION value: {getattr(settings, 'STATICFILES_LOCATION', None)}")

        # Ensure the location matches your custom_storages setup
        static_storage = S3Boto3Storage(location=settings.STATICFILES_LOCATION)
        
        # Define a test file content and name
        file_content = ContentFile('This is a test upload for S3.')
        file_name = 'test_s3_upload.txt'  # Example file name
        
        # Save the file to S3
        file_path = static_storage.save(file_name, file_content)
        file_url = static_storage.url(file_path)
        
        print(f"Uploaded test file to: {file_url}")
    except Exception as e:
        print(f"An error occurred: {e}")

test_s3_upload()
