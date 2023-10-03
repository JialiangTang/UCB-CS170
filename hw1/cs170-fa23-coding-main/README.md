# CS 170 Fall 2023 Coding Notebooks
Coding Jupyter Notebooks for Fall 2023 Iteration of CS 170

## Instructions for initial local setup

1. Install Anaconda following the instructions [here](https://www.anaconda.com/products/distribution).
2. Open up your terminal.
3. Create a conda environment (with python 3.8):
```
conda create -n cs170 python=3.8
```
4. Activate the environment:
```
conda activate cs170
```
5. Install pip:
```
conda install pip
```
6. Install jupyter:
```
conda install jupyter
```
7. Clone this repository somewhere in your device:
```
git clone https://github.com/Berkeley-CS170/cs170-fa23-coding
```
8. Once you're done, deactivate the conda environment to return to your default environment:
```
conda deactivate
```
9. Yay you're done with local setup!

## Instructions for completing each coding homework

1. Make sure that you've completed the initial local setup above. 
2. Open up your terminal
3. `cd` into your specific coding homework directory, e.g.:
```
cd <wherever your homework lives>/cs170-fa23-coding/hw01
```
4. Activate the `cs170` conda environment you created during initial local setup:
```
conda activate cs170
```
5. Install all python package requirements for that homework:
```
pip install -r requirements.txt
```
If there isn't a `requirements.txt` file in the coding homework directory, you can skip this step.

6. Start up a local jupyter notebook server by running
```
jupyter notebook
```
7. Navigate to the jupyter notebook for the assignment and complete it! Good luck :D
8. Yay you finished your coding homework for the week! Once you're done, submit your completed `.ipynb` file to Gradescope, and if you want, deactivate the conda environment to return to your default environment:
```
conda deactivate
```