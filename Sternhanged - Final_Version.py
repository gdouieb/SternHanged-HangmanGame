#
#
# Beta_02 : ajout page de choix du niveau.


from tkinter import *
import tkinter as tk, threading
import imageio
import csv, random
from PIL import Image, ImageTk
from pprint import pprint
import pandas as pd
from tkinter import messagebox



#Tkinter window and a parameters of window

root = tk.Tk()
root.title("Sternhanged")
# root.attributes('-fullscreen', True)
# root.resizable(False,False)
root.config(background = 'black')
# root.iconbitmap("static/hang_logo.ico")

#Creation of videos and images into variables that we will be able to use
video_name = "static/skull.mp4"
video = imageio.get_reader(video_name)

first_step= (Image.open("static/step2.png"))
step_one= first_step.resize((1358,957), Image.ANTIALIAS)
step_1= ImageTk.PhotoImage(step_one)

second_step= (Image.open("static/step3.png"))
step_two= second_step.resize((1358,957), Image.ANTIALIAS)
step_2= ImageTk.PhotoImage(step_two)

third_step= (Image.open("static/step4.png"))
step_three= third_step.resize((1358,957), Image.ANTIALIAS)
step_3= ImageTk.PhotoImage(step_three)

fourth_step= (Image.open("static/step5.png"))
step_four= fourth_step.resize((1358,957), Image.ANTIALIAS)
step_4= ImageTk.PhotoImage(step_four)

final_step = (Image.open("static/stepfinal.png"))
last_step= final_step.resize((1358,957), Image.ANTIALIAS)
finalstep= ImageTk.PhotoImage(last_step)

Accueil= (Image.open("static/step1.png"))
AccMenu= Accueil.resize((1358,957), Image.ANTIALIAS)
WelcomeMenu= ImageTk.PhotoImage(AccMenu)

###############################################################################

########################### main frames & labels ###################################

# Main title label
welcometitle = Label(root, bg = "black", text = "Are you ready to be Sternhanged ?", font = ("Chiller", 46),  fg = "yellow",borderwidth = 0,  height = 1, pady=50)
welcometitle.pack(side = TOP, fill = Y)

# frame to contain the left menu : buttons GAME , LEVELS, RULES, EXIT
frame_menu = Frame(root, borderwidth=0, bg="black", padx=50)
frame_menu.pack(side = LEFT, fill = Y)

# frame to contain the game itself : keyboard, word, hangman pictures etc.
gameFrame = Frame(root, borderwidth=0,  padx=50, bg="black")
gameFrame.pack(side = LEFT, fill = 'both', expand=True)

# frame to contain the 'level choice' widgets
level_container_frame = Frame(root, borderwidth=0,  padx=50, bg="black")

# frame to contain the rules of the game


#Label used for intro video only
my_label = tk.Label(gameFrame, bg = "green", borderwidth=0, highlightthickness = 0)
my_label.place(bordermode=OUTSIDE, rely = 0.0, relx = 0.0, anchor = NW)

'''
scoreBoard = Frame(root, borderwidth=0, bg="black", padx=50, width=200)
scoreBoard.pack(side = LEFT, fill = Y)
'''

####################### LEVEL CHOICE #####################################################




welcometitle = Label(level_container_frame, bg = "black", text = "Choose your level MORTAL ", font = ("goudy stout", 20),  fg = "yellow",  height = 2)
welcometitle.pack(side = TOP, fill = "both", expand = False)

    # 1er frame
frame_btn1 = Frame(level_container_frame, borderwidth=0, bg="black")
frame_btn1.pack(side = TOP, padx = 5, pady=20)

    # 2em frame
frame_btn2 = Frame(level_container_frame, borderwidth=0, bg="black")
frame_btn2.pack(side = TOP, padx = 5,pady=25)

    # 3em frame
frame_btn3 = Frame(level_container_frame, borderwidth=0, bg="black")
frame_btn3.pack(side = TOP, padx = 5,pady=30)

    # 4em frame
frame_btn4 = Frame(level_container_frame, borderwidth=0, bg="black")
frame_btn4.pack(side = BOTTOM, padx = 5,pady=30)

    # Ajouter le gif dans le frame
img=Image.open("./static/giphy.gif")



    # label qui affiche le niveau , après avoir appuyé sur les buttons
