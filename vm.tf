provider "aws" {
  region  = "us-east-1"
}

resource "aws_instance" "app_server" {
  ami           = "ami-064983766e6ab3419"
  instance_type = "t2.micro"

  tags = {
    Name = "ExampleAppServerInstance"
  }
}