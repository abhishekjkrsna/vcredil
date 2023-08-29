from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, FileField
from wtforms.validators import DataRequired, Length, Optional, Regexp, Email

districts = {
    1: "Agra",
    2: "Aligarh",
    3: "Ambedkar Nagar",
    4: "Amethi",
    5: "Amroha",
    6: "Auraiya",
    7: "Ayodhya",
    8: "Azamgarh",
    9: "Baghpat",
    10: "Bahraich",
    11: "Ballia",
    12: "Balrampur",
    13: "Banda",
    14: "Barabanki",
    15: "Bareilly",
    16: "Basti",
    17: "Bhadohi",
    18: "Bijnor",
    19: "Budaun",
    20: "Bulandshahr",
    21: "Chandauli",
    22: "Chitrakoot",
    23: "Deoria",
    24: "Etah",
    25: "Etawah",
    26: "Farrukhabad",
    27: "Fatehpur",
    28: "Firozabad",
    29: "Gautam Buddha Nagar",
    30: "Ghaziabad",
    31: "Ghazipur",
    32: "Gonda",
    33: "Gorakhpur",
    34: "Hamirpur",
    35: "Hapur",
    36: "Hardoi",
    37: "Hathras",
    38: "Jalaun",
    39: "Jaunpur",
    40: "Jhansi",
    41: "Kannauj",
    42: "Kanpur Dehat",
    43: "Kanpur Nagar",
    44: "Kasganj",
    45: "Kaushambi",
    46: "Lakhimpur Kheri",
    47: "Kushinagar",
    48: "Lalitpur",
    49: "Lucknow",
    50: "Maharajganj",
    51: "Mahoba",
    52: "Mainpuri",
    53: "Mathura",
    54: "Mau",
    55: "Meerut",
    56: "Mirzapur",
    57: "Moradabad",
    58: "Muzaffarnagar",
    59: "Pilibhit",
    60: "Pratapgarh",
    61: "Prayagraj",
    62: "Raebareli",
    63: "Rampur",
    64: "Saharanpur",
    65: "Sambhal",
    66: "Sant Kabir Nagar",
    67: "Shahjahanpur",
    68: "Shamli",
    69: "Shravasti",
    70: "Siddharthnagar",
    71: "Sitapur",
    72: "Sonbhadra",
    73: "Sultanpur",
    74: "Unnao",
    75: "Varanasi"
}


class ApplyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(message='Please fill name')], render_kw={"placeholder": "Eg: Sunita Devi"})
    mobile = StringField('Mobile', validators=[DataRequired(message='Please fill mobile number'), Length(min=10, max=10), Regexp(r'\d{10}')], render_kw={"placeholder": "Eg: 9876543210"})
    alternate_mobile = StringField('Alternate Mobile', validators=[Optional(), Length(max=10), Regexp(r'\d{10}')], render_kw={"placeholder": "Eg: 6328798541"})
    vehicle_number = StringField('Vehicle Number', validators=[DataRequired(message='Please Enter the vehicle number')], render_kw={"placeholder": "Eg: UP32AB1234"})
    aadhar = StringField('Aadhar Number', validators=[DataRequired(message='Please Enter the Aadhar Number'), Regexp(regex=r'^\d{12}$', message='Incorrect Aadhar Number')], render_kw={"placeholder": "Eg: 1254659887546532"})
    pan = StringField('Pan Number', validators=[DataRequired(message='Please fill the pan number'), Regexp(regex=r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$', message='Incorrect PAN Number')],render_kw={"placeholder": "Eg: ABCDE1234A"})
    district = SelectField('District', choices=[(key, value) for key, value in districts.items()], validators=[DataRequired(message='Select the district')])
    address = TextAreaField('Enter address', validators=[DataRequired()], render_kw={"placeholder": "Eg: C/O, Ram Prasad, 10 mrjapur, Unnao, UP-209859"})
    submit = SubmitField('Submit')
    
class LoginForm(FlaskForm):
    mobile = StringField('Mobile Number', validators=[DataRequired(message='Please Enter the Mobile Number')], render_kw={"placeholder": "Eg: 9876543210"})
    pan = StringField('Pan Number', validators=[DataRequired('Please Enter the Pan Number'), Regexp(regex=r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$', message='Incorrect PAN Number')],render_kw={"placeholder": "Eg: ABCDE1234A"})
    submit = SubmitField('Submit')

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(message='Please enter your name')], render_kw={"placeholder": "Eg: Sunita Devi"})
    mobile = StringField('Mobile', validators=[DataRequired(message='Please fill mobile number'), Length(min=10, max=10), Regexp(r'\d{10}')], render_kw={"placeholder": "Eg: 9876543210"})
    email = StringField('Email', validators=[Optional(), Email()], render_kw={"placeholder": "Eg: sunita@abc.com"})
    subject = TextAreaField('Subject', validators=[DataRequired()], render_kw={"placeholder": "Enter your issue"})
    submit = SubmitField('Submit')

class KycForm(FlaskForm):
    aadhar_front = FileField('Aadhar Front')
    aadhar_back = FileField('Aadhar Back')
    pan = FileField('PAN Card')
    submit = SubmitField('Submit')