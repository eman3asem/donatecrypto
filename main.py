from flask import Flask, render_template,  request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import uuid
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Use SQLite for simplicity
db = SQLAlchemy(app)

# Define a simple model
class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    donorName = db.Column(db.String(100), nullable=False)
    email=db.Column(db.String(100), nullable=False)
    donationAmount=db.Column(db.String(100), nullable=False)
    organization=db.Column(db.String(100), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/payment/<organization>/<value>')
def payment(organization, value):
    return render_template('index.html', organization=organization, value=value)

@app.route('/add_donation', methods=['POST'])
def add_donation(organization):
    if request.method == 'POST':
        donor_name = request.form['donorName']
        donor_email = request.form['email']
        donation_amount = request.form['donationAmount']

        new_donation = Donation(donorName=donor_name, email=donor_email, donationAmount=donation_amount,organization=organization)
        db.session.add(new_donation)
        db.session.commit()

        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)