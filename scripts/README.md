# Scripts

## `data_acquisition.sh`

Shell script for downloading the data.

Run like this in a UNIX-like CLI:

```
# make sure your working directory is the base directory of this repo `RestAI`
# then run this command:
bash scripts/data_acquisition.sh
```

Requires a Kaggle account and API token. Here's how to set it up:

- Kaggle API is installed into your environment already when it's built using
the provided `environment.yaml` file

- If you do not have a Kaggle account, create one here: https://www.kaggle.com/.
If you have one, you can omit this step.

- You need a Kaggle API key. If you have one, you can omit this step and use
your existing key.
If you don't, set one up following these instructions:
Navigate to `Settings` > `API`.
Select `Create New Token`, and download it.
The token will be saved to a file called `kaggle.json`.

- Move this `kaggle.json` file to this directory: `~/.kaggle/`.
If you work on a UNIX-like operation system, one way to do so could look like
this: 

    - Open a new command line terminal.
    
    - Change directory to your downloads directory, e.g. like this:
    `cd ~/Downloads`

    - Run this command: `mv kaggle.json ~/.kaggle/kaggle.json` to move the file
    to the Kaggle directory.

    - Change permissions for the file, so it can be used by the Kaggle API like
    this: `chmod 600 ~/.kaggle/kaggle.json`

    Now, you should be able to use the Kaggle API to download data and to run
    this data acquisition script without errors.

- To test the installation, either run the script or one of these commands:

    - `kaggle -v`: you should get somthing comparable to `Kaggle API 1.6.17`
    
    - `which kaggle`: you should get a valid path corresponding to the location
    of your installation of Kaggle API

### Alternative Method for Data Acquisition

All data sets are tracked in this Git repository, as none of the files exceeds a
total sizes of 200 kB. It's small data.

Still, here are alternative methods for downloading the data yourself:

For all data sets, the source is provided via a link.
Follow the link to Kaggle, and click `Download` in the top right corner.
There is a range of different options for downloading the data.
Choose your preferred one.
I considered the Kaggle API to be the most comfortable one.
For others, the easiest way may be just manually downloading the data, and 
moving the files to the cloned repository.

## `train.py`

- Train the final model (model selection was done in notebook
`02-train_evaluate_compare_models.ipynb`)
- Save final model to a pickle file

Run like this:
```bash
# if current working directory is repo root "RestAI"
python scripts/train.py

# if current working directory is scripts direcory "RestAI/scripts"
python train.py
```

## `predict.py`

- Load the final model (model was trained in script `train.py`)
- Serve it via the web service Flask
