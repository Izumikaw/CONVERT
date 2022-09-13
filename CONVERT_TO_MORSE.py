#!/usr/bin/env python
# coding: utf-8

# In[3]:


import tkinter as tk
import tkinter.ttk as ttk

words = {"A": "A・－","B": "B－・・・","C": "C－・－・","D": "D－・・","E": "E・","F": "F・・－・",
              "G": "G－－・","H": "H・・・・","I": "I・・","J": "J・－－－","K": "K－・－","L": "L・－・・",
              "M": "M－－","N": "N－・","O": "O－－－","P": "P・－－・","Q": "Q－－・－","R": "R・－・",
              "S": "S・・・","T": "T－","U": "U・・－","V": "V・・・－","W": "W・－－","X": "X－・・－","Y": "Y－・－－","Z": "Z－－・・",
         "a": "a・－","b": "b－・・・","c": "c－・－・","d": "d－・・","e": "e・","f": "f・・－・",
              "g": "g－－・","h": "h・・・・","i": "i・・","j": "j・－－－","k": "k－・－","l": "l・－・・",
              "m": "m－－","n": "n－・","o": "o－－－","p": "p・－－・","q": "q－－・－","r": "r・－・",
              "s": "s・・・","t": "t－","u": "u・・－","v": "v・・・－","w": "w・－－","x": "x－・・－","y": "y－・－－","z": "z－－・・",
         "あ": "あ－－・－－","い": "い・－","う": "う・・－","え": "え－・－－－","お": "お・－・・・","か": "か・－・・",
              "き": "き－・－・・","け": "け－・－－","こ": "こ－－－－","さ": "さ－・－・－","し": "し－－・－・","す": "す－－－・－",
              "せ": "せ・－－－・","そ": "そ－－－・","た": "た－・","ち": "ち・・－・","つ": "つ・－－・","て": "て・－・－－",
              "と": "と・・－・・","な": "な・－・","に": "に－・－・","ぬ": "ぬ・・・・","ね": "ね－－・－","の": "の・・－－",
              "ま": "ま－・・－","は": "は－・・・","ひ": "ひ－－・・－","ふ": "ふ－－・・","へ": "へ・","ほ": "ほ－・・",
              "み": "み・・－・－","む": "む－","め": "め－・・・－","も": "も－・・－・","や": "や・－－","ゆ": "ゆ－・・－－",
              "よ": "よ－－","ら": "ら・・・","り": "り－－・","る": "る－・－－・","れ": "れ－－－","ろ": "ろ・－・－",
              "わ": "わ－・－","を": "を・－－－","ん": "ん・－・－・","く": "く・・・－",
         "が": "か・－・・ ゛・・","ぎ": "き－・－・・ ゛・・","ぐ": "く・・・－ ゛・・","げ": "け－・－－ ゛・・",
              "ご": "こ－－－－ ゛・・","ざ": "さ－・－・－ ゛・・","じ": "し－－・－・ ゛・・","ず": "す－－－・－ ゛・・",
              "せ": "せ・－－－・ ゛・・","そ": "そ－－－・ ゛・・","だ": "た－・ ゛・・","ぢ": "ち・・－・ ゛・・",
              "づ": "つ・－－・ ゛・・","で": "て・－・－－ ゛・・","ど": "と・・－・・ ゛・・",
              "ば": "は－・・・ ゛・・","び": "ひ－－・・－ ゛・・","ぶ": "ふ－－・・ ゛・・","べ": "へ・ ゛・・",
              "ぼ": "ほ－・・ ゛・・","ぱ": "は－・・・ ゜・・－－・","ぴ": "ひ－－・・－ ゜・・－－・",
              "ぷ": "ふ－－・・ ゜・・－－・","ぺ": "へ・ ゜・・－－・","ぽ": "ほ－・・ ゜・・－－・",
         ".": ".(period)・－・－・－",",": ",(comma)－－・・－－","?": "?・・－－・・","+": "+・－・－・",
              "=": "=－・・・－","*": "*－・・－"
}

def eng_to_morse(M):
    ENG = [words[s] for s in M if s in words]       
    return '    '.join(ENG)

