import argparse
import sys

# Help options
parser = argparse.ArgumentParser \
    (description='Welcome to MS Azure Manager!\nThis program allows you to perform '
                 'several actions with your MS Azure storage account. See available '
                 'options below: ', usage='am.py [-h] <options>')


def show_help():
    upload_blobs_help = parser.add_argument_group('Option 1: "am.py upload <container_name> <path_to_folder>"',
                                                  'Upload all blobs in '
                                                  'folder to your chosen container')
    upload_blobs_help.add_argument('container_name', help='Name of your container')
    upload_blobs_help.add_argument('path_to_folder', help='Path to folder containing your files')

    list_blobs_help = parser.add_argument_group('Option 2: "am.py showall <acc_connection_uri> <container_name> '
                                                '<sas_token>"', 'Show all blobs currently stored in your chosen '
                                                'container.')
    list_blobs_help.add_argument('acc_connection_uri', help='Your Azure connection URI')
    list_blobs_help.add_argument('container_name', help='Name of your container')
    list_blobs_help.add_argument('sas_token', help='Your Azure SAS token')

    if len(sys.argv) == 2:
        parser.print_help()