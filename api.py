from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, reqparse, fields, marshal_with, abort

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
api = Api(app)

# Substituição do before_first_request
with app.app_context():
    db.create_all()

# Parser para os dados do usuário
user_args = reqparse.RequestParser()
user_args.add_argument("username", type=str, help="Username is required", required=True)
user_args.add_argument("email", type=str, help="Email is required", required=True)

# Campos para serialização
user_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'email': fields.String
} 

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"User(name={self.username}, email={self.email})"
    
class Users(Resource):
    @marshal_with(user_fields)
    def get(self):
        users = UserModel.query.all()    
        return users
    
    @marshal_with(user_fields)
    def post(self):
        args = user_args.parse_args()
        
        if UserModel.query.filter_by(username=args['username']).first():
            abort(409, message="Username already exists")
        if UserModel.query.filter_by(email=args['email']).first():
            abort(409, message="Email already exists")
            
        user = UserModel(username=args['username'], email=args['email'])
        db.session.add(user)
        db.session.commit()
        return user, 201
        
class User(Resource):
    @marshal_with(user_fields)
    def get(self, id):
        user = UserModel.query.get(id)
        if not user:
            abort(404, message=f"User with id {id} not found")
        return user
    
    @marshal_with(user_fields)
    def patch(self, id):
        args = user_args.parse_args()
        user = UserModel.query.get(id)
        if not user:
            abort(404, message=f"User with id {id} not found")
            
        if args['email'] != user.email and UserModel.query.filter_by(email=args['email']).first():
            abort(409, message="Email already in use by another user")
            
        user.username = args['username']
        user.email = args['email']
        db.session.commit()
        return user
    
    def delete(self, id):
        user = UserModel.query.get(id)
        if not user:
            abort(404, message=f"User with id {id} not found")
            
        db.session.delete(user)
        db.session.commit()
        return '', 204

api.add_resource(Users, "/api/users")       
api.add_resource(User, "/api/users/<int:id>")
 
@app.route('/')
def home():
    return '<h1>Hello World :D</h1>'

if __name__ == '__main__':
    app.run(debug=True)