pipeline {
    agent any

    stages {
        
        stage('Build') {
            steps {
                echo 'Building..'
                sh '''
                    cd app
                    docker-compose build
                '''
            }
        }
        stage('Upload') {
            steps {
                
                echo 'Uploading ...'
                sh '''
                    rm -rf workspace
                    mkdir workspace

                    iectl publisher docker-engine v -u http://localhost:2375

                    export IE_SKIP_CERTIFICATE=true
                    export EDGE_SKIP_TLS=1

                    iectl config add publisher --name "publisherdev" --dockerurl "http://localhost:2375" --workspace "./workspace"                    

                    cd workspace
                    iectl publisher workspace init

                    iectl config add iem --name "iemdev" --url ${IEM_URL} --user ${USER_NAME} --password '$PSWD'
                    iectl publisher standalone-app create --reponame ${REPO_NAME} --appdescription "upload using Jenkins" --iconpath ${ICON_PATH} --appname ${APP_NAME}

                    version=\$(iectl publisher standalone-app version list -a ${APP_NAME} -k "versionNumber" | python3 getAppVersion.py)

                    version_new=\$(echo \$version | awk -F. -v OFS=. 'NF==1{print ++\$NF}; NF>1{if(length(\$NF+1)>length(\$NF))\$(NF-1)++; \$NF=sprintf("%0*d", length(\$NF), (\$NF+1)%(10^length(\$NF))); print}')
                    echo 'new Version: '\$version_new

                    iectl publisher standalone-app version create --appname ${APP_NAME} --changelogs "new release" --yamlpath "docker-compose.prod.yml" --versionnumber \$version_new -n '{"hello-edge":[{"name":"hello-edge","protocol":"HTTP","port":"80","headers":"","rewriteTarget":"/"}]}' -s 'hello-edge' -t 'FromBoxReverseProxy' -u "hello-edge" -r "/"

                    iectl publisher app-project upload catalog --appname ${APP_NAME} -v \$version_new

                '''

            }
        }
      
    }
}

