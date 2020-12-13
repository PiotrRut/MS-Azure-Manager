import os
import sys

from azure.storage.blob import BlobServiceClient, ContentSettings


def upload_all():
    # Initialize the connection to Azure storage account
    blob_service_client = BlobServiceClient.from_connection_string(os.getenv('AZURE_CON_STR'))
    image_content_setting = ContentSettings(content_type='image/jpeg')
    # Go through all files in provided directory
    all_files = [f for f in os.listdir(sys.argv[2])]
    for file in all_files:
        blob_client = blob_service_client.get_blob_client(container=sys.argv[1], blob=file)
        with open(os.path.join(sys.argv[2], file), "rb") as data:
            # Upload all files to Azure
            blob_client.upload_blob(data, content_settings=image_content_setting)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        exit("Please provide the name of your container name as first argument, and the path to your folder as "
             "second.\nThe correct format is: 'uploader.py <container> <path>'")
    else:
        print("Starting upload")
        upload_all()
        print(f"All files successfully uploaded to {sys.argv[1]} container")
