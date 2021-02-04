# Installation of Jenkins server

- [Installation of Jenkins server](#installation-of-jenkins-server)
  - [Installing Jenkins](#installing-jenkins)
  - [Installation steps](#installation-steps)
  

## Installing Jenkins 

Further information about installing Jenkins on your device can be found [here](https://www.jenkins.io/doc/book/installing/)

Jenkins is build on top of java so it typically runs as a standalone application in its own process with the built-in Java application or in a docker container. In this example, we will istall Jenkins server directly on the ubuntu development VM but remember that it is also possible to run Jenkins in docker container. 

## Installation steps 

*Note:*
*Ubuntu 20.04 is used for running Jenkins server*

To install Jenkins on your linux device, follow these instructions:  

1) Jenkins is build using Java and therefore we need to have Java installed. To do that go to your terminal and run this commands

    ```bash
    sudo apt-get update
    sudo apt-get install openjdk-8-jdk
    java -version
    ```
2) Then install Jenkins by running following commands 

    ```bash
    wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -
    sudo sh -c 'echo deb https://pkg.jenkins.io/debian-stable binary/ > \
    /etc/apt/sources.list.d/jenkins.list'
    sudo apt-get update
    sudo apt-get install jenkins
    ```

3) You can start aand check the Jenkins service with the command:

    ```bash
    sudo systemctl start jenkins
    sudo systemctl status jenkins
    ```

4) If everything has been set up correctly, you should see an output like this:

    ```txt
    Loaded: loaded (/etc/rc.d/init.d/jenkins; generated)
    Active: active (running) since Tue 2018-11-13 16:19:01 +03; 4min 57s ago
    ```