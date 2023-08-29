from flask import Flask, render_template, request
from forms.form import ApplyForm, LoginForm, ContactForm, KycForm
from werkzeug.utils import secure_filename
import requests
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'youwillneverguess'

@app.route('/', methods=['GET', 'POST'])
def home():
    form = ApplyForm()
    if request.method=='POST' and form.validate_on_submit():
        application = {}
        application['name'] = form.name.data;
        application['mobile'] = form.mobile.data;
        application['alternate_mobile'] = form.alternate_mobile.data;
        application['vehicle_number'] = form.vehicle_number.data;
        application['aadhar'] = form.aadhar.data;
        application['pan'] = form.pan.data;
        application['district'] = form.district.data;
        application['address'] = form.address.data;
        return render_template('thanks.html', data=application)
    return render_template('home.html', form=form)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        mobile = form.mobile.data
        pan = form.pan.data
        
    return render_template('login.html', form=form)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST' and form.validate_on_submit():
        contact = {}
        contact['name'] = form.name.data
        contact['mobile'] = form.mobile.data
        contact['email'] = form.email.data
        contact['subject'] = form.subject.data
        return render_template('thanks.html', data=contact)

    return render_template('contact.html', form=form)

@app.route('/score')
def score():
    return render_template('score.html')

@app.route('/kyc', methods=['GET', 'POST'])
def kyc():
    form = KycForm()
    if request.method == 'POST':
        if 'aadhar_front' in request.files:
            aadhar_front = request.files['aadhar_front']
            aadhar_front.save(os.getcwd()+'/uploads/aadhar_front/'+secure_filename(aadhar_front.filename))
        if 'aadhar_back' in request.files:
            aadhar_back = request.files['aadhar_back']
            aadhar_back.save(os.getcwd()+'/uploads/aadhar_back/'+ secure_filename(aadhar_back.filename))        
        return render_template('thanks.html')
    return render_template('kyc.html', form=form)

@app.errorhandler(404)
def error():
    return render_template('404.html')
