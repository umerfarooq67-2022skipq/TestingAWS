# SkipQ - Cohort Orions
# AWS CDK Sprint 1
## Intro
This project is about learning the basics of CDK in python. I set up the cloud9 IDE for CDK. Install dependencies and deploy a simple Lambda function to print Hello World in the AWS platform.

## Lambda Function (Hello World)
Lambda is a serverless function that is mainly used for tasks that might take at most 15 mins to fetch/send or process data.
- Uploading file
- Sending message.
- HTTP Requests to view data.
- Sending Sensor data for analysis.

## Steps
- Sign in to AWS.
- Install Cloud9 Instance. (t2 micro, 1GB RAM, and 15GGB EBS Volume but the more the space the better.)
- Update Python from 2.7 to 3.x. Use Amazon Linux 2 to avoid this step.
- Install cdk-aws-lib to create stacks that provide APIs to define your CDK application and add CDK constructs to the application.
- Install aws-cdk toolkit using npm that provides the cdk command-line interface that can be used to work with AWS CDK applications.
- Install the libraries from requirements in the virtual environment.
- Update aws-cdk-lib to version 2.x.
- Create a sample stack.
- Write your lambda function that return's Hello World.
- Setup stack in stack.py to deploy Lambda on Aws. Note: The name of this file depends on the folder you are in.
- Synthesize the CDK App
- Deploy it.


## Requirements
Install below dependencies to write and deploy CDK apps:

- Install Python 3.x.x (3.7)
- Upgrade AWS CLI version to 2.x.x
- Install requirements.
- Install aws-cdk


## Installation
```sh
1. fork repository
2. git clone https://github.com/username/repo_name.git
3. Enter GitHub username
4. Enter access token from GitHub.
```

### For Only Python 2.x.x to 3.x.x
```sh
1. vim ~/.bashrc
2. press "i" to insert
3. copy at the end of file [alias python='/usr/bin/python3'] (without brackets)
4. Esc
5. Enter :wq
6. source ~/.bashrc
6. which python (to test python version)
```

### Install Required Dependencies/Packages
```sh
1. mkdir folder_name (sprint1) : Can be any name.
2. cd sprint1
3. cdk init app --language python
4. source .venv/bin/activate
5. vm install v16.3.0 && nvm use 16.3.0 && nvm alias default v16.3.0
6. .venv/bin/pip3.6 install -r requirements.txt
7. npm install -g aws-cdk
8. export PATH=$PATH:$(npm get prefix)/bin
```

### Setup Stack for Lambda Function
```sh
1. cd sprint1 (your folder name where you init your CDK app). Note your stack folder will be sprint1 and the stack file will be sprint1_stack if the folder name is sprint1
2. source .venv/bin/activate
3. mkdir lib folder && cd lib (to store lambda functions).
4. vim HWLambda.py
5. Press "i" to write code.

-> def handleHelloWorldHandler(event, context):    
->    return "Hello World {} {}".format(event['first_name'], event['last_name'])

6. cd ..
8. Open app.py
7. Insert Tags e.g. cdk.Tags.of(app).add("Cohort","Your Cohort Name") and cdk.Tags.of(app).add("Name","Enter your name here") after app = cdk.App()
8. Give a unique ID to stack STACK_NAME(app, "Unique Stack Id"). Do not change STACK_NAME. It is imported.
8. Open stack folder (sprint1) and open stack file as sprint1_stack.py
9. Import this module -> from aws_cdk import (Stack, aws_lambda as lambda_)
10. Import this module -> from constructs import Construct
11. Create a configuration for lambda function we create previously.

-> lambda_method = lambda_.Function(
->           self,
->           id = ID_OF_LAMBDA_FUNCTION,
->           handler = OUR_LAMBDA_FUNCTION_NAME,
->           code = lambda_.Code.from_asset(PATH_OF_LIB_FOLDER),
->           runtime = lambda_.Runtime.PYTHON_3_7)

11. cdk synth
12. cdk diff (see the changes).
13. cdk deploy
14. Enter y
15. Go to Cloudformation to deployment status.
16. Go to Lambda Function Managment Console to test the lambda function.
```


## Contribute

Want to contribute and support. 
Join SkipQ.

SkipQ provides a platform that helps tech geeks to excel in practical skills. Learn DevOps and MERN Stack from the best experts to skip the queue of jobs.

Fork the project in your account and play with it.
## License
SkipQ



# Welcome to your CDK Python project!

This is a blank project for Python development with CDK.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
