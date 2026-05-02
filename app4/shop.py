from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
bootstrap = Bootstrap(app)

technologies = [
    { "name": "Headphones", "price": "$99.99", "description": "High-quality headphones for immersive audio experiences.", "image": "headphones.jpg" },
    { "name": "Speakers", "price": "$199.99", "description": "Powerful speakers for crystal-clear sound.","image": "speaker.jpg" },
    { "name": "Earphones", "price": "$99.99", "description": "Comfortable earphones for portable listening.", "image": "earphones.jpg" },
    ]

class OpinionForm(FlaskForm):
    opinion = StringField('Your Opinion: ',validators = [DataRequired(),Length(min=0,max=100)])
    submit = SubmitField('Submit')

@app.route('/')
def galleryPage():
    return render_template('index.html',technologies = technologies)

@app.route('/tech/<int:techId>',methods=['GET','POST'])
def singleProductPage(techId):
    form = OpinionForm()
    if form.validate_on_submit():
        return render_template('SingleTechOpinion.html', technology = technologies[techId], opinion = form.opinion.data, techId = techId)
    else:
        return render_template('SingleTech.html', technology = technologies[techId], form = form)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
