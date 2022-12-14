from dialog import Dialog
from subprocess import run

def msgbox(title, text, height = None, width = None):
    text = "\n" + text
    d = Dialog(dialog = "dialog", autowidgetsize = True)
    code = d.msgbox(text, title = title, height = height, width = width)
    if code == d.ESC:
        run("clear")
        exit()

def yesno(title, text, height = None, width = None):
    text = "\n" + text
    d = Dialog(dialog = "dialog", autowidgetsize = True)
    code = d.yesno(text, title = title, height = height, width = width)
    if code == d.OK:
        return True
    elif code == d.CANCEL:
        return False
    elif code == d.ESC:
        run("clear")
        exit()

def inputbox(title, text, init = "", height = None, width = None):
    text = "\n" + text
    d = Dialog(dialog = "dialog", autowidgetsize = True)
    code, string = d.inputbox(text, init = init, title = title, height = height, width = width)
    if code == d.OK:
        return string
    elif code == d.CANCEL:
        run("clear")
        exit()
    elif code == d.ESC:
        run("clear")
        exit()

def menu(title, text, choices, height = None, width = None):
    text = "\n" + text
    d = Dialog(dialog = "dialog", autowidgetsize = True)
    code, tag = d.menu(text, choices = choices, title = title, height = height, width = width)
    if code == d.OK:
        return tag
    elif code == d.CANCEL:
        run("clear")
        exit()
    elif code == d.ESC:
        run("clear")
        exit()

def infobox(title, text, height = None, width = None):
    text = "\n" + text
    d = Dialog(dialog = "dialog", autowidgetsize = True)
    code = d.infobox(text, title = title, height = height, width = width)
    if code == d.ESC:
        run("clear")
        exit()
