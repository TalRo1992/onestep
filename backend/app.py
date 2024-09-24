from flask import Flask
from models import db
from scraper import save_case_studies
from routes.case_studies import case_studies_bp
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)
app.register_blueprint(case_studies_bp)


@app.before_first_request
def setup():
    db.drop_all() 
    db.create_all()
    save_case_studies()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
