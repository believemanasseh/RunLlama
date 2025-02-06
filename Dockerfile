FROM ollama/ollama:0.5.7

WORKDIR /app

COPY . .

EXPOSE 11434

COPY start.sh .
RUN chmod +x start.sh

ENTRYPOINT ["./start.sh"]
