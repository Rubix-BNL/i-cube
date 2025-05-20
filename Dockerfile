FROM python:3.9-slim

WORKDIR /app

# Kopieer requirements.txt en installeer dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopieer de rest van de projectbestanden
COPY main.py .
COPY pad.svg .
COPY pad_coordinaten.csv .

# Instellen van matplotlib voor gebruik in containeromgeving
ENV PYTHONUNBUFFERED=1
ENV MPLBACKEND=Agg

# Commando dat uitgevoerd wordt wanneer de container start
CMD ["python", "main.py"]
