node {
    checkout scm
    withEnv(['HOME=.']) {
        stage ('Build') {
             docker.image('docker:18.09-dind').withRun(""" --privileged  """) { c ->
             docker.withRegistry( '','credentials-id') {    
             docker.image('$DOCKER_IMAGE_CLI').inside(""" --link ${c.id}:docker --privileged -u root """) {

                sh """
                   
                    cd app
                    docker-compose --host tcp://docker:2375 build
                    docker --host tcp://docker:2375 images
                    cd ..
                    """
          stage ('Upload') {
                 sh """
              
                    cp -RT app /app/src/workspace
                    cd /app/src/workspace
                    ie-app-publisher-linux de c -u http://docker:2375
                    export IE_SKIP_CERTIFICATE=true
                    ie-app-publisher-linux em li -u "$IEM_URL" -e $USER_NAME -p $PSWD
                    ie-app-publisher-linux em app cuv -a $APP_ID -v 0.0.$BUILD_NUMBER -y ./docker-compose.prod.yml -n '{"hello-edge":[{"name":"hello-edge","protocol":"HTTP","port":"80","headers":"","rewriteTarget":"/"}]}' -s 'hello-edge' -t 'FromBoxReverseProxy' -u "hello-edge" -r "/"
                    ie-app-publisher-linux em app uuv -a $APP_ID -v 0.0.$BUILD_NUMBER
                """
             }
             }  
             }
                
          }
        }
    }
}
