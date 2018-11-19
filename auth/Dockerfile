# Realiza o download de uma imagem base Ubuntu com a
# última versão do Python já instalado e configurado
FROM python:latest 

# Executa o comando apt-get update para 
# atualizar os repositórios
RUN ["apt-get", "update"]

# Executa o comando de criação de um diretório para 
# alocar o código-fonte
RUN mkdir -p /src

# Define que o diretório de trabalho do contêiner
# será a pasta anteriormente criada
WORKDIR /src

# Copia o arquivo de dependências do Python para
# dentro do contêiner
COPY requirements.txt /src

# Instala as dependências do Python utilizando 
# o gerenciador de pacotes PIP 
# (que já vem configurado na imagem base)
RUN pip install -r requirements.txt

# Copia todo o código-fonte para dentro do contêiner
COPY . /src

# Expõe a porta 5000, que será utilizada pela API para
# escutar as chamadas HTTP
EXPOSE 5000