import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

db_password = os.getenv("DATABASE_PASSWORD")

df = pd.read_csv('train.csv')

print(db_password)

engine = create_engine(f'postgresql://dimitri:{db_password}@localhost/titanic')

df.to_sql('passengers', con=engine, index=False, if_exists='replace')
