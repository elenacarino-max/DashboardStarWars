from pathlib import Path

print("Estoy en:")
print(Path.cwd())

print("\nBuscando todos los characters.csv dentro de data/raw:")
for ruta in Path("data/raw").rglob("characters.csv"):
    print(ruta)

print("\nBuscando todas las carpetas llamadas csv dentro de data/raw:")
for ruta in Path("data/raw").rglob("csv"):
    if ruta.is_dir():
        print(ruta)




from pathlib import Path
import pandas as pd

RAW_DIR = Path("data/raw")

STARWARS_PATH = RAW_DIR / "StarWars" / "StarWars.csv"
KAGGLE_CSV_DIR = RAW_DIR / "starwars_kaggle" / "archive (1)" / "csv"

print("Ruta StarWars:", STARWARS_PATH)
print("Existe StarWars:", STARWARS_PATH.exists())

print("Ruta Kaggle CSV:", KAGGLE_CSV_DIR)
print("Existe carpeta Kaggle CSV:", KAGGLE_CSV_DIR.exists())

print("Existe characters.csv:", (KAGGLE_CSV_DIR / "characters.csv").exists())

df_starwars = pd.read_csv(STARWARS_PATH)

df_characters = pd.read_csv(KAGGLE_CSV_DIR / "characters.csv")
df_films = pd.read_csv(KAGGLE_CSV_DIR / "films.csv")
df_planets = pd.read_csv(KAGGLE_CSV_DIR / "planets.csv")
df_species = pd.read_csv(KAGGLE_CSV_DIR / "species.csv")
df_starships = pd.read_csv(KAGGLE_CSV_DIR / "starships.csv")
df_vehicles = pd.read_csv(KAGGLE_CSV_DIR / "vehicles.csv")
df_quotes = pd.read_csv(KAGGLE_CSV_DIR / "quotes.csv")
df_weapons = pd.read_csv(KAGGLE_CSV_DIR / "weapons.csv")
df_droids = pd.read_csv(KAGGLE_CSV_DIR / "droids.csv")

print("\nDatasets cargados correctamente:")
print("StarWars:", df_starwars.shape)
print("Characters:", df_characters.shape)
print("Films:", df_films.shape)
print("Planets:", df_planets.shape)
print("Species:", df_species.shape)
print("Starships:", df_starships.shape)
print("Vehicles:", df_vehicles.shape)
print("Quotes:", df_quotes.shape)
print("Weapons:", df_weapons.shape)
print("Droids:", df_droids.shape)

print("\nPrimeras filas de Characters:")
print(df_characters.head())