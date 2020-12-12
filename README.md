# MS Azure File Uploader 

The reason for creating this script was simple - I am already using another script created by my friend [Reece](https://github.com/Reeceeboii/Batch-Compression) 
to automatically batch-compress all my images, optimising them for being displayed on my website. However, that solution still required me to upload those files
manually to my MS Azure blob storage, from where my Node backend was grabbing them and serving on [prutkowski.tech](https://prutkowski.tech).

This script automates the upload process for me, optimising my workflow, and making uploading files easier and faster!

## Usage

**Make sure Python is installed and configured if you're using Windows - it comes preinstalled on most machines running macOS and Linux.**

Before executing, you have to configure your Azure account connection string as an environment variable in your system.
You can find it in your Azure portal by navigating to your **storage account** -> **settings** -> **access keys**, and copying **"connection string"** under **"key 1"**

```bash
$ export AZURE_CON_STR=<your_connection_string>

# check that the env var has been set
$ $AZURE_CON_STR
```
Remember to `source ~/.zshrc` or `source ~/.bashrc` after setting the environment variable in order for it to take effect. Alternatively you can kill your terminal instance and restart it. 

In order to execute the script, you should to include two arguments in the command - `container name` and `path to files`.
The path can either be absolute or relative, and it is recommended to have your data folder in the same working directory for simplicity and less room for error.

```bash
$ python uploader.py <container_name> <file_path>
# example (this would grab the files from the "files" folder in the same working directory):
$ python uploader.py container1 ./files
```


