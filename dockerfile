FROM python:3.10-slim
ENV TOKEN='6680716877:AAEyCQi5HRGPe-k9ncxPOASurzXUMROg5Kg'
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "main.py"]

