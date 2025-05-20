# SVG Path Extractor

Dit project extraheert padcoördinaten uit een SVG-bestand en slaat deze op in een CSV-bestand. Het visualiseert ook het pad met correcte oriëntatie.

## Vereisten

Zorg ervoor dat je Python 3.6 of hoger hebt geïnstalleerd. Installeer alle benodigde packages met:

```bash
pip install -r requirements.txt
```

## Gebruik

### Methode 1: Direct uitvoeren

1. Plaats je SVG-bestand in de projectmap met de naam `pad.svg`
2. Voer het script uit:

```bash
python main.py
```

3. Het script zal:
   - De padcoördinaten uit het SVG-bestand extraheren
   - De coördinaten opslaan in `pad_coordinaten.csv`
   - Een plot tonen met het geëxtraheerde pad

### Methode 2: Docker Container

Je kunt dit project ook in een Docker container uitvoeren, waarvoor geen lokale Python-installatie nodig is:

1. Zorg ervoor dat Docker is geïnstalleerd op je systeem
2. Plaats je SVG-bestand in de projectmap met de naam `pad.svg`
3. Voer het meegeleverde script uit:

```bash
./run_docker.sh
```

4. Het script zal:
   - Een Docker image bouwen met alle benodigde dependencies
   - De container starten en het pad extraheren
   - De uitvoerbestanden (pad_coordinaten.csv en pad_visualisatie.png) kopiëren naar je lokale map
   - De container automatisch opruimen na gebruik

Je kunt ook handmatig de Docker container bouwen en uitvoeren:

```bash
# Docker image bouwen
docker build -t i-cube .

# Docker container runnen
docker run --name i-cube-container -v $(pwd):/app i-cube

# Bestanden kopiëren (indien nodig)
docker cp i-cube-container:/app/pad_visualisatie.png .
docker cp i-cube-container:/app/pad_coordinaten.csv .

# Container opruimen
docker rm i-cube-container
```

## Configuratie

Je kunt de volgende parameters in `main.py` aanpassen:
- `svg_bestand`: Naam van het SVG-bestandpad (standaard: 'pad.svg')
- `csv_bestand`: Naam van het uitvoer CSV-bestandpad (standaard: 'pad_coordinaten.csv')
- `step_size`: Sampleafstand langs het pad (standaard: 1.0)

## Uitvoer

- Een CSV-bestand met X en Y coördinaten
- Een visualisatie van het pad:
  - In normale modus: getoond in een interactief venster
  - In Docker modus: opgeslagen als `pad_visualisatie.png`

## Opmerking

De Y-as wordt automatisch gespiegeld zodat de oriëntatie overeenkomt met de standaard coördinatensystemen waar de Y-as naar boven wijst.