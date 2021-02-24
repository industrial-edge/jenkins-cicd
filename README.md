# CI/CD pipelines with Jenkins 

Automate process of uploading apps to IEM with Jenkins.

- [CI/CD pipelines with Jenkins](#cicd-pipelines-with-jenkins)
  - [Description](#description)
    - [Overview](#overview)
    - [General task](#general-task)
  - [Requirements](#requirements)
    - [Prerequisites](#prerequisites)
    - [Used components](#used-components)
  - [Installation steps](#installation-steps)
  - [Documentation](#documentation)
  - [Contribution](#contribution)
  - [Licence & Legal Information](#licence--legal-information)

## Description

###  Overview
This application example shows how to create Jenkins CI/CD pipelines to automatically upload applications to Industrial Edge Management system.

### General task
The main goal of this example is to show how to setup Jenkins server and create Jenkins pipelines to upload applications to IEM. Jenkins can be integrated with several Git providers but GitHub is used for this example. With GitHub webhook feature it is possible on every commit to the GitHub repository to automatically trigger Jenkins pipeline on a Jenkins server that build, test and upload application to IEM. 

<img src="./docs/graphics/overview.png" width="700"/>

## Requirements

###  Prerequisites

- Installed Industrial Edge Management
- VM (will be used for Jenkins) with docker and docker-compose installed
- VM has connection to IEM


### Used components

- Industrial Edge Device V 1.1.0-39
- Industrial Edge Management V 1.1.11
- VM - Ubuntu 20.04
- Docker 19.03.13
- Jenkins 2.263.3


## Installation steps
The repository is divided into two main directories. The [docs](./docs) folder contains documentation that describes the necessary steps for installation and implementation. The documentation for the installation steps of the Jenkins server can be found [here](./docs/installation.md). The documentation for creating Jenkins pipeline using either docker or shell script can be found [here](./docs/pipeline.md). It describes the process of connecting GitHub repository with Jenkins using webhooks and creating Jenkins pipelines to automatically upload app to IEM on every code changes push. The folder is extended by documentation describing implementation of the pipelines which can be found [here](./docs/pipeline.md)


The [src](./src) folder consist source code of Jenkins pipeline implementation using either shell script or docker. 

## Documentation

- You can find further documentation and help in the following links
  - [Industrial Edge Hub](https://iehub.eu1.edge.siemens.cloud/#/documentation)
  - [Industrial Edge Forum](https://www.siemens.com/industrial-edge-forum)
  - [Industrial Edge landing page](https://new.siemens.com/global/en/products/automation/topic-areas/industrial-edge/simatic-edge.html)
  
## Contribution
Thanks for your interest in contributing. Anybody is free to report bugs, unclear documentation, and other problems regarding this repository in the Issues section or, even better, is free to propose any changes to this repository using Merge Requests.

## Licence & Legal Information
Please read the [Legal information](LICENSE.md)