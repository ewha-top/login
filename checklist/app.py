from flask import Flask, request, redirect, url_for, session, render_template
from models import db, User
from flask import flash

app = Flask(__name__)
app.secret_key = 'your_secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # 또는 MySQL URI
db.init_app(app)


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login_id = request.form['loginId']
        login_pw = request.form['loginPw']
        existing_user = User.query.filter_by(login_id=login_id).first()
        if existing_user:
            flash("이미 존재하는 ID입니다. 다른 ID로 시도하세요.")
            return render_template('login.html', login=False)
        # 사용자 정보 DB에 저장
        new_user = User(login_id=login_id, login_pw=login_pw)
        db.session.add(new_user)
        db.session.commit()

        session['username'] = login_id
        return redirect(url_for('todo'))

    return render_template('login.html', login=False)

@app.route('/todo')
def todo():
    if 'username' in session:
        return render_template('todo.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
