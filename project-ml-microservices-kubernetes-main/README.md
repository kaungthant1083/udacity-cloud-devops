[![CircleCI](https://dl.circleci.com/status-badge/img/circleci/AejTxv7BTjrkxuT1BSh6bo/KAn4HrEH2fSeVWrHz39X6z/tree/main.svg?style=svg&circle-token=5d25a2ed83a6e0477b613d8621f9c7fa2e9ed878)](https://github.com/kaungthant1083/udacity-cloud-devops)

## Project Overview

In this project, you will apply the skills you have acquired in this course to operationalize a Machine Learning Microservice API. 

You are given a pre-trained, `sklearn` model that has been trained to predict housing prices in Boston according to several features, such as average rooms in a home and data about highway access, teacher-to-pupil ratios, and so on. You can read more about the data, which was initially taken from Kaggle, on [the data source site](https://www.kaggle.com/c/boston-housing). This project tests your ability to operationalize a Python flask app—in a provided file, `app.py`—that serves out predictions (inference) about housing prices through API calls. This project could be extended to any pre-trained machine learning model, such as those for image recognition and data labeling.

### Project Tasks

Your project goal is to operationalize this working, machine learning microservice using [kubernetes](https://kubernetes.io/), which is an open-source system for automating the management of containerized applications. In this project you will:
* Test your project code using linting
* Complete a Dockerfile to containerize this application
* Deploy your containerized application using Docker and make a prediction
* Improve the log statements in the source code for this application
* Configure Kubernetes and create a Kubernetes cluster
* Deploy a container using Kubernetes and make a prediction
* Upload a complete Github repo with CircleCI to indicate that your code has been tested

You can find a detailed [project rubric, here](https://review.udacity.com/#!/rubrics/2576/view).

**The final implementation of the project will showcase your abilities to operationalize production microservices.**

---

## Setup the Environment

* Create a virtualenv with Python 3.7 and activate it. Refer to this link for help on specifying the Python version in the virtualenv. 
```bash
python3 -m pip install --user virtualenv
# You should have Python 3.7 available in your host. 
# Check the Python path using `which python3`
# Use a command similar to this one:
python3 -m virtualenv --python=<path-to-Python3.7> .devops
source .devops/bin/activate
```
* Run `make install` to install the necessary dependencies

### Running `app.py`

1. Standalone:  `python app.py`
2. Run in Docker:  `./run_docker.sh`
3. Run in Kubernetes:  `./run_kubernetes.sh`
4. Make predictions on our app : `./make_prediction.sh`

### Publish Docker Image 

* Push : `./upload_docker.sh`

### Kubernetes Steps

* Setup and Configure Docker locally
    > https://docs.docker.com/engine/install/

* Setup and Configure Kubernetes locallly
    * We will use minikube to run k8s and follow this tutorial to run minikube. 
    > https://kubernetes.io/vi/docs/tasks/tools/install-minikube/

* Create Flask app in Container
    * Create Dockerfile that will build our app.py to become container. You can check Dockerfile for details

* Run via kubectl
    > kubectl run udacity-ml --image=<your image> --port=80

### Files Included

* `.circleci` - circleci config scripts for cicd
* `output_txt_files` - project output files (docker, kubernetes)
    * `docker_out.txt` - run_docker.sh output
    * `kubernetes_out.txt` - run_kubernetes.sh output
    * `kubernetes.out.txt` - make_prediction.sh output while running k8s pod
* `app.py` - python web application entry point file
* `Dickerfile` -  For building docker image
* `make_prediction.sh` - Script for making prediction HTTP call
* `Makefile` - make file (install, test, lint steps)
* `requirements.txt` - web application dependencies (python, libraries)
* `run_docker.sh` - Script for running docker container
* `run_kubernetes.sh` - Script for running kubernetes pod for the web app
* `upload_docker.sh` - Script for uploading docker image to dicker hub

