import tkinter as tk

class View(object):
    def __init__(self, master, model):
        self.master = master
        self.model = model

        # 画面パーツの生成
        # 入力欄ラベル
        self.lbl_choice = tk.Label(
            master,
            text='入力'
        )

        # 入力欄
        self.ent_choice = tk.Entry(
            master,
            textvariable=model.ent_choice_text,
            width=30
        )

        # 送信ボタン
        self.btn_submit = tk.Button(
            master,
            text="メッセージを送信"
        )

        # 出力欄ラベル
        self.lbl_message = tk.Label(
            master,
            textvariable=model.lbl_message_text
        )

        # 画面パーツを配置
        self.lbl_choice.grid(row=0, column=0)
        self.ent_choice.grid(row=0, column=1)
        self.btn_submit.grid(row=0, column=2)

        self.lbl_message.grid(row=1, column=1)



