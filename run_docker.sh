#!/bin/bash

# Docker image bouwen
echo "Docker image bouwen..."
docker build -t i-cube .

# Docker container runnen
echo "Docker container starten..."
docker run --name i-cube-container -v $(pwd):/app i-cube

# Kopieer de gegenereerde afbeelding naar de host als de container succesvol heeft gedraaid
echo "Bestanden van container naar host kopiëren..."
docker cp i-cube-container:/app/pad_visualisatie.png .
docker cp i-cube-container:/app/pad_coordinaten.csv .

# Container opruimen
echo "Container opruimen..."
docker rm i-cube-container

echo "Klaar! Je kunt pad_visualisatie.png en pad_coordinaten.csv nu bekijken."
