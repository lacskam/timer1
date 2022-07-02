import random
import datetime
import threading
from time import sleep
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle
Window.size =(480,640)
from kivymd.uix.button import MDIconButton

start = 0
def getMounts():
    delta = datetime.datetime.now() - datetime.datetime(2021, 8, 20)
    mounts = int(delta.days/30.6)
    return mounts


def getDays():
    delta = datetime.datetime.now() - datetime.datetime(2021, 8, 20)
    days = int(delta.days % 30.5)
    return days



def getHours():
    delta = datetime.datetime.now() - datetime.datetime(2021, 8, 20)
    hours = delta.seconds // 3600
    return hours

def getMinots():
    delta = datetime.datetime.now() - datetime.datetime(2021, 8, 20)
    minots = (delta.seconds % 3600) // 60
    return minots


def getSeconds():
    delta = datetime.datetime.now() - datetime.datetime(2021, 8, 20)
    seconds = delta.seconds % 60
    return seconds
stop = False



class MyApp(MDApp):


    x=0
    secret = 0
    def updateText(self,instance):
        list = ["Люблю тебя, очень!","Очень-преочень люблю!","Ты самая милая",
        "Дороже тебя у меня нет никого!","Ты самая лучшая!","Я безумно рад что встретил тебя!",
        "Ты - лучший момент моей жизни","Как же я хочу тебя обнять!"]
        if self.secret >=1 and self.secret <=2:
            if self.secret == 1:
                self.lbt2.text = "Или это приложение удалиться!"
                self.secret+=1
            elif self.secret ==2:
                self.lbt2.text = "Шутю ^_^, жмякай сколько хочешь!"
                self.secret=5
        else:
            if self.x == 0:
                self.lbt2.text = "Ой..., ты всё таки нашла эту пасхалку..."
            else:
                
                self.lbt2.text= list[random.randrange(len(list))]
            self.x+=1
            if self.x>10 and self.secret==0:
                if random.randint(1,7) == 3:
                    self.lbt2.text="Ну хватит, хихихихи"
                    self.secret +=1
        
        



    def build(self):
        
        screen = Screen()
        with screen.canvas:
            
            Rectangle(pos=(0,0),size_hint=(1,1),size=(480,640),source="fon.jpg")
        bl = BoxLayout(orientation="vertical",size_hint=(.6,.4),pos_hint={"center_x":.5,"center_y":.5},padding=(0,0,0,0))
        lbt = MDLabel(text="Мы вместе",font_style="H3",halign="center",theme_text_color="Custom",text_color= (1, 1, 1, 1),
        pos_hint={"center_x":.5,"center_y":.75})
        self.lbt2 = MDLabel(text="Надеюсь этот таймер никогда не остановится   .",font_style="H6",halign="center",theme_text_color="Custom",text_color= (1, 1, 1, 1),
        pos_hint={"center_x":.5,"center_y":.05})
        btn = MDIconButton(icon="heart",theme_text_color="Custom",text_color=(1, 1, 1, 1),pos_hint={"center_x":.96,"center_y":.05},on_press=self.updateText)
        lb1 = MDLabel(text="2131",font_style="H4",halign="center",theme_text_color="Custom",text_color= (1, 1, 1, 1))
        lb2 = MDLabel(text="2131",font_style="H4",halign="center",theme_text_color="Custom",text_color= (1, 1, 1, 1))
        lb3 = MDLabel(text="2131",font_style="H4",halign="center",theme_text_color="Custom",text_color= (1, 1, 1, 1))
        lb4 = MDLabel(text="2131",font_style="H4",halign="center",theme_text_color="Custom",text_color= (1, 1, 1, 1))
        lb5 = MDLabel(text="2131",font_style="H4",halign="center",theme_text_color="Custom",text_color= (1, 1, 1, 1))
       
    
        bl.add_widget(lb1)
        bl.add_widget(lb2)
        bl.add_widget(lb3)
        bl.add_widget(lb4)
        bl.add_widget(lb5)
        screen.add_widget(bl)
        screen.add_widget(lbt)
        screen.add_widget(self.lbt2)
        screen.add_widget(btn)
        

        def updadateLabel():
            while not stop:
                im = ""
                if (getMounts()>4):
                    im = " месяцев" 
                elif getMounts()==1 or getMounts()==21 or getMounts()==31:
                    im = " месяц" 
                else: im = " месяца"

                lb1.text = (str(getMounts()) + im)


                id =""
                if getDays()==1 or getDays()==21 or getDays()==31:
                    id = " день"
                elif (getDays()<5 and getDays()>1 or getDays()>21 and getDays()<25): 
                    id = " дня"
                else: id = " дней"

                lb2.text = (str(getDays())+id)

                ih =""
                if (getHours()==1 or getHours()==21):
                   ih = " час"
                
                elif (getHours()<5 and getHours()>1 or getHours()>21 and getHours()<25):
                    ih = " часа"
                else: ih = " часов"
                lb3.text = (str(getHours())+ih)

                im =""
                if (getMinots()==1 or getMinots()==21 or getMinots()==31 or getMinots()==41 or getMinots()==51):
                    im = " минуту"
                
                elif (getMinots()<5 and getMinots()>1 or getMinots()>21 and getMinots()<25 or getMinots()>31 and getMinots()<35 or getMinots()>41 and getMinots()<45 or getMinots()>51 and getMinots()<55):
                    im = " минуты"
                else: im = " минут"

                lb4.text = (str(getMinots())+im)


                isec =""
                if (getSeconds()==1 or getSeconds()==21 or getSeconds()==31 or getSeconds()==41 or getSeconds()==51):
                    isec = " секунду"
                
                elif (getSeconds()<5 and getSeconds()>1 or getSeconds()>21 and getSeconds()<25 or getSeconds()>31 and getSeconds()<35 or getSeconds()>41 and getSeconds()<45 or getSeconds()>51 and getSeconds()<55):
                    isec = " секунды"
                else: isec = " секунд"
                lb5.text = (str(getSeconds())+isec)
                sleep(1)
                
                    
        t1 = threading.Thread(target=updadateLabel,args=(),name="t1",daemon=True)
        t1.start()
        
        return screen
    
   
    

if __name__ =="__main__":
    MyApp().run()
