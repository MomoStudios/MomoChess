from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from momochess.routes import create_routes
def create_app():
  app = Flask(__name__)
  app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/momochess'
  db = SQLAlchemy(app)
  return create_routes(app)

