from flask import Blueprint, flash, g, render_template, url_for, request, session, redirect

bp = Blueprint('mail', __name__)

@bp.route('/', methods=['POST', 'GET'])
def index():
    return render_template('mail/index.html')