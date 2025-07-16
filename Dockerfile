# 1. Escolha uma imagem base estável e leve
FROM python:3.11-slim

# 2. Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# 3. Copie o arquivo de dependências primeiro para aproveitar o cache do Docker
# O Docker só reinstalará as dependências se este arquivo mudar.
COPY requirements.txt .

# 4. Instale as dependências
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 5. Copie o restante do código da aplicação
COPY . .

# 6. Exponha a porta em que a aplicação será executada
EXPOSE 8080

# 7. Defina o comando para iniciar a aplicação com Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
