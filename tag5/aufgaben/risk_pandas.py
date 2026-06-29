# Counterparty-Exposure-Report (pandas)
import pandas as pd
from decimal import Decimal
FILE = r"/home/ucuber/Workspace/kurse/kurs-python/tag5/aufgaben/gegenparteien.txt"
GEWICHT = {"AAA": 0.2, "AA": 0.4, "A": 0.6, "BBB": 0.8, "BB": 1.0, "B": 1.5, "CCC": 2.0}
LIMIT = 5_000_000

# Einlesen: eine Zeile Code, Spaltennamen vergeben
df = pd.read_csv(FILE, sep="\t", names=["name", "rating", "exposure"])

# Risikogewicht als neue Spalte ableiten
df["gewicht"] = df["rating"].map(GEWICHT).fillna(1.0)
df["gewichtet"] = df["exposure"] * df["gewicht"]

# Kennzahlen
print(f"{len(df)} Gegenparteien")
print(f"Exposure gesamt:    {df['exposure'].sum():,.0f} EUR")
print(f"Risikogewichtet:    {df['gewichtet'].sum():,.0f} EUR")

# Limit-Verstoesse, gleich absteigend sortiert
ueber = df[df["exposure"] > LIMIT].sort_values("exposure", ascending=False)
print(f"\nUeber Limit ({LIMIT:,.0f} EUR):")
print(ueber[["name", "rating", "exposure"]].to_string(index=False))

# Erläuterung
# die Praxis in der Finanzwelt: pandas für Analyse, Aggregation, Reporting — wo float64 völlig reicht,
#  weil ein Risiko-Report auf den Euro genau gar nicht sein muss und Rundung im Rauschen verschwindet.
# Decimal für die Stellen, wo Centgenauigkeit zählt — Buchungssätze, Abrechnungen, alles, was bilanziell
# stimmen muss. Das macht man dann eben nicht in einem Riesen-DataFrame, sondern in der Buchungslogik
# (oft sogar in der Datenbank mit NUMERIC/DECIMAL-Spalten).
#
# Merksatz: Wo analysiere ich (float ok), und wo buche/rechne ich verbindlich ab (Decimal/NUMERIC)
