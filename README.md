# Despliegue Juego Snake

Este repositorio contiene los archivos necesarios para desplegar una aplicación de Snake en un contenedor Docker, y la infraestructura para desplegar esta aplicación automáticamente en AWS usando Terraform.

## Pasos para el Despliegue

### 1. Clonar el Repositorio
Primero, clona este repositorio en tu máquina local usando Git.

```sh
git clone https://github.com/TU_USUARIO/snake.git
cd snake/

## 2. Instalar Terraform
Terraform se puede instalar de dos maneras: usando comandos o descargándolo directamente desde la página oficial.

En Ubuntu
sh
Copiar código
sudo apt-get update
sudo snap install terraform --classic

Otra forma: Instalación por Descarga Directa
Ve a la página de descargas de Terraform.
Descarga el paquete adecuado para tu sistema operativo.
Extrae el archivo y mueve el ejecutable a un directorio incluido en tu variable PATH.

## 3. Configurar Credenciales de AWS
Para que Terraform pueda interactuar con tu cuenta de AWS, necesitas configurar tus credenciales en el archivo ~/.aws/credentials.

Crea el archivo si no existe y agrega tus credenciales de AWS:

sh
Copiar código
mkdir -p ~/.aws/
nano ~/.aws/credentials
Copia allí las credenciales que aparecen en AWS DETAILS y selecciona AWS CLI:

ini
Copiar código
[default]
aws_access_key_id = TU_ACCESS_KEY_ID
aws_secret_access_key = TU_SECRET_ACCESS_KEY

## 4. Iniciar Terraform
Navega al directorio donde se encuentra tu archivo de configuración de Terraform (normalmente main.tf) y sigue estos pasos:

Inicializa los plugins y módulos de Terraform
sh
Copiar código
terraform init
Revisa el plan de ejecución para la infraestructura
sh
Copiar código
terraform plan
Aplica el plan para crear la infraestructura
sh
Copiar código
terraform apply -auto-approve

## 5. Acceder a la Aplicación de Snake
Una vez que la infraestructura esté desplegada y el contenedor Docker esté corriendo, obtén la dirección IP de la instancia donde está ejecutándose la aplicación. Luego, abre tu navegador web preferido y accede a la aplicación utilizando la dirección IP y el puerto 80 como se muestra a continuación:

sh
Copiar código
http://<tu-dirección-ip>