# lbl_niveau=Label(level_container_frame,text="niveau choisi:" ,font = ("AnotherScream", 18), bg="BLACK", fg="white")
# lbl_niveau.place(x=7,y=160)

# la variable qui envoie la valeur de nivea, pour choisir la dificulté
niveau=""

    # les defiitions suffisantes sont pour affecter la variable 'niveau' , à la valeur (niveau) choisie par le joueur
def niveau_easy():
    global niveau
    niveau ="EASY"
    # lbl_niveau.configure(text="votre niveau : EASY (mdr)")
    butlevel['text']="LEVEL\n(easy)"
    print(niveau)

def niveau_medium():
    global niveau
    niveau="MEDIUM"
    # lbl_niveau.config(text="votre niveau : MEDIUM (encore mdr)")
    butlevel['text']="LEVEL\n(medium)"
    print(niveau)

def niveau_hard():
    global niveau
    niveau="HARD"
    # lbl_niveau.config(text="votre niveau : HARD (First time ?)")
    butlevel['text']="LEVEL\n(hard)"
    print(niveau)

# def btn_quit():
#     win.destroy()


    # Button EASY
btn_easy = Button(frame_btn1, bg = 'black',font = ("AnotherScream", 20), fg = "blue", text = "EASY ( scared! )",command=niveau_easy, height =2, width = 16)
btn_easy.pack(padx = 20)

    # Button MEDIUM
btn_medium = Button(frame_btn2,bg = 'black',font = ("AnotherScream", 20), fg = "yellow", text = "MEDIUM ( still scared! ) ",command=niveau_medium, height =2, width = 16)
btn_medium.pack(padx = 20)

    # Button HARD
btn_hard = Button(frame_btn3, bg = 'black',font = ("AnotherScream", 20), text = "HARD ( you'll DIE! )",command=niveau_hard, fg = "red", height =2, width = 16)
btn_hard.pack(padx = 20)

#     # Button QUIT
# btn_quit= Button(frame_btn4, bg = 'black',command=btn_quit,font = ("AnotherScream", 20), text = "QUIT ( panicky ! )", fg = "red", height = 2, width = 16)
# btn_quit.pack(padx = 20)

    # Les labels suivants sont pour afficher le gif , à droit et à gauche
lbl_gif_right=Label(level_container_frame)
lbl_gif_right.place(x=1350,y=350)

lbl_gif_left=Label(level_container_frame)
lbl_gif_left.place(x=50,y=350)



####################### Background animation of the hangman #####################################################


#Labels to be sorted only on this order
#Labels are displayed on each other starting by step 6 to step 1
#Once an error is made, step1 is forget(). Two errors, step2 is forget() and so on

step6 = Label(gameFrame, image=finalstep, relief = FLAT, bg = "black", borderwidth=0, highlightthickness = 0)
step5 = Label(gameFrame, image=step_4, relief = FLAT, bg = "black", borderwidth=0, highlightthickness = 0)
step4 = Label(gameFrame, image=step_3, relief = FLAT, bg = "black", borderwidth=0, highlightthickness = 0)
step3 = Label(gameFrame, image=step_2, relief = FLAT, bg = "black", borderwidth=0, highlightthickness = 0)
step2 = Label(gameFrame, image=step_1, relief = FLAT, bg = "black", borderwidth=0, highlightthickness = 0)
step1 = Label(gameFrame, image=WelcomeMenu, relief = FLAT, bg = "black", borderwidth=0, highlightthickness = 0)


##################################################################################################


def get_word():
    '''returns a city name selected randomly from database db_pendu, or from csv file if db conn fails'''
    try:
        return get_word_sql(2)
    except:
        print("something wrong with connexion to DB")
        pass
    print("using csv instead")
    return get_word_csv()


def get_word_sql(level):

    levels = {0:100000,1:50000,2:0}

    conn = psycopg2.connect(dbname="db_pendu", user="python", password="thonpy", host="localhost")
    print(conn.closed)
    cur = conn.cursor()
    table = "tb_villes"

    sql_request = f"SELECT nom_ville FROM {table} WHERE population_ville > {levels[level]} ORDER BY RANDOM() LIMIT 1"
    # sql_request = f"SELECT nom_ville FROM {table} ORDER BY RANDOM() LIMIT 1"
    # sql_request = f"select count(id_ville) from {table}"
    print(sql_request)
    cur.execute(sql_request)
    # conn.commit()
    records = cur.fetchall()
    word = records[0][0]
    # close cursor and conn
    cur.close()
    conn.close()

    print(f"word from  get_word using SQL database : {word}")
    return(word)


