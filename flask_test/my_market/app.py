from flask import Flask,render_template

app = Flask(__name__)

class GetItems:
    def __init__(self,product_name,price,color,picture_pass,supplier):
        self.product_name = product_name
        self.price = price
        self.color = color
        self.picture_pass = picture_pass
        self.supplier = supplier

item_list = [
    GetItems("イヤホン",15000,"赤","/images/buds_earphone","輸入"),
    GetItems("ヘッドホン",36000,"白","/images/headphone","国内"),
    GetItems("キーボード",8200,"アイボリー","/images/keyboard","国内"),
    GetItems("マウス",5700,"黒","/images/mouse","輸入"),
]

menus = ["このショップについて","商品一覧","よくあるご質問","商品ご購入の際の注意事項"]

@app.route("/top")
def top():
    return render_template("top.html",menus=menus)

@app.route("/itemlist")
def itemlist():
    return render_template("itemlist.html")

if __name__ == '__main__':
    app.run(debug=True)