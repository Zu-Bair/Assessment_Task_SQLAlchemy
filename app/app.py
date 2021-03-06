from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:''@localhost/task_sqlalchemy'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = True

    db.init_app(app)

    with app.app_context():
        import routes 
        db.create_all()
        db.session.commit()

        return app

app = create_app()

if __name__ == '__main__':
    app.run(host='127.0.0.1')