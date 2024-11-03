from flask import render_template, request, redirect, url_for, Blueprint
from app import db
from app.models import Service

# Criação do Blueprint
main = Blueprint('main', __name__)

@main.route('/')
def home():
    services = Service.query.all()
    return render_template('index.html', services=services)

@main.route('/services')
def services():
    services = Service.query.all()
    return render_template('services.html', services=services)

@main.route('/customize')
def customize():
    return render_template('customize.html')

@main.route('/pricing')
def pricing():
    return render_template('pricing.html')

@main.route('/testimonials')
def testimonials():
    return render_template('testimonials.html')
