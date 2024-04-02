import pandas as pd
from sqlalchemy import create_engine
from os import environ

PG_USER = environ["PG_USER"]
PG_PASS = environ["PG_PASS"]

df_to_insert = pd.read_csv("data/driver_standings_2010-2021.csv")
engine = create_engine(f'postgresql://{PG_USER}:{PG_PASS}@localhost:5432/daria')

df_to_insert.to_sql("driver",con=engine,if_exists='replace')