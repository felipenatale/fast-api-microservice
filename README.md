# fast-api-microservice
Microserviço em FastApi - Python

Criação de um microserviço: 

Criar o microserviço já containerizado para uso em orquestradores (uso de dockerfile). 
A aplicação utiliza a extensão .devcontainer do VSCode para facilitar o ambiente de desenvolvimento. 
A aplicação possui as configurações de devcontainer para uso em ambiente de desenvolvmento (devcontainer.json; docker-compose.yml e Dockerfile)

http://127.0.0.1:8000/docs -> SwaggerUI
http://127.0.0.1:8000/redoc -> openapi specification 

TODOs:
Melhorar documentação
1. explicar estrutura
2. explicar como colocar aplicação "em pé"
3. explicar swagger e openapi specification
4. explicar uso do "task" e do uso do pytest/coverage

Criação de conexão com BD para CRUD 
1. add client
2. get clients
3. remove client
4. arquivo de config e uso do .env

Criação e uso de design patter
1. add design patter

Criação de testes unitários
1. testar main - DONE
2. testar healthcheck
3. testar outros endpoints

Adicionar servidor web
1. conectar com nginx