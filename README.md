[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/xnURI3fj)
# Homework 1 (2024)

submit before 11:59pm Friday May 17th 2024

# Instructions

1. Accept the assignment: [https://classroom.github.com/a/xnURI3fj](https://classroom.github.com/a/xnURI3fj) (you already did this)


2. Clone repository locally (recommended):
```
git clone git@github.com:WeizmannMLcourse/homework1-2024-<GIT-USERNAME>-<POSSIBLE-SUFFIX>.git
cd homework1-2024-<GIT-USERNAME>-<POSSIBLE-SUFFIX>
```
(you can also use Google colab: [see this link](https://bebi103a.github.io/lessons/02/git_with_colab.html))

3. Complete the missing code in `model.py`
4. Run `homework_1.ipynb` to download the train and validation datasets
5. Train your model using the loop in the notebook. Note: you should aim to achieve >55% accuracy on the validation dataset. You can check this in the notebook or by doing:
```
python evaluate.py galaxy_val.h5
```
6. Commit/upload the files (not your datasets) back to original repository:
```
git add model.py trained_model.pt
git commit -m "My attempted solution"
git push origin main
```
(you can also do this step using your editor, e.g. VSCode, if supported)

7. On the GitHub page of your repository, you can watch the autograding run each time you make a new commit. It will determine whether you passed by evaluating your model on a separate test dataset and checking for accuracy >55%. You can make commits up until the deadline and the autograding should rerun each time (contact us if there's any issue).