# クリックイベント
def btn_click():
    global lbl_2
    M = txt_1.get()
    Answer = eng_to_morse(M)
    lbl_2 = tk.Label(text="モールス信号は  "+Answer+"  です。")
    lbl_2.pack()
    lbl_2.place(x=30, y=100)

#テキストボックス、ラベルをクリア
def clear():
    txt_1.delete(0,tk.END)
    lbl_2.destroy()
    
#終了ボタン
def end():
    tki.destroy()

'''def T_to_M():
    global frame
    frame_app.destroy()

    # メインフレームの作成と設置
    frame = ttk.Frame(tki)
    frame.pack(fill = tk.BOTH, pady=20)
    
    #メニューバー作成 
    men = tkinter.Menu(tki) 
    #メニューバーを画面にセット 
    tki.config(menu=men) 
    #メニューに親メニュー（ファイル）を作成する 
    menu_file = tkinter.Menu(tki) 
    men.add_cascade(label='METHOD', menu=menu_file) 
    #親メニューに子メニュー（開く・閉じる）を追加する 
    menu_file.add_command(label='Text to Morse', command=T_to_M) 
    menu_file.add_separator() 
    menu_file.add_command(label='Morse to Text', command=M_to_T)
    # ラベル
    lbl_1 = tkinter.Label(text='文字を入力')
    lbl_1.place(x=30, y=70)
    # テキストボックス
    txt_1 = tkinter.Entry(width=60)
    txt_1.place(x=100, y=70)
    # 変換ボタン
    btn_1 = tkinter.Button(tki, text='変換',width=10, command=btn_click)
    btn_1.place(x=70, y=170)
    #クリアボタン
    btn_2 = tkinter.Button(text='クリア',width=10 , command = clear)
    btn_2.place(x=480, y =70)
    #閉じるボタン
    btn_3 = tkinter.Button(text='終了', width=10, command = end)
    btn_3.place(x=500, y =170)

def M_to_T():
    global frame_app
    tki.title('MORSE -> TEXT')
    
    frame.destroy()
    
    frame_app = ttk.Frame(tki)
    frame_app.pack(fill = tk.BOTH, pady=20)
    
    #メニューバー作成 
    men = tkinter.Menu(tki) 
    #メニューバーを画面にセット 
    tki.config(menu=men) 
    #メニューに親メニュー（ファイル）を作成する 
    menu_file = tkinter.Menu(tki) 
    men.add_cascade(label='METHOD', menu=menu_file) 
    #親メニューに子メニュー（開く・閉じる）を追加する 
    menu_file.add_command(label='Text to Morse', command=T_to_M)
    menu_file.add_separator() 
    menu_file.add_command(label='Morse to Text', command=M_to_T)
    # ラベル
    lbl_1 = tkinter.Label(text='文字を入力')
    lbl_1.place(x=30, y=70)
    # テキストボックス
    txt_1 = tkinter.Entry(width=60)
    txt_1.place(x=100, y=70)
    # 変換ボタン
    btn_1 = tkinter.Button(tki, text='変換',width=10, command=btn_click)
    btn_1.place(x=70, y=170)
    #クリアボタン
    btn_2 = tkinter.Button(text='クリア',width=10 , command = clear)
    btn_2.place(x=480, y =70)
    #閉じるボタン
    btn_3 = tkinter.Button(text='終了', width=10, command = end)
    btn_3.place(x=500, y =170)'''
   


tki = tk.Tk()
tki.geometry('600x200')
tki.title('TEXT -> MORSE')

#frame = ttk.Frame(tki)
#frame.pack(fill = tk.BOTH, pady=20)

#メニューバー作成 
#men = tk.Menu(tki) 

#メニューバーを画面にセット 
#tki.config(menu=men) 

#メニューに親メニュー（ファイル）を作成する 
#menu_file = tk.Menu(tki) 
#men.add_cascade(label='METHOD', menu=menu_file) 

#親メニューに子メニュー（開く・閉じる）を追加する 
#menu_file.add_command(label='Text to Morse', command=T_to_M) 
#menu_file.add_separator() 
#menu_file.add_command(label='Morse to Text', command=M_to_T)

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