def get_word_csv():
    global niveau

    df = pd.read_csv(r"villes_france.csv", sep=',',header = None ,encoding="utf-8" 
    ,usecols=[1,3,8,14,20,19]
    ,names=['departement','nom', 'code_postal','population', 'latitude','longitude']
    )
    # memo : 
    # nom_ville, code_postal_ville, population_ville, departement_ville, latitude_ville, longitude_ville)
    # '{row[3]}'     '{row[8]}'        '{row[14]}'          '{row[1]}'      '{row[20]}'     '{row[19]}'

    niveau_settings = {'EASY':50000,'MEDIUM':10000, 'HARD':0}
    # niveau par defaut :
    if not niveau:
        niveau = 'MEDIUM'
    
    # selection aleatoire d'1 nom de ville , en fonction du niveau choisi : 
    df_niveau = df.loc[df['population']>= niveau_settings[niveau],:]
    ville = df_niveau.sample()['nom'].item()
    print(f"ville choisie : {str(ville)}")
    return(ville)


def init_user_word(word):
    '''creates and returns the initial user_word list : a list of _ and - and ' based on word to guess given in parameter'''
    w=[]
    for character in word:
        # replace letters by UNDERSCORE
        if 65<=ord(character)<=90:
            w.append("_")
        # keep APOSTROPHE
        elif ord(character)==39:
            w.append("'")
        # replace all other characters by DASH
        else:
            w.append("-")
    return(w)


def try_letter(letter):

    # try:

    global errors, error_limit, user_word, word, buttons, lives, score

    # if max errors not reached and letter not null,
    if (errors < error_limit) and letter:

        # if the letter hasn't been tried yet ,
        if letter not in tried:

            # lock corresponding keyboard button
            buttons[letter].configure(state = DISABLED)

            # add the letter to the list of tried letter
            tried.append(letter)

            # if the letter is in the word to letter , get indexes of all instances of letter in word to letter, with enumerate :
            if letter in word:

                indexes = [i for i, x in enumerate(word) if x == letter]
                for i in indexes:
                    user_word[i] = letter

                label_user_word.config(text=user_word)


            # if user letter is NOT in the word (), add it to the TRIED list, increment ERRORS
            else:
                # compteur du nombre d'erreurs
                errors += 1
                # update and forget() of the hangman animation :
                if errors == 1:
                    step1.place_forget()
                if errors == 2:
                    step2.place_forget()
                if errors == 3:
                    step3.place_forget()
                if errors == 4:
                    step4.place_forget()
                if errors == 5:
                    step5.place_forget()

                # delete one life :
                print("letter not in word")
                # j = random.randint(0,len(insults)-1)
                # label_output.config(text=insults[j])
                print("removing 1up n.",error_limit-errors)
                lives[error_limit-errors].destroy()
                # welcometitle.config(text=insults[j])

                # WHAT HAPPENS IF USER LOOSES THE GAME :
                # errors == error_limit : game over.
                if errors == error_limit:
                    # welcometitle.config(text="GAME OVER.")

                    label_output.config(text="GAME OVER.")
                    label_user_word.config(text=word)
                    # saveScore(score)
                    score=0

            # WHAT HAPPENS IF USER WINS THE GAME :
            # if user_word matches with word to find, game is won:
            if user_word == word:
                score +=1
                label_output.config(text=f"You won. your score : {score}. Next time you'll loose.")
                label_user_word.config(text=word)
    print(
        f"errors : {errors}"
        ,f"error_limit : {error_limit}"
        ,f"length of lives dict : {len(lives)}"
        , sep="\n"
        )
    # except:
    #     print("something went wrong...")
    #     #

'''
def saveScore(score):
    print(score)
    player = eg.enterbox("enter your pseudo, 5 letters max, no space:")
    player = str(list(player)[:6])
    print(player)
    highscores[player]=score
    # save the score
    with open('highscores.txt', 'wb') as file:
        pickle.dump(highscores, file)
'''

