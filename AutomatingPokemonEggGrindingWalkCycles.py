import pydirectinput
from pynput import keyboard
from threading import Thread
import time
global num
num=1
def hold(x,hold_time):
    start = time.time()
    while time.time() - start < hold_time:
        pydirectinput.keyDown(x)
    else:
        pydirectinput.keyUp(x)
        
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

        
if __name__ == '__main__':
    abortKey = 't'
    listener = keyboard.Listener(on_press=on_press, abortKey=abortKey)
    listener.start() 
    Thread(target=move_loop, args=(), name='move_loop', daemon=True).start()
    listener.join()