# CI/CD pipelines with Jenkins 

Automate process of uploading apps to IEM with Jenkins.


- [Simulating virtual sensor with LiveTwin](#simulating-virtual-sensor-with-livetwin)
  - [Description](#description)
    - [Overview](#overview)
    - [General task](#general-task)

## Description


###  Overview
This application example shows how to create Jenkins CI/CD pipelines to automatically upload applications to Industrial Edge Management system.

### General task
The main goal of this example is to show how to setup Jenkins server and create Jenkins pipelines to upload applications to IEM. Jenkins can be integrated with several Git providers but GitHub is used for this example. With GitHub webhook feature it is possible on every commitment to the GitHub repository to automatically trigger Jenkins pipeline that build, test and upload application to IEM. 

<img src="./graphics/overview.png" width="700"/>

