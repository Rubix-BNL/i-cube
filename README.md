# SVG Path Extractor

Dit project extraheert padcoördinaten uit een SVG-bestand en slaat deze op in een CSV-bestand. Het visualiseert ook het pad met correcte oriëntatie.

## Vereisten

Zorg ervoor dat je Python 3.6 of hoger hebt geïnstalleerd. Installeer alle benodigde packages met:

```bash
pip install -r requirements.txt
```

## Gebruik

1. Plaats je SVG-bestand in de projectmap met de naam `pad.svg`
2. Voer het script uit:

```bash
python main.py
```

3. Het script zal:
   - De padcoördinaten uit het SVG-bestand extraheren
   - De coördinaten opslaan in `pad_coordinaten.csv`
   - Een plot tonen met het geëxtraheerde pad

## Configuratie

Je kunt de volgende parameters in `main.py` aanpassen:
- `svg_bestand`: Naam van het SVG-bestandpad (standaard: 'pad.svg')
- `csv_bestand`: Naam van het uitvoer CSV-bestandpad (standaard: 'pad_coordinaten.csv')
- `step_size`: Sampleafstand langs het pad (standaard: 1.0)

## Uitvoer

- Een CSV-bestand met X en Y coördinaten
- Een plot van het pad met correcte oriëntatie

## Opmerking

De Y-as wordt automatisch gespiegeld zodat de oriëntatie overeenkomt met de standaard coördinatensystemen waar de Y-as naar boven wijst.