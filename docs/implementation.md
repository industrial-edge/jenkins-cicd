# Implementation

- [Implementation](#implementation)
  - [Shell script](#shell-script)
    - [Build stage](#build-stage)
    - [Upload stage](#upload-stage)
  - [Using Docker with Pipeline](#using-docker-with-pipeline)
    - [Build stage](#build-stage-1)
    - [Upload stage](#upload-stage-1)


## Shell script 

Jenkins pipeline using shell script in this example is implemented using so called declarative pipeline syntax. When building declarative pipeline, you start by using `pipeline` keyword. Then you can define where should the pipeline run by specifying Jenkins agent. After that, the pipeline stages shall be defined. 

### Build stage

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

### Upload stage
The upload stage is responsible to perform different jobs. At first, it creates, initialize and copy application files to a workspace folder, which is used by the IECTL  as a working directory. 

```txt
            stage('Upload') {
                steps {
                
                    echo 'Uploading ...'
                    sh '''
                        rm -rf workspace
                        mkdir workspace
                        cd workspace
                        iectl publisher workspace init
                        cd ..
                        cp -RT app ./workspace
                        cd workspace

```

After that, the connection to a local running docker engine is established using IE Publisher CLI command.

```txt
                        iectl publisher docker-engine v -u http://localhost:2375
```
The last part of the upload stage is logging into IEM using credentials stored as Jenkins environment variables, creates application version with reverse proxy configuration and uploads to the IEM repository. 

```txt
// login to IEM
                        export IE_SKIP_CERTIFICATE=true
                        ie-app-publisher-linux em li -u "$IEM_URL" -e $USER_NAME -p $PSWD
// creating app version                       
                        ie-app-publisher-linux em app cuv -a $APP_ID -v 0.0.$BUILD_NUMBER -y ./docker-compose.prod.yml -n '{"hello-edge":[{"name":"hello-edge","protocol":"HTTP","port":"80","headers":"","rewriteTarget":"/"}]}' -s 'hello-edge' -t 'FromBoxReverseProxy' -u "hello-edge" -r "/"
// uploading app version                          
                        ie-app-publisher-linux em app uuv -a $APP_ID -v 0.0.$BUILD_NUMBER

```


## Using Docker with Pipeline

Jenkins pipeline using docker in this example is implemented using so called scripted pipeline syntax. When building scripted pipeline, you start by using `node` keyword. Then the `checkout` keyword is used to pull application files from the Git repository to the Jenkins server. After that, you can specify the docker images to be used inside of the pipeline. In this example we use 2 docker containers. The `docker:18.09-dind` container is pulled from Docker Hub and it is used as a service container with docker daemon exposed on port 2375. The second container is a custom docker container with IE Publisher CLI installed. These containers are linked to each other so they can communicate over this link. The infrastructure of the containers is shown in the picture below. The jobs within the stages are then running inside of the custom docker container.

<img src="./graphics/docker_pipeline.PNG" width="200"/>

```txt
node {
    checkout scm
    withEnv(['HOME=.']) {          
        docker.image('docker:18.09-dind').withRun(""" --privileged  """) { c ->
            docker.withRegistry( '','credentials-id') {    
                docker.image('$DOCKER_IMAGE_CLI').inside(""" --link ${c.id}:docker --privileged -u root """) {

```
### Build stage

During the build stage, the docker images defined inside of the `docker-compose.yml` file are build using connection to exposed docker daemon. 

```txt
                    stage ('Build') {
                        sh """
                            cd app
                            docker-compose --host tcp://docker:2375 build
                            docker --host tcp://docker:2375 images
                            cd ..
                        """
                    }

```

### Upload stage

The upload stage is performing the same task as shown for the shell script. The only difference is that the working directory for the IE Publisher is already initialize inside of the docker container and the connection to the docker engine is done by using docker link. 



```txt
                    stage ('Upload') {
                        sh """
// copy app files                       
                            cp -RT app /app/src/workspace
                            cd /app/src/workspace
// connection to docker engine
                            ie-app-publisher-linux de c -u http://docker:2375
// login to IEM
                            export IE_SKIP_CERTIFICATE=true
                            ie-app-publisher-linux em li -u "$IEM_URL" -e $USER_NAME -p $PSWD
// create app version
                            ie-app-publisher-linux em app cuv -a $APP_ID -v 0.0.$BUILD_NUMBER -y ./docker-compose.prod.yml -n '{"hello-edge":[{"name":"hello-edge","protocol":"HTTP","port":"80","headers":"","rewriteTarget":"/"}]}' -s 'hello-edge' -t 'FromBoxReverseProxy' -u "hello-edge" -r "/"
// upload app version
                            ie-app-publisher-linux em app uuv -a $APP_ID -v 0.0.$BUILD_NUMBER
                        """
                    }  


```
