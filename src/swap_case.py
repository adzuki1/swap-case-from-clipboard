import pyperclip
import keyboard

def swapClipboardCase():
    """
    Capture text from the clipboard (cb),
    swap case and put it back on the cb
    """
    try:
        # get text from the cb
        original_txt = pyperclip.paste()
        if not original_txt: return
        # swap case
        swapped_txt = original_txt.swapcase()
        # putting it back on the cb
        pyperclip.copy(swapped_txt)

    except pyperclip.PyperclipException as e:
            print(f"Error: {e}\n")

    except Exception as e:
         print(f"Error: {e}\n")

def main():
    """
    Configure hotkey listener and loop the process
    """
    hotkey = 'alt+v'
    exit_hotkey = 'ctrl+alt+esc' # end process

    try:
        keyboard.add_hotkey(hotkey, swapClipboardCase, suppress=True)
        
        # log while running
        print("Started.")
        
        #keep process until action exit
        keyboard.wait(exit_hotkey)

    except Exception as e:
        # if no root
        if "Permission denied" in str(e) or "root" in str(e):
             print(f"permission error: {e}\n")
             print("Try add 'sudo'")
        else:
             print(f"lintener error: {e}")

if __name__=="__main__":
     main()
 