def init_lives():


    for i in range(0,error_limit-errors):
        lives.append(
            Button(
                frame_lives,
                bg=bg0,
                activebackground=bg0,
                image=oneUp,
                padx=0,
                pady=0,
                highlightthickness=0,
                border=0,
                ))
        lives[i].grid(row=1,column = i)


# (physical) keyboard events to allow user to input letters with physical keyboard :
def key_pressed(event):
    pprint(event)
    # try:
    letter = event.char.upper()
    print(f"letter presse : {letter}")
    if len(letter)!=0 and (65 <= ord(letter) <= 90):
        try_letter(letter)
    # except:
    #     print("keystroke was not a letter between A and Z, ignored.")


##################################################################################################


error_limit = 5
score = 0

# Couleurs
bg0 = 'black'
bg1 = '#AEA79F'


# picture used for the buttons :
image = Image.open("static/Button_dark.png")
button_image = ImageTk.PhotoImage(image)


# picture used for the lives :
# image = Image.open("static/1up.png")
image = Image.open("static/skull.png")
image = image.resize((40, 40), Image.ANTIALIAS)
oneUp = ImageTk.PhotoImage(image)


frame_user_word = Frame(gameFrame, bg = bg0 , height= 40, padx=5,pady=5)
frame_keyboard = Frame(gameFrame, bg = "black", height = 100 ,   padx=5,pady=5)
frame_output = Frame(gameFrame, bg = bg0, height = 50, padx= 5, pady=5)
frame_lives = Frame(gameFrame, bg = bg0, height = 50,  padx= 5, pady=5)

# button to start new game :
#play_button = Button(gameFrame, text="Start the game", command=init_game)



# labels

#
label_user_word = Label(frame_user_word, text = "", font=('TlwgTypewriter'), fg = 'white', bg = bg0)
label_user_word.pack()
#
label_output = Label(frame_output, text ="", font=('TlwgTypewriter'), fg = 'white', bg = bg0)
label_output.grid(row=0)
#


frame_keyboard.bind_all("<Key>", key_pressed)

# configure gameFrame grid :
Grid.grid_columnconfigure(gameFrame, index=0, weight=1)
Grid.grid_columnconfigure(gameFrame, index=1, weight=1)
for i in range(0,5):
    Grid.grid_rowconfigure(gameFrame, index=i, weight=1)

#
# generate keyboard
#

# empty dict to store all keyboard buttons :
buttons = {}

# letters used for the keyboard :
keys0 = ["A","Z","E","R","T","Y","U","I","O","P"]
keys1 = ["Q","S","D","F","G","H","J","K","L","M"]
keys2 = ["W","X","C","V","B","N"]

# configure the GRID columns and rows for frame_keyboard :
for i in range(0,len(keys0)):
    Grid.grid_columnconfigure(frame_keyboard, index=i, weight=1)
for i in range(0,3):
    Grid.grid_rowconfigure(frame_keyboard, index=i, weight=1)
row=0

# generate buttons, add them to the buttons dict
for key_list in [keys0,keys1,keys2]:
    # get number of keys on the line, will be used for grid column position
    w = len(key_list)
    for i, k in enumerate(key_list):
        # pass each button's text to a function

        # action = lambda x = k: try_letter(x)
        action = lambda x = k: try_letter(x)
        # create the buttons and assign to animal:button-object dict pair
        buttons[k] = Button(
            frame_keyboard,
            bg='black',
            fg='white',
            activebackground=bg0,
            activeforeground='black',
            text=k,
            font=('Liberation Mono',12,'bold'),
            image=button_image,
            compound=CENTER,
            command=action,
            padx=10,
            pady=10,
            highlightthickness=0,
            border=0,
        )

        # methode .GRID() renvoie toujours NONE : à appliquer après la déclaration du button !
        buttons[k].grid(column = int((10-w)/2)+i, row=row)


    row += 1

##################################################################################################

def action_level():
    # hide all elements from 'game','rules'
    print("forgetting gameplay frames...")
    frame_keyboard.grid_forget()
    frame_user_word.grid_forget()
    frame_output.grid_forget()
    frame_lives.grid_forget()

    print("packing level selection frame")
    level_container_frame.pack(side = LEFT, fill = 'both', expand=True)

    # display elements for 'level'

