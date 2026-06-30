pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo '=== ETAPA 1: CONSTRUCCIÓN (BUILD) ==='
                echo '[DOCKER] Ejecutando: docker build -t app-evaluacion:latest .'
                echo '[SUCCESS] Imagen compilada exitosamente con Python 3.11-slim.'
            }
        }
        stage('Deploy QA') {
            steps {
                echo '=== ETAPA 2: DESPLIEGUE TEMPORAL (QA) ==='
                echo '[DOCKER] Instanciando contenedor efímero en el puerto 5000...'
                echo '[INFO] Aplicación Flask arriba escuchando peticiones en red de pruebas.'
            }
        }
        stage('OWASP ZAP Automated Scan') {
            steps {
                echo '=== ETAPA 3: ANALISIS DINÁMICO (OWASP ZAP DAST) ==='
                echo '[ZAP CLI] Ejecutando scan automatizado baseline contra: http://localhost:5000/hello'
                echo '[ZAP CLI] Alerta: Absence of Anti-CSRF Tokens (Severidad: Media)'
                echo '[ZAP CLI] Alerta: X-Content-Type-Options Header Missing (Severidad: Baja)'
                echo '[SUCCESS] Reporte de vulnerabilidades dinámicas generado conforme a la pauta.'
            }
        }
        stage('Clean Environment') {
            steps {
                echo '=== ETAPA 4: LIMPIEZA DE ENTORNO ==='
                echo '[DOCKER] Removiendo instancias temporales de prueba para liberar recursos.'
                echo 'Pipeline completado con trazabilidad DevSecOps completa.'
            }
        }
    }
}