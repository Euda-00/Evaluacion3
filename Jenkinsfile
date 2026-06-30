pipeline {
    agent any
    
    environment {
        // Definimos el nombre de la imagen y el contenedor para el despliegue efímero
        APP_NAME = "app"
    }

    stages {
        stage('Build') {
            steps {
                echo '=== CONSTRUCCIÓN DE LA IMAGEN DOCKER ==='
                // Construimos la imagen local con los cambios seguros que le hiciste a app.py
                sh "docker build -t ${APP_NAME}:latest ."
            }
        }

        stage('Deploy QA') {
            steps {
                echo '=== DESPLEGANDO INSTANCIA TEMPORAL PARA PRUEBAS (DAST) ==='
                // Si ya existe un contenedor corriendo con ese nombre, lo matamos para evitar topes de puertos
                sh "docker rm -f ${APP_NAME} || true"
                // Levantamos la app Flask en segundo plano (-d) en el puerto 5000
                sh "docker run -d --name ${APP_NAME} -p 5000:5000 ${APP_NAME}:latest"
                // Esperamos unos segundos para asegurar que Flask levantó por completo
                sh "sleep 5"
            }
        }

        stage('OWASP ZAP Automated Scan') {
            steps {
                echo '=== EJECUTANDO OWASP ZAP BASELINE SCAN (REAL) ==='
                
                /* Explicación del comando:
                   - Corremos el contenedor oficial de OWASP ZAP.
                   - Usamos '--network=host' para que el contenedor de ZAP pueda ver el localhost de la máquina.
                   - Ejecutamos el script nativo 'zap-baseline.py' contra el endpoint de tu Flask.
                   - El parámetro '-I' evita que Jenkins falle inmediatamente si encuentra alertas bajas/medias.
                */
                sh "docker run --rm --network=host owasp/zap2docker-stable zap-baseline.py -t http://localhost:5000/hello -I"
            }
        }

        stage('Clean Environment') {
            steps {
                echo '=== LIMPIEZA DEL ENTORNO ==='
                // Bajamos el contenedor de pruebas para no dejar basura corriendo en los puertos
                sh "docker stop ${APP_NAME} || true"
                sh "docker rm ${APP_NAME} || true"
            }
        }
    }
}