def action_rules():
    # hide all elements from 'game','level'
    # frame_keyboard.grid_forget()
    # frame_user_word.grid_forget()
    # frame_output.grid_forget()
    # frame_lives.grid_forget()
    # level_container_frame.pack_forget()

    # display elements for 'rules'
    # -> insérer code pour afficher les règles du jeu.
    
    messagebox.showinfo('Règles du jeu','Règle n°1 du pendu : ne te fais pas pendre.\n Règle n°2 : ... devines la suite.' )


def action_play():


    # hide all elements of previous games and start new game
    level_container_frame.pack_forget()

    global errors, lives, tried, word, user_word

    #Once PLAY button is pressed, replace the steps background
    #It should be place on this order no matter what
    step1.place (bordermode=OUTSIDE, rely = 0.0, relx = 0.0, anchor = NW)
    step2.place (bordermode=OUTSIDE, rely = 0.0, relx = 0.0, anchor = NW)
    step3.place (bordermode=OUTSIDE, rely = 0.0, relx = 0.0, anchor = NW)
    step4.place (bordermode=OUTSIDE, rely = 0.0, relx = 0.0, anchor = NW)
    step5.place (bordermode=OUTSIDE, rely = 0.0, relx = 0.0, anchor = NW)
    step6.place (bordermode=OUTSIDE, rely = 0.0, relx = 0.0, anchor = NW)

    # get new word from DB
    word_str = get_word()

    # clean-up spaces in words
    word_str = word_str.replace(" ","-")
    word=[]
    word[:0]= word_str
    pprint(word)

    # initiate the user word
    user_word = init_user_word(word)
    pprint(user_word)

    label_user_word.configure(text = user_word)


    # reset keyboard buttons
    for key in buttons:
        buttons[key].configure(state = NORMAL)

    # empty list of tried letters
    tried=[]

    # errors counter and limit
    errors = 0


    # reset the output

    label_output.configure(text="")

    # initialize lives
    lives=[]


    init_lives()


    # display elements for 'game':
    frame_user_word.grid(row=1,column=1)
    frame_lives.grid(row=2,column=1)
    frame_keyboard.grid(row=3,column=1)
    frame_output.grid(row=4,column=1)

# setup the MENU frame (left)
for i in range(0,4):
    Grid.grid_rowconfigure(frame_menu, index=i, weight=1)

butplay = Button(frame_menu, bg = 'black',font = ("goudy stout", 12), fg = "yellow", text = "PLAY", height = 3, width = 10, command=action_play, )
butplay.grid(row=0,column=0)

butlevel = Button(frame_menu,bg = 'black',font = ("goudy stout", 12), fg = "green", text = "LEVEL\n(medium)", height = 3, width = 10, command=action_level)
butlevel.grid(row=1,column=0)

butrules = Button(frame_menu, bg = 'black',font = ("goudy stout", 12), text = "RULES", fg = "red", height = 3, width = 10, command=action_rules)
butrules.grid(row=2,column=0)

butquit = Button(frame_menu, bg = 'black',font = ("goudy stout", 12), text = "EXIT", fg = "orange", height = 3, width = 10,command=root.destroy)
butquit.grid(row=3,column=0)




'''
# load the previous score if it exists
try:
    global highscores
    with open('highscores.txt', 'rb') as file:
        highscores = pickle.load(file)

except:
    highscores = {}

pprint(highscores)

# setup the HIGHSCORE BOARD frame (right)
highScores_label = Label(scoreBoard, text ="High Scores", font=('TlwgTypewriter'), fg = 'white', bg = 'black')
highScores_label.pack(side=TOP)
highScores_text = Text(scoreBoard, font=('TlwgTypewriter'), fg = 'white', bg = 'black',width=20)
highScores_text.pack()
highscore_keys = highscores.keys()
for key in highscore_keys:
    highScores_text.insert(END, f"{key} : {highscores[key]}\n")
'''


#Stream function "streams" the video "skull.mp4" as welcome introduction
#the video is a infinite loop until player press any button and change the gameFrame

def stream(label):

    #each image is stock in frame_image and refresh with a new image
    #the speed of  the image sequence give impression that this is a video
    for image in video.iter_data():
        frame_image = ImageTk.PhotoImage(Image.fromarray(image).resize((1378,950)))
        label.config(image=frame_image)
        label.image = frame_image

thread = threading.Thread(target=stream, args=(my_label,))
thread.daemon = 1
thread.start()

root.mainloop()
