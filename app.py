import os
from flask import Flask, render_template, redirect, url_for, flash, request, abort
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

from models import db, User, Product, CartItem

app = Flask(__name__)