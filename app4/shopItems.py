from listItems import app, db, Technology
technologies = [
    { "name": "Headphones", "price": "$99.99", "description": "High-quality headphones for immersive audio experiences.", "image": "headphones.jpg", "basket": False, "enviromentalImpact": "Low" },
    { "name": "Speakers", "price": "$199.99", "description": "Powerful speakers for crystal-clear sound.","image": "speaker.jpg", "basket": False, "enviromentalImpact": "Medium" },
    { "name": "Earphones", "price": "$99.99", "description": "Comfortable earphones for portable listening.", "image": "earphones.jpg", "basket": False, "enviromentalImpact": "Low" },
    { "name": "Smartphone", "price": "$499.99", "description": "A sleek smartphone with advanced features.", "image": "smartphone.jpg", "basket": False, "enviromentalImpact": "High" },
    { "name": "Laptop", "price": "$999.99", "description": "A powerful laptop for work and play.", "image": "laptop.jpg", "basket": False, "enviromentalImpact": "High" },
    { "name": "Tablet", "price": "$299.99", "description": "A versatile tablet for entertainment and productivity.", "image": "tablet.jpg", "basket": False, "enviromentalImpact": "Medium" },
    { "name": "Smartwatch", "price": "$199.99", "description": "A stylish smartwatch to keep you connected.", "image": "smartwatch.jpg", "basket": False, "enviromentalImpact": "Low" },
    { "name": "Gaming Console", "price": "$399.99", "description": "A gaming console for immersive gaming experiences.", "image": "gaming_console.jpg", "basket": False, "enviromentalImpact": "High" },
    { "name": "Camera", "price": "$599.99", "description": "A high-resolution camera for capturing memories.", "image": "camera.jpg", "basket": False, "enviromentalImpact": "Medium" },
    ]

with app.app_context():
    db.create_all() # creates the empty tables
    
    # Clear existing data to avoid unique constraint violations
    Technology.query.delete()
    db.session.commit()
    
    for tech in technologies:
        newTech = Technology(name=tech["name"], price=tech["price"], description=tech["description"], enviromentalImpact=tech["enviromentalImpact"])
        db.session.add(newTech)
    
    db.session.commit()
