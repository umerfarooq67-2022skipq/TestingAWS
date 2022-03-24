# Sprint 1

In sprint1, we create Clodu9 instance and write hello World Lambda function.

## Installation

Login to aws console. Search Cloud9 service and create new instance with ubuntu platform. Check python version if it's below 3 then set alias to python3
in .bashrc file.

Open .bashrc in vim and add alias command.

```bash
vim ~/.bashrc
alias python='/usr/bin/python3'
```
To re-read .bashrc use following command.

```bash
source ~/.bashrc
```
Update Python CLI version to latest with these commands.

```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

Create new folder for the project and cd into the folder. Use following commands to initialize the project folder with cdk.

```bash
cdk init app --language python
source .venv/bin/activate
python -m pip install aws-cdk-lib==2.10.0
python -m pip install -r requirements.txt
nvm install v16.3.0 && nvm use 16.3.0 && nvm alias default v16.3.0
npm install -g aws-cdk
export PATH=$PATH:$(npm get prefix)/bin
.venv/bin/pip3.6 install -r requirements.txt
```

Now our project is ready and we need to create our first lambda function.

Create a resource folder and create new file with name HWLambda.py. This file will be our resource file for lambda function.

Now we will define our hello world lambda even handler in this file.

```bash
def lambda_handler(event,context):
    return 'Hello {} {} !'.format(event['first_name'],event['last_name'])
```

In stack file, we created our lambda function.

```bash
def create_lambda(self,id,asset,handler):
        return lambda_.Function(
            self,
            id=id,
            code=lambda_.Code.from_asset(asset),
            handler=handler,
            runtime=lambda_.Runtime.PYTHON_3_6)
```

To deploy lambda function, use these commands.

```bash
cdk synth
cdk deploy
```

Our lambda function has been deployed. To test it, open dashboard and go to function. Search your function in the list and open it.
Click on the test button and create test cases as json file.

```bash
{
    "first_name":"MyFirstName",
    "last_name":"MyLastName"
}

```

Click on test button and lambda will execute.


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[SkipQ](https://skip.org)