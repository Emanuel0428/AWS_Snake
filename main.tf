provider "aws" {
  region = "us-east-1"
}

// Creamos la llave para conectarse remotamente a la instancia
resource "aws_key_pair" "deployer_key" {
  key_name   = "KeyIaC"
  public_key = file("C:/Users/<tu_usuario>/.ssh/KeyIaC.pub")
}

// Creación del security group
resource "aws_security_group" "web" {
  name        = "web_sg"
  description = "Security Group para acceso a puertos 22 y 80"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

// Creamos la instancia
resource "aws_instance" "web_server" {
  ami                         = "ami-04b70fa74e45c3917" # Amazon Linux 2 AMI
  instance_type               = "t2.micro"
  key_name                    = aws_key_pair.deployer_key.key_name
  security_groups             = [aws_security_group.web.name]
  associate_public_ip_address = true

  user_data = <<-EOF
    #!/bin/bash
    sudo yum update -y
    sudo amazon-linux-extras install docker -y
    sudo service docker start
    sudo usermod -a -G docker ec2-user
    cd /home/ec2-user
    sudo curl -L -o app.tar.gz https://github.com/tu_usuario/tu_repositorio/archive/refs/heads/main.tar.gz
    sudo tar -xzf app.tar.gz --strip 1
    sudo docker build -t my_flask_app .
    sudo docker run -d -p 80:5000 my_flask_app
  EOF

  tags = {
    Name = "FlaskAppServer"
  }
}

output "instance_ip" {
  value = aws_instance.web_server.public_ip
}
