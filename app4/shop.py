from flask import Flask, render_template, request, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_bootstrap import Bootstrap
from listItems import app as list_app, db, Technology

app = list_app

class OpinionForm(FlaskForm):
    opinion = StringField('Your Opinion: ',validators = [DataRequired(),Length(min=0,max=100)])
    submit = SubmitField('Submit')

@app.route('/')
def galleryPage():
    technologies = Technology.query.all()
    return render_template('index.html', technologies=technologies)

@app.route('/tech/<int:techId>', methods=['GET', 'POST'])
def singleProductPage(techId):
    technology = Technology.query.get_or_404(techId)
    form = OpinionForm()
    if form.validate_on_submit():
        pass
    return render_template('SingleTech.html', technology=technology, form=form)

@app.route('/add_to_basket/<int:techId>')
def add_to_basket(techId):
    if 'basket' not in session:
        session['basket'] = []
    
    technology = Technology.query.get_or_404(techId)
    image_map = {'Headphones': 'headphones.jpg', 'Speakers': 'speakers.jpg', 'Earphones': 'earphones.jpg'}
    basket_item = {
        'id': technology.id,
        'name': technology.name,
        'price': technology.price,
        'image': image_map.get(technology.name, f"{technology.name.lower()}.jpg")
    }
    
    # Check if item already in basket
    for item in session['basket']:
        if item['id'] == techId:
            break
    else:
        session['basket'].append(basket_item)
    
    session.modified = True
    return redirect(url_for('galleryPage'))

@app.route('/basket')
def view_basket():
    basket_items = session.get('basket', [])
    return render_template('basket.html', basket_items=basket_items)

@app.route('/remove_from_basket/<int:techId>')
def remove_from_basket(techId):
    if 'basket' in session:
        session['basket'] = [item for item in session['basket'] if item['id'] != techId]
        session.modified = True
    return redirect(url_for('view_basket'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
