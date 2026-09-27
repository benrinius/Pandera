# Pandera – Datavalidering i Python

Ett mindre Python-projekt som undersöker hur Pandera kan användas för att validera data i en pandas DataFrame.

Projektet innehåller ett Pandera-schema som kontrollerar:

- datatyper
- åldersintervall
- negativa köpbelopp
- duplicerade `customer_id`

Det finns två dataset: ett med korrekt data och ett med avsiktliga fel. Projektet demonstrerar även hur `lazy=True` kan användas för att samla flera valideringsfel.

## Projektstruktur

```text
pandera_project/
├── data/
│   ├── valid_data.csv
│   └── invalid_data.csv
│
├── src/
│   └── validation.py
│
├── README.md
├── rapport.md
├── requirements.txt
└── .gitignore
```

## Installation

Skapa och aktivera ett virtuellt Python-environment och installera beroendena:

```bash
pip install -r requirements.txt
```

## Kör projektet

Kör från projektets rotmapp:

```bash
python src/validation.py
```

Programmet validerar först den korrekta datan och visar därefter vilka valideringsfel som upptäcks i den felaktiga datan.

## Teknik

- Python 3.13
- pandas
- Pandera
- CSV