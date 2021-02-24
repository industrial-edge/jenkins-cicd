# Implementation

- [Implementation](#implementation)
- [Shell script](#shell-script)
  - [Build stage](#build-stage)
  - [Upload stage](#upload-stage)


# Shell script 

Jenkins pipeline using shell script in this example is implemented using so called declarative syntax. When building declarative pipeline, you start by using `pipeline` keyword. Then you can define where should the pipeline run by specifying Jenkins agent. After that, the pipeline stages shall be defined. 

## Build stage

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

## Upload stage
The upload stage is responsible to perform different jobs. At first, it creates, initialize and copy application files to a workspace folder, which is used by the IE Publisher as a working directory. 

```txt
            stage('Upload') {
                steps {
                
                    echo 'Uploading ...'
                    sh '''
                        rm -rf workspace
                        mkdir workspace
                        cd workspace
                        ie-app-publisher-linux ws init
                        cd ..
                        cp -RT app ./workspace
                        cd workspace

```

After that, the connection to a local running docker engine is established using IE Publisher CLI command.

```txt
                        ie-app-publisher-linux de c -u http://localhost:2375
```
The last part of the upload stage is logging into IEM using credentials stored as Jenkins enviroment variables, creates application version with reverse proxy configuration and uploads to the IEM repository. 

```txt
// login to IEM
                        export IE_SKIP_CERTIFICATE=true
                        ie-app-publisher-linux em li -u "$IEM_URL" -e $USER_NAME -p $PSWD
// creating app version                       
                        ie-app-publisher-linux em app cuv -a $APP_ID -v 0.0.$BUILD_NUMBER -y ./docker-compose.prod.yml -n '{"hello-edge":[{"name":"hello-edge","protocol":"HTTP","port":"80","headers":"","rewriteTarget":"/"}]}' -s 'hello-edge' -t 'FromBoxReverseProxy' -u "hello-edge" -r "/"
// uploading app version                          
                        ie-app-publisher-linux em app uuv -a $APP_ID -v 0.0.$BUILD_NUMBER

```