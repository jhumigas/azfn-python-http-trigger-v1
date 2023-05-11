# README

** ARCHIVE **

Template of azure function  project using poetry.
With this, you have a basic structure with azure functions using a python project.
This was developped using [python programming model V1](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-python?pivots=python-mode-configuration&tabs=asgi%2Capplication-level#programming-model).

## Pre-requisities

Make sure you have:

* Python 
* Poetry (installation instructions [here](https://python-poetry.org/docs/#installation))
* Docker container manager (use [colima](https://github.com/abiosoft/colima#installation) for macOs)

Optional:

If you are using Code as your Code editor you can install the following extensions:
* [Durable Functions Monitor](https://marketplace.visualstudio.com/items?itemName=DurableFunctionsMonitor.durablefunctionsmonitor)

## Setup local env

You can run:

```sh
make init-env-file # Copy default ./docker/template.env to ./docker/.env

make setup # Install project dependencies
```

You can then run an orchestration for demonstration purpose by doing the following:

```sh
colima start # Start docker service if you are using colima
make start-dev # Build python bundle, build docker and starts it
make check-up-azfn # To check if azure function hub is up and running
```

At this point you can monitor the orchestration using the azure functions monitor vscode extension.
The connection string should be: 
```
DefaultEndpointsProtocol=http;AccountName=localstoreaccount;AccountKey=key1;BlobEndpoint=http://localhost:10000/localstoreaccount;QueueEndpoint=http://localhost:10001/localstoreaccount;TableEndpoint=http://localhost:10002/localstoreaccount;
```

Then to trigger an http azure function, do the following:

```sh
curl http://localhost:8080/api/orchestrator
```

When you are done, you can run:

```sh
make stop-dev    # Shut down the docker containers
```

## Run tests

For unit tests
```sh
make run-unit-tests # Check if unit tests work
```

For integration tests:

```sh
make start-dev # To get local env running
make check-up-azfn # To check if azure function hub is up and running
make run-integration-tests
make stop-dev # To shutdown local env 
```

### Build and deploy 

The build stage goal is to create an artifact that contains the azure functions source code and the python project.
For that we need to:
* Build the python bundle using poetry, which will create wheel
* Copy the bundle in a custom folder in the azure function folder i.e `{function apps folder}/.python_packages/lib/site-packages`
* Zip the function_apps folder which will create the final artifact

See `./github/workflows/build.yml`

The deploy stage is just about uploading the artifact to the function apps azure resource.

See `./github/workflows/deploy.yml`

### Project structure

```
.
├── README.md              <- The top-level README for developers using this project.
├── Makefile               <- Makefile with commands like `make setup` to install the project
├── .github                <- Github actions and workflows configurations for CI/CD
│   ├── actions
│   │   └── setup-python-env      <- Action for python environment setup
│   └── workflows
│       ├── build.yml             <- Build workflow to produce to the function apps artifact
│       ├── check-quality.yml     <- Workflow quality gate
│       ├── check-security.yml    <- Workflow security gate
│       ├── deploy.yml            <- Deployment gate
│       ├── orchestrate_ci_cd.yml <- Main workflow for the full CI/CD
│       └── run-tests.yml         <- Workflow for tesy gate
├── .pre-commit-config.yaml
├── docker                 <- Docker Configuration to run a local environment           
│   ├── Dockerfile         <- Dockerfile for the python azure function
│   ├── docker-compose.yml <- configuration of the containers used for the project
│   ├── template.env       <- Template of .env file to use for docker configuration
│   └── wait-azfn.sh       <- Script to check if the azure function is up and running
├── function_apps          <- Folder containing all the azure functions
├── py_project             <- Python project to import in azure functions
├── pyproject.toml         <- Build poetry configuration holding dependencies and tools configurations
├── poetry.lock
└── tests                  <- Tests
    ├── integration
    └── unit
```

### References

* [Azure functions docker python sample](https://github.com/Azure/azure-functions-docker-python-sample)

