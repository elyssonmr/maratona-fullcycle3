Primeiro Desafio Maratona Full Cycle
====================================

Link da imagem gerada: [https://hub.docker.com/r/elyssonmr/fullcycle-hello-go](https://hub.docker.com/r/elyssonmr/fullcycle-hello-go)

Para rodar o projeto
--------------------

1. Faça o download deste repositório.
2. Instale o [Go lang](https://golang.org/dl/) e o [Docker](https://docs.docker.com/get-docker/) caso não os tenha instalado.
3. Execute o comando `make build_app` para compilar a aplicação.
4. Execute o comando `make build_docker_image` para construir uma nova imagem Docker. **Não é necessário fazer o build da aplicação primeiro.**
5. Execute o comando `make upload_docker_image` para fazer o upload da imagem para o Docker Hub. Será necessário alterar o nome do usuário no `makefile`. **Não é necessário contruir a imagem docker da aplicação primeiro.**

Informações do desafio
----------------------

O primeiro desafio dessa maratona consiste em criar um "Hello Full Cycle" utilizando a linguagem Golang.
Basicamente quando o arquivo compilado for executado, deverá ser exibido: Hello Full Cycle.
Se tudo estiver funcionando de forma adequada, gere uma imagem docker que quando executada deva rodar o programa criado em Golang.

Faça o push da imagem no Docker Hub e informe a url da imagem na área de entrega do desafio abaixo.

OBS: Caso você não tenha experiência com Docker ou com Golang, recomendamos os vídeos abaixo:
- [Iniciando com Docker](https://www.youtube.com/watch?v=39Jl_M3nUTo)
- [Go Lang: A linguagem simples e rápida que todo desenvolvedor Full Cycle deveria saber](https://www.youtube.com/watch?v=jzUCK3ElaN4)

Não se esqueça que também temos um canal na comunidade criada no Discord para debater exatamente esse desafio.
