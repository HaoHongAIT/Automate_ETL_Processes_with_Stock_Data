import SQLAlchemy

# SQL > database
# ORM: python > sqlachemy > sql > database
# 

app.secret_key = '1234567890qwertyuiop'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/news?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


def create_db(app):
return SQLAlchemy(app=app)


app = create_app()
login_manager = LoginManager(app=app)
root_path = app.root_path
phobert_model = load_model(root_path)
# phobert_model = None
db = create_db(app)