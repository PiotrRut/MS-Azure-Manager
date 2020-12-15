import argparse
import sys

# Help options
parser = argparse.ArgumentParser \
    (description='Welcome to MS Azure Manager!\nThis program allows you to perform '
                 'several actions with your MS Azure storage account. See available '
                 'options below:', usage="am.py [-h | --help] [cc | dc | upload | list | download | download]")


def show_help():
    parser.add_argument('cc', help="Create container - am.py cc <container_name>")
    parser.add_argument('dc', help="Delete container - am.py dc <container_name>")
    parser.add_argument('lc', help="List all containers - am.py lc")
    parser.add_argument('upload', help="Batch upload blobs - am.py upload <container_name> <file_path>")
    parser.add_argument('list', help="List all blobs - am.py list <acc_connection_uri> <container_name> <sas_token>")
    parser.add_argument('download', help="Download all blobs - am.py download <acc_connection_uri> "
                                         "<container_name> <sas_token>")
    parser.add_argument('download', help="Download only one blob - am.py download <acc_connection_uri> "
                                         "<container_name> <sas_token> <blob_name>")

    if len(sys.argv) == 2 and not sys.argv[1] == 'lc':
        parser.print_help()
