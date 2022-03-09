from flask import Flask, render_template, request, jsonify, json
app = Flask(__name__)

from pymongo import MongoClient
# import certifi
# ca = certifi.where()

# client = MongoClient('mongodb+srv://test:sparta@cluster0.gmolb.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', tlsCAFile=ca)
client = MongoClient('localhost', 27017)
db = client.dbsparta

## HTML 화면 보여주기
@app.route('/')
def home():
   return render_template('home.html')

@app.route('/login')
def login():
   return render_template('login.html')

@app.route('/all_diary')
def all_diary():
   return render_template('all_diary.html')

@app.route('/contact')
def contact():
   return render_template('contact.html')

@app.route('/admin')
def admin():
   return render_template('admin.html')

@app.route('/manager')
def progress():
   return render_template('manager.html')

@app.route('/my_diary')
def my_diary():
   return render_template('my_diary.html')

@app.route('/write_diary')
def write_diary():
   return render_template('write_diary.html')

# 사용자 가입(POST) API
@app.route('/users', methods=['POST'])
def save_users():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']
    nm_receive = request.form['nm_give']
    chk_author = request.form['au_give']

    # 수정 저장 여부
    chk_btn = request.form['chk_btn']

    # PK 대신 사용
    tmp_id = request.form['tmp_id']
    tmp_pw = request.form['tmp_pw']

    doc = {'id': id_receive,
           'pw': pw_receive,
           'name': nm_receive,
           'author': chk_author
          }

    # 동일한 id가 있는지 확인.
    target_user = db.users.find_one({'id': id_receive}, {'_id': False})

    # 수정인지 저장인지 구분
    if (int(chk_btn) == 0):
        # 동일한 id 여부 확인
        if (target_user):
            return jsonify({'msg': '동일한 ID를 가진 사용자가 있습니다.', 'result': 'error'})

        db.users.insert_one(doc)
        return jsonify({'msg': '가입이 완료되었습니다!', 'result': 'success'})
    else :
        # 동일한 id 여부 확인
        if (target_user):
            if (tmp_id != target_user['id']):
                return jsonify({'msg': '동일한 ID를 가진 사용자가 있습니다.', 'result': 'error'})
            # 변경 사항 여부 확인
            elif (id_receive == target_user['id'] and pw_receive == target_user['pw']
              and nm_receive == target_user['name'] and chk_author == target_user['author']):
                return jsonify({'msg': '변경할 내역이 없습니다.', 'result': 'error'})
        db.users.update_one({'id': tmp_id, 'pw': tmp_pw}, {'$set': doc})
        return jsonify({'msg': '수정 되었습니다!', 'result': 'success'})

# 사용자 삭제(POST) API
@app.route('/users/delete', methods=['POST'])
def delete_users():
    users_data = request.form['users_data']
    
    # JSON API 사용
    json_data = json.loads(users_data)

    for users in json_data:
        db.users.delete_one({'id':users['userid'], 'pw':users['userpw'], 'name':users['name']})

    return jsonify({'msg': '삭제되었습니다!'})

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