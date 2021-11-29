import redis
import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser
from PIL import ImageTk, Image
import ctypes 

client = redis.Redis(host='localhost', port=6379, db=0)
print('ok')
 
window = tk.Tk()
window.title("Welcome to Redis")
window.geometry("300x250")
 
client.zadd( 'sum', {'Peskin':0})
client.zadd( 'sum', {'Bulkin':0})
client.zadd( 'sum', {'Koshkin':0})
client.zadd( 'sum', {'Sonkin':0})

def choose_color():
    color_code = colorchooser.askcolor(title ="Choose color")
    print(color_code[1])
    window.configure(bg=color_code[1])
    
    
def update_top():
    f = client.zrevrange('sum',0, 3, withscores=1)
    f.reverse()
    for sportsman in f:
        sportsmen_listbox.insert(0, sportsman)


# Функция сохранения 
def save_mark():
    mark = text_mark.get()
    if not mark:
        ctypes.windll.user32.MessageBoxW(0, "Введите количество баллов", 
                                         "Ошибка ввода", 0)
        return
    
    sportsman = list_of_sportsmen.get()
    if not sportsman:
        ctypes.windll.user32.MessageBoxW(0, "Введите имя спортсмена", 
                                         "Ошибка ввода", 0)
        return
    
    judge = list_of_judges.get()
    if not judge:
        ctypes.windll.user32.MessageBoxW(0, "Введите имя судьи", 
                                         "Ошибка ввода", 0)
        return    
 
    client.zincrby('sum', mark, sportsman) #сохранение общей суммы 
                                           #баллов поставленной спортсмену
                                           
    client.zincrby(sportsman, mark, judge) #сохранение общей суммы баллов 
                                           #добавленных судьей
    
    text_mark.delete(0, 'end')
    text_mark.insert(0, 'OK')
    
    update_top()



                        # Выбор судьи
                    
label_judges = tk.Label(window, text="Выберите судью")
label_judges.grid(row=0, column=0)
 
 
list_of_judges = ttk.Combobox(window, 
                              values=["Chatsky", "Famusov", "Griboyedov"])
list_of_judges.grid(row=1, column=0)


                        # Выбор спортсмена
                    
label_sportsmen = tk.Label(window, text="Выберите спортсмена")
label_sportsmen.grid(row=2, column=0)
 
list_of_sportsmen = ttk.Combobox(window, 
                                 values=["Bulkin", "Koshkin", 
                                         "Peskin", "Sonkin"])
list_of_sportsmen.grid(row=3, column=0)

 
                         # Ввод баллов 
                         
label_mark = tk.Label(window, text="Введите баллы")
label_mark.grid(row=2, column=2)
 
text_mark = tk.Entry(window, width=25, bd=3)
text_mark.grid(row=3, column=2)


                        # Кнопка сохранения баллов
                        
save_button = tk.Button(window, text="Сохранить", command=save_mark)
save_button.grid(row=4, column=2)
 

                        #Список баллов
                        
label_top = tk.Label(window, text="Рейтинг спортсменов")
label_top.grid(row=5, column=0)

sportsmen_listbox = tk.Listbox(height=4, width=20)
sportsmen_listbox.grid(row = 6, column = 0)
 
update_top()

color = tk.Button(window, text = "Выбрать цвет фона", command = choose_color)
color.grid(row=7, column=0)


















###
### Секретный код!!
###










def make_window():
    window.destroy()
    pic_window = tk.Tk()
    pic_window.title("Lovely kitty!")
    pic_window.geometry("1004x554")
    pic_window.configure(bg='#ffa477')
    
    img = Image.open('kitty.jpg')
    img = img.resize((550, 550), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(img)
    label = tk.Label(pic_window, image=photo)
    label.grid(row=0, column=0, rowspan=2)

    file = open('anec.txt', encoding="utf-8")
    anec = tk.Label(pic_window, 
                    text=file.read(), 
                    font='Sans', 
                    justify='left', 
                    bg='#ffebe1') 
    file.close()
    anec.grid(row=0, column=1, 
              padx=(25, 25), pady=(10,10))
    
    buttom = tk.Button(pic_window, 
                       text="Спасибо, Гриша! :)", 
                       font='Sans', 
                       pady=10, padx=10, 
                       bg='#ff8040', 
                       command=pic_window.destroy)
    buttom.grid(row=1, column=1)
    
    pic_window.mainloop()




#Секретная кнопка!
a = tk.Button(window, 
              text = "СЮРПРИИИИЗ!", 
              bg='#ffa477', 
              command = make_window)
a.grid(row=7, column=2)



window.mainloop()
