from listItems import app, db, Technology
technologies = [
    { "name": "Headphones", "price": "$99.99", "description": "High-quality headphones for immersive audio experiences.", "image": "headphones.jpg", "basket": False },
    { "name": "Speakers", "price": "$199.99", "description": "Powerful speakers for crystal-clear sound.","image": "speaker.jpg", "basket": False },
    { "name": "Earphones", "price": "$99.99", "description": "Comfortable earphones for portable listening.", "image": "earphones.jpg", "basket": False },
    ]

with app.app_context():
    db.create_all() # creates the empty tables
    
    for tech in technologies:
        newTech = Technology(name=tech["name"], price=tech["price"], description=tech["description"])
        db.session.add(newTech)
    
    db.session.commit()
