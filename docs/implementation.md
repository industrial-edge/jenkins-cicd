# Implementation

- [Implementation](#implementation)
- [Shell script](#shell-script)


# Shell script 

Jenkins pipeline using shell script in this example is implemented using so called declarative syntax. When building declarative pipeline, you start by using `pipeline` keyword. Then you can define where should the pipeline run by specifying Jenkins agent. After that, the pipeline stages shall be defined. 

```txt
    pipeline {
        agent any
        stages {
```

The build stage is building docker images defined inside of the docker-compose file. 

```txt
            stage('Build') {
            steps {
                echo 'Building..'
                sh '''
                    cd app
                    docker-compose build
                '''
            }
        }

```
