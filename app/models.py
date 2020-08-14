from app import db


# Flask Model for items
class items(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(15)) 
    description = db.Column(db.String(30)) 
    location = db.Column(db.String(30)) 
    created_at = db.Column(db.DateTime(30))

    def __init__(self,name,description,location,created_at):
        self.name=name
        self.description=description
        self.location=location
        self.created_at=created_at

# Flask Model for item pics
class item_pic(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    item_id = db.Column(db.Integer(15)) 
    pic_name = db.Column(db.String(10))  

    def __init__(self,item_id,pic_name):
        self.item_id=item_id
        self.pic_name=pic_name

# Flask Model for users
class user(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    username = db.Column(db.String(20)) 
    useremail = db.Column(db.String(20)) 
    password = db.Column(db.String(20)) 

    def __init__(self,username,useremail,password):
        self.username=username
        self.useremail=useremail
        self.password=password