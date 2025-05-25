from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)       # 고유 ID (자동 증가)
    login_id = db.Column(db.String(80), unique=True)   # 로그인 ID (유니크)
    login_pw = db.Column(db.String(120))                # 비밀번호
    
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200))
    due_date = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    #ForeignKey : 다른 테이블의 특정 컬럼 참조 -> 두 테이블 연결