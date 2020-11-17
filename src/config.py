import os
from flask import Flask, request
import telebot
from flask_sqlalchemy import SQLAlchemy


token = "1328680191:AAFpCvIjUfxizaGJX6vvYE-W85yr3lif8Xs"
DATABASE_URI = 'postgres+psycopg2://daka:daka111@localhost:5432/bot'

server = Flask(__name__)
bot = telebot.TeleBot(token)
server.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
server.config['SQLALCHEMY_TRACK_MODFICATIONS'] = True
db = SQLAlchemy(server)