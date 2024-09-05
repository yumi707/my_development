from flask import Flask,render_template,request,redirect,url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

@app.route('/upload', methods=["GET","POST"])
def upload():
    # POSTの場合
    if request.method == 'POST':
        # ファイルを取り出す
        file = request.files.get('file')
        # ファイル名を安全な形式に変換
        save_filename = secure_filename(file.filename) 
        # 静的コンテンツのデフォルトの場所の絶対パスを取得してファイル名と繋げる
        file.save(os.path.join(app.static_folder,save_filename))
        
        return render_template('uploaded.html',file_name=save_filename)
    
    # GETの場合
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
