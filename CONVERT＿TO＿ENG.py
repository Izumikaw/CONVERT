#!/usr/bin/env python
# coding: utf-8

# In[11]:


import tkinter as tk
import tkinter.ttk as ttk

morses = {"・－": "A","－・・・": "B","－・－・": "C","－・・": "D","・": "E","・・－・": "F",
              "－－・": "G","・・・・": "H","・・": "I","・－－－": "J","－・－": "K","・－・・": "L",
              "－－": "M","－・": "N","－－－": "O","・－－・": "P","－－・－": "Q","・－・": "R",
              "・・・": "S","－": "T","・・－": "U","・・・－": "V","・－－": "W","－・・－": "X","－・－－": "Y","－－・・": "Z",
         "・－・－・－": ".","－－・・－": ",－","・・－－・・": "?","・－・－・": "+","－・・・－": "=","－・・－": "*"
}
#変換
def morse_to_eng(M):
    Ms=M.replace('　',' ').split(' ')
    ENG = [morses[s] for s in Ms if s in morses]       
    return '    '.join(ENG)

# クリックイベント
def btn_click():
    global lbl_2
    M = txt_1.get()
    Answer = morse_to_eng(M)
    lbl_2 = tk.Label(text="このモールス信号は  "+Answer+"  です。")
    lbl_2.pack()
    lbl_2.place(x=30, y=100)

#テキストボックス、ラベルをクリア
def clear():
    txt_1.delete(0,tk.END)
    lbl_2.destroy()
    
#終了ボタン
def end():
    tki.destroy()  

tki = tk.Tk()
tki.geometry('600x200')
tki.title('TEXT -> MORSE')

# ラベル
lbl1_frame = ttk.Label(text='文字を入力')
lbl1_frame.place(x=30, y=70)

# テキストボックス
txt_1 = ttk.Entry(width=60)
txt_1.place(x=100, y=70)

# 変換ボタン
btn_1 = ttk.Button(tki, text='変換',width=10, command=btn_click)
btn_1.place(x=70, y=170)

#クリアボタン
btn_2 = ttk.Button(text='クリア',width=10 , command = clear)
btn_2.place(x=480, y =70)

#閉じるボタン
btn_3 = ttk.Button(text='終了', width=10, command = end)
btn_3.place(x=500, y =170)

tki.mainloop()


# In[ ]:





# In[ ]:




