'''
Author: Gabriel Pereira
Alias: Moriartie
'''
import pyautogui
import pyperclip as p

AUTO_REPLACE = True
COMMAND_SEPARATOR = "##"


def process(text, command):
    '''
    Custom commands
    '''
    print(f"text: {text}\ncommand: {command}")
    if command=="solve":
        p.copy(eval(text))

    elif command=="captalize":
        p.copy(text.upper())
    
    elif command=="sarcasmize":
        t = [[c.lower(),c.upper()][i%2==0] for i,c in enumerate(text)]
        p.copy(''.join(t))
    elif command=="mirror":
         p.copy(text[::-1])
    elif '->' in command:
            a, b = command.split('->')
            t = text.replace(a,b)
            p.copy(t)

def grab_input():
    '''
    Gets clipboard data and identify the command
    '''
    values = p.paste().split(COMMAND_SEPARATOR)
    print(values)
    if len(values)>1:
        command = values[-1]
        text = ''.join(values[:-1])
        return [text, command]
    else:
        return 0
     
def control_key(a):
    '''
    Fix for pyautogui.hotkey()
    '''
    if AUTO_REPLACE:
       pyautogui.keyDown('ctrl')
       pyautogui.press(a)
       pyautogui.keyUp('ctrl')

if __name__=="__main__":
    #control_key('a')
    control_key('c')
    inputs = grab_input()
    if not inputs:
        print("no command")
        exit()
    process(*inputs)
    control_key('v')
