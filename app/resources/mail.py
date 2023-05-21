from flask import Blueprint, flash, g, render_template, url_for, request, session, redirect
from app.models.mail import Mail

bp = Blueprint('mail', __name__)

@bp.route('/', methods=['POST', 'GET'])
def index():
    mails = Mail.get_all()
    return render_template('mail/index.html', mails=mails)

@bp.route('/create', methods=['POST', 'GET'])
def create():
    return render_template('mail/create.html')