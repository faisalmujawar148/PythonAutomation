import pydirectinput
from pynput import keyboard
from threading import Thread
import time
global num
num=1
def hold(key,hold_time): #control how long to hold down a key
    start = time.time()
    while time.time() - start < hold_time:
        pydirectinput.keyDown(key)
    else:
        pydirectinput.keyUp(key)
        
def on_press(key, abortKey='esc'):
    global num
    try:
        k=key.char 
    except:
        k=key.name
    if k=='k': #if you press 'k' or whatever you want, it pauses the move_loop (via global num value)
        num=2
        print('paused')
    if k==abortKey: #if you press esc, it stops the loop basically (via global num value)
        num=0
        print('end loop')
        return False 

def move_loop():
    global num
    time.sleep(5)
    count=0
    while True:
        hold('x',.01) #change this to whatever your binds are, and for however long you want
        count+=1
        if num==0:
            break
        if num==2:
            time.sleep(20) #you can increase/decrease the pause amount
            num=1

        
if __name__ == '__main__': #basically allows you to only run the listener part directly, not as a module, can be removed if you want to import this into another program as a module
    abortKey = 'esc'
    listener = keyboard.Listener(on_press=on_press, abortKey=abortKey) #Initializing a keyboard listener
    listener.start() 
    Thread(target=move_loop, args=(), name='move_loop', daemon=True).start() #Starting the listener
    listener.join()
