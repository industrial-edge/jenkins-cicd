# Creating Jenkins pipelines using shell script

Automate process of uploading apps to IEM with Jenkins using shell script. To demonstarte this approach, a simple nginx application is used. As a prerequisity for this task you need to have repository on GitHub, Jenkins installed and setup GitHub webhook to connect them. In order to complete this, follow instructions below. 

- [Creating Jenkins pipelines using shell script](#creating-jenkins-pipelines-using-shell-script)
  - [Create project and application in IEM](#create-project-and-application-in-iem)
  - [Create GitHub repository](#create-github-repository)
  - [Create Jenkins pipeline](#create-jenkins-pipeline)
  - [Create GitHub webhook](#create-github-webhook)



## Create project and application in IEM 
*Prerequisities:*
*- IEM isntalled and configured*

1) Go to the "Applications" section of your Edge Management system. 

2) Click on "Create Project" button in the right upper corner. 

3) Provide necessary information for your project 

    ```txt
    - Project Name
    - Description 
    - Company information (if needed)
    ```

4) Click on "Create" to create the project. 

<img src="graphics/create_project.gif" width="1000"/>


5) Go to your created project and clisk on "Create application"

6) Fill in the form for your application 


    ```txt
    - Application Name 
    - Repository Name
    - Website
    - Sescription
    - Select icon
    ```

7) Click on "Create" button. Your application is succesfully created.

<img src="graphics/create_app.gif" width="1000"/>


## Create GitHub repository 


## Create Jenkins pipeline

## Create GitHub webhook