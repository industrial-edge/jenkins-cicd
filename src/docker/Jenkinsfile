node {
    checkout scm
    withEnv(['HOME=.']) {          
        docker.image('docker:18.09-dind').withRun(""" --privileged  """) { c ->   

            docker.withRegistry('', 'credentials-id') { 
                
                echo "DOCKER_IMAGE_CLI -> $DOCKER_IMAGE_CLI"

                def trimmedImage = "$DOCKER_IMAGE_CLI".trim()
                def trimmedIcon = "$ICON_PATH".trim()

                echo "1"

                docker.image(trimmedImage).inside(""" --link ${c.id}:docker --privileged -u root """) {
                    
                    echo "2"

                    stage('Build') {

                        echo "3"

                        sh """
                            cd app
                            docker-compose --host tcp://docker:2375 build
                            docker --host tcp://docker:2375 images
                            cd ..
                        """
                    }

                    stage('Upload') {
                        sh """
                            cp -RT app /app/src/workspace
                            cd /app/src/workspace

                            export IE_SKIP_CERTIFICATE=true
                            export EDGE_SKIP_TLS=1

                            iectl config add publisher --name "publisherdev" --dockerurl "http://docker:2375" --workspace "/app/src/workspace"
                            iectl publisher workspace init
                            cd ..

                            iectl publisher docker-engine v -u http://docker:2375
                            
                            iectl config add iem --name "iemdev" --url ${IEM_URL} --user ${USER_NAME} --password '$PSWD'

                            iectl publisher standalone-app create --reponame ${REPO_NAME} --appdescription "uploaded using Jenkins" --iconpath ${trimmedIcon} --appname ${APP_NAME}

                            version=\$(iectl publisher standalone-app version list -a ${APP_NAME} -k "versionNumber" | python3 getAppVersion.py)

                            version_new=\$(echo \$version | awk -F. -v OFS=. 'NF==1{print ++\$NF}; NF>1{if(length(\$NF+1)>length(\$NF))\$(NF-1)++; \$NF=sprintf("%0*d", length(\$NF), (\$NF+1)%(10^length(\$NF))); print}')
                            echo 'new Version: '\$version_new

                            iectl publisher standalone-app version create --appname ${APP_NAME} --changelogs "new release" --yamlpath "docker-compose.prod.yml" --versionnumber \$version_new -n '{"hello-edge":[{"name":"hello-edge","protocol":"HTTP","port":"80","headers":"","rewriteTarget":"/"}]}' -s 'hello-edge' -t 'FromBoxReverseProxy' -u "hello-edge" -r "/"

                            iectl publisher app-project upload catalog --appname ${APP_NAME} -v \$version_new
                        """
                    }
                }        
            }
        }
    }
}

