from flask import Blueprint, flash, g, render_template, url_for, request, session, redirect
from app.models.mail import Mail

bp = Blueprint('mail', __name__)

@bp.route('/', methods=['POST', 'GET'])
def index():
    mails = Mail.get_all()
    return render_template('mail/index.html', mails=mails)

@bp.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        if request.form.get('create'):
            if not request.form['email'] or not request.form['subject'] or not request.form['content']:
                flash('You must complete all the fields')
            else:
                Mail.create(request.form['email'], request.form['subject'], request.form['content'])
                return redirect(url_for('mail.index'))
        else:
            return redirect(url_for('mail.index'))
        
    return render_template('mail/create.html')

def send(email, subject, content):
    pass
    #sg = sendgrid.SendGridAPIClient(api_key=current_app.config['SENDGRID_KEY'])