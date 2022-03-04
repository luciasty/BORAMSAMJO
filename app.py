from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
# import certifi
# ca = certifi.where()

# client = MongoClient('mongodb+srv://test:sparta@cluster0.gmolb.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', tlsCAFile=ca)
client = MongoClient('localhost', 27017)
db = client.dbsparta

## HTML 화면 보여주기
@app.route('/')
def login():
   return render_template('login.html')

@app.route('/main')
def main():
   return render_template('main.html')

@app.route('/contact')
def contact():
   return render_template('contact.html')

@app.route('/admin')
def admin():
   return render_template('admin.html')

# 사용자 가입(POST) API
@app.route('/users', methods=['POST'])
def save_users():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']
    nm_receive = request.form['nm_give']
    chk_author = 2

    doc = {'id': id_receive,
           'pw': pw_receive,
           'name': nm_receive,
           'author': chk_author
          }
    db.users.insert_one(doc)

    return jsonify({'msg': '가입이 완료되었습니다!'})

# 사용자 목록보기(GET) API
@app.route('/users', methods=['GET'])
def view_users():
    users_info = list(db.users.find({}, {'_id': False}))

    return jsonify({'users_info': users_info})

@app.route('/login', methods=['GET', 'POST'])
def chk_users():
    id_receive = request.form['loginId_give']
    pw_receive = request.form['loginPw_give']

    users_info = list(db.users.find({}, {'_id': False}))
    for user in users_info:
        if (id_receive == user['id'] and pw_receive == user['pw']):
            return jsonify({'msg': '로그인 되었습니다!', 'user_info': user})
        pass

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)