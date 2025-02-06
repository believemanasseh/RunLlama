FROM ollama/ollama:0.5.7 AS ollama

WORKDIR /app

COPY . .

EXPOSE 11434

COPY start.sh .
RUN chmod +x start.sh

CMD ["./start.sh"]
