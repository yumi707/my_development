from flask import Flask,render_template,abort

app = Flask(__name__)

class GetItems:
    def __init__(self,id,product_name,price,color,picture_pass,supplier):
        self.id = id
        self.product_name = product_name
        self.price = price
        self.color = color
        self.picture_pass = picture_pass
        self.supplier = supplier

item_list = [
    GetItems(1,"イヤホン",15000,"赤","images/buds_earphone.jpg","輸入"),
    GetItems(2,"ヘッドホン",36000,"白","images/headphone.jpg","国内"),
    GetItems(3,"キーボード",8200,"アイボリー","images/keyboard.jpg","国内"),
    GetItems(4,"マウス",5700,"黒","images/mouse.jpg","輸入"),
]

@app.template_filter('check_postage')
def check_postage_filter(supplier,price):
    postage = 500
    if supplier == "輸入":
        postage += 1000
    if price >= 10000:
        postage -= 600
    if postage < 0:
        postage = 0
    return postage

about = {"このショップについて": "バイヤーが厳選した商品を取り揃えております"}
item_lists = {"商品一覧": "商品をチェック"}
qa = {"よくあるご質問": "Q&Aです"}
precautions = {"商品ご購入の際の注意事項": "商品到着から8日以内のキャンセルは承ります"}
menus = [about,item_lists,qa,precautions]

@app.route("/top")
def top():
    return render_template("top.html",menus=menus)

@app.route('/itemlist')
def itemlist():
    return render_template("itemlist.html",item_list=item_list)


@app.route("/item/<int:item_id>")
def item_detail(item_id):
    for item in item_list:
        if item_id == item.id:
            return render_template("item_detail.html",item=item)

@app.errorhandler(404)
def page_not_found(error):
    return render_template("not_found.html"),404

if __name__ == '__main__':
    app.run(debug=True)