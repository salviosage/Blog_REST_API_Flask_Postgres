# /run.py
import os

from src.app import create_app

if __name__ == '__main__':
  env_name = os.getenv('FLASK_ENV')
  database = os.getenv('DATABASE_URL')
  testDB = os.getenv('DATABASE_TEST_URL')
  dbdb = os.getenv('Database')
  print(dbdb)
  app = create_app(env_name)
  # run app
  app.run()