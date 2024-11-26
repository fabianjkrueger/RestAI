<div align="center">
    <img src="images/logo.png" width="100%">
</div>

# 🌚 It's been a long day, traveller... you should take a Rest! 😴

Ever caught yourself doom-scrolling at 2 AM, knowing you'll regret it tomorrow? Yeah, me too. In our always-on world, sleep often takes a back seat to, well, everything else. Yet ironically, while we're all chasing productivity and self-improvement, we're missing out on sleep - the ultimate performance enhancer.

That's where RestAI comes in. It's a simple tool that predicts how well you might sleep based on your daily habits. Just plug in some basic info about your day - things like caffeine intake, screen time, and physical activity - and it'll give you a heads-up about your potential sleep quality.

No fancy sleep trackers or complicated apps. Just straightforward feedback to help you make better choices throughout your day. Because sometimes, knowing the impact of that late-night coffee or extra Netflix episode is all we need to make smarter decisions.
Sweet dreams! 🌙


## Technical Description

This project was made as midterm project for DataTalk ML-Zoomcamp 2024.
An Extra Trees Regressor was trained on a synthetic data set
(test size: n = 400) about sleep quality.
Variables include things like caffeine intake, typical bedtime,
wakeup time or physical activity.
Output is a score between 0 (worst sleep) and 1 (best sleep)

Disclaimer: This project was done for training purposes.
Unfortunately, the data used here was synthetic, and its size was
too low to produce reliable results.
Please do not rely on any recommendations made by the algorithm.
This is not sleep advice. Have fun exploring the project 💚

# Usage

## Get the Code

Clone the repository and change working directory.

```
git clone https://github.com/fabianjkrueger/RestAI.git
cd RestAI
```

## Get the Dependencies

Build a virtual environment identical to mine in Conda based on
the `environment.yaml` file.

You need to have conda installed to do this.

```bash
# create conda environment
conda env create -f environment.yaml

# activate conda environment
conda activate RestAI
```

## Query the Model

The model can be queried when deployed
using flask as well as docker.
Just choose one of both.

To make this work, you first have to start the application.
Make sure your current working
directory is the base directory of this repository: `RestAI/`.
Now run one of the two provided commands.

Then you can query the model using the
code in the notebook `03-inference_flask_localhost.ipynb`.
It contains instructions for querying the model.
You can easily exchange the examples for
your own queries.

#### Flask

```bash
# start application
python scripts/predict.py
```

#### Docker

```bash
# build the image
docker build -t restai .

# run the container
# -p maps host port to container port (host:container)
docker run -p 9696:9696 restai
# if that doesn't work (may happen if you use bash instead of zsh, run:)
# docker run -p 9696::9696 restai
```

## Reproduce the Project

This is the pipeline of the strictly necessary steps:


0. Clone repository using `git clone https://github.com/fabianjkrueger/RestAI/``
1. Create and activate environment according to instructions in `Get the Dependencies`.
2. Acquire data if it should not be available in this repo. Otherwise, find it in `data/`.
3. Run notebook `01-data_preparation.ipynb` to prepare and save data.
4. Run script `python scripts/train.py` to train the final model.
5. To query the model, host it according to instructions in `Query the Model`,
then open
notebook `03-inference_flask_localhost.ipynb` to find code 
and ready to use examples.