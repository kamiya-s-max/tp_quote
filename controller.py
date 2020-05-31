class Controller(object):
    def __init__(self, master, model, view):
        self.master = master
        self.model = model
        self.view = view

    # ボタンクリック時の処理を定義
    def btn_submit_clicked(self):
        # モデルのメソッドを呼び出し
        self.model.hello_execute()
