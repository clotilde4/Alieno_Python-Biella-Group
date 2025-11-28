from pgzero.actor import Actor
from pgzero.clock import clock #schedula eventi
from random import randint
import pgzrun

TITLE= "Il mio gioco alieno"
WIDTH= 800 #altezza schermo
HEIGHT= 600 #larghezza schermo
messaggio="" #variabile globale
alieno= Actor("alieno") #nome dell'immagine
alieno2=Actor("alieno2")

def draw():
    screen.clear()
    screen.fill(color=(252,240,252)) #riempie colore sfondo in RGB
    alieno.draw()
    alieno2.draw()
    screen.draw.text(messaggio, color=(1,1,1),center=(400,40),fontsize=50) #center serve per centrare la scritta
    
def piazza_alieno():
    alieno.x=randint(50, WIDTH-50) #dobbiamo mettere -50 per evitare che finisca fuori dallo schermo
    alieno.y=randint(50, HEIGHT-50)
    alieno.image="alieno"
    
def on_mouse_down(pos):
    global messaggio
    if alieno.collidepoint(pos):
        messaggio="uhia colpito!"
        alieno.image="esplosione"
    else:
        messaggio="mancato marameo"

def on_mouse_down(pos):
    global messaggio
    if alieno2.collidepoint(pos):
        messaggio="uhia colpito!"
        alieno2.image="esplosione"
    else:
        messaggio="mancato marameo"
        
piazza_alieno()
clock.schedule_interval(piazza_alieno,0.3)
pgzrun.go()
