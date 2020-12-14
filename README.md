# MS Azure Manager 📂

The reason for creating this script was simple - I am already using another script created by my friend [Reece](https://github.com/Reeceeboii/Batch-Compression) 
to automatically batch-compress all my images, optimising them for being displayed on my website. However, that solution still required me to upload those files
manually to my MS Azure blob storage, from where my Node backend was grabbing them and serving on [prutkowski.tech](https://prutkowski.tech).

This script automates a lot of the work for me, and gives me access to many Azure tasks from the comfort of my terminal.

## Usage 👨🏻‍💻

**Make sure Python 3 is installed and configured if you're using Windows - it comes preinstalled on most machines running macOS and Linux.** You can check your Python version by running `python -V`, and you might have to update it if necessary.

Before use, you have to configure your Azure account connection string as an environment variable in your system.
You can find it in your Azure portal by navigating to your _**storage account** -> **settings** -> **access keys**_, and copying _**"connection string"**_ under _**"key 1"**_ - they usually start with `DefaultEndpointsProtocol=https...`

```bash
$ export AZURE_CON_STR=<your_connection_string>

# check that the env var has been set
$ $AZURE_CON_STR
```
Remember to `source ~/.zshrc` or `source ~/.bashrc` after setting the environment variable in order for it to take effect. Alternatively you can kill your terminal instance and restart it. 

**You can at any time access information about all functions by running**
```bash
$ python am.py --help
```

### Upload files 🆙
In order to execute the script, you should include two arguments in the command - `container` and `path`.
The path can either be absolute or relative, and it is recommended to have your data folder in the same working directory for simplicity and less room for error.

```bash
$ python am.py upload <container_name> <file_path>

# example (this would grab the files from the "files" folder in the same working directory):
# └── src
#     ├── am.py
#     └── /files
$ python am.py upload container1 ./files
```

### List all blobs 🔍
To list all the blobs within a container, you'll need to gather a bit more information about your account than with the previous function.

What you'll need is:
- Your `account connection URI` - this can be found on the Azure portal under _**properties**_ -> _**primary endpoint**_
- Your `SAS` - can be generated from the Azure portal under _**shared access signature**_

The format of the command is as follows:

```bash
$ python am.py showall <acc_connection_uri> <container_name> <sas_token>
```

## Feature list 💭

- [x] Upload new blobs
- [x] List all blobs
- [ ] Download blobs
- [ ] Create/delete containers
- [ ] Delete blobs
