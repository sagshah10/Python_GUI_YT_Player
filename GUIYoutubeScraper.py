from tkinter import *
from functools import partial
import time
import urllib.request as request
import re
import urllib
import subprocess
import os
import random

vlc_path = "C:/Program Files/VideoLAN/VLC/vlc.exe"


def getHeaders():
    user_agent = ['Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; it; rv:2.0b4) Gecko/20100818', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330', 'Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.9.2a1pre) Gecko', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; pl; rv:1.9.2.3) Gecko/20100401 Lightningquail/3.6.3', 'Mozilla/5.0 (X11; ; Linux i686; rv:1.9.2.20) Gecko/20110805', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; fr; rv:1.9.2.13) Gecko/20101203 iPhone', 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2.13; ) Gecko/20101203', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1b3) Gecko/20090305', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-TW; rv:1.9.0.9) Gecko/2009040821', 'Mozilla/5.0 (X11; U; Linux i686; ru; rv:1.9.0.8) Gecko/2009032711', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.7) Gecko/2009032803', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.7) Gecko/2009021910 MEGAUPLOAD 1.0', 'Mozilla/5.0 (Windows; U; BeOS; en-US; rv:1.9.0.7) Gecko/2009021910', 'Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.0.6) Gecko/2009020911', 'Mozilla/5.0 (X11; U; Linux i686; en; rv:1.9.0.6) Gecko/20080528', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.6) Gecko/2009020409', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1)', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.3) Gecko/2008092816', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.3) Gecko/2008090713', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.2) Gecko Fedora/1.9.0.2-1.fc9', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.14) Gecko/2009091010', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.10) Gecko/2009042523', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.1) Gecko/2008072610', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008072820 Ubuntu/8.04 (hardy) (Linux Mint)', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko', 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.0.1) Gecko/2008070206', 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-au; rv:1.9.0.1) Gecko/2008070206', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9) Gecko', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9) Gecko', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; cs; rv:1.9) Gecko/2008052906']
    choice = random.choice(user_agent)
    headers = {'User-Agent': choice}
    # print("chosen headers = ", choice)
    return headers

def getQualityChoice(url):
    req = request.Request(url, headers=getHeaders())
    with request.urlopen(url) as response:
        content = response.read().decode("utf-8").replace(r"\u2006", "&")

    # print(content)
    # content = request.unquote(re.sub(r"\+", " ", content))
    # content = request.unquote(content)  # have to do it again, because certain items were not properly decoding
    
    qualityChoices = []

    match = re.compile('"adaptive_fmts":(.+?),"', re.DOTALL).findall(content)

    
    for extractedContent in match:

        # print(extractedContent, "\n\n\n\n")
        # print(test, "\n\n\n")
        # extractedContent = request.unquote(re.sub(r"\+", " ", extractedContent))

        extractedContent = urllib.parse.unquote_plus(extractedContent)
        match2 = re.compile("url=(.+?)url=", re.DOTALL).findall(extractedContent)
        # print("match2 = ", match2, "\n\n\n\n")

        
        
        for qualityOptions in match2:

            # print (qualityOptions, "\n\n\n")
        
            # if "&type=audio" in qualityOptions:
            #    print(qualityOptions, "\n\n\n")

            # if "quality_label" in qualityOptions:
            #    print(qualityOptions, "\n\n\n")

            

            split = qualityOptions.split(";")

            # print(split)
            vid_url = split[0].strip() + ";"

            # print(split)
            
            cont_type = re.compile(r"[&]?type=[\w]*/[\w\d]{2,5}").search(vid_url)[0]

            cont_type = cont_type.replace("&","").replace("type=", "").strip()

            try:
                quality = re.compile(r"quality_label=[\d\w]*").search(qualityOptions)[0]
            except Exception:
                pass
            
            # print("Type = " , cont_type)    
            # print("Quality = " , quality)

            quality = quality.replace("quality_label=", "")
            if "\\" in vid_url:
                vid_url = vid_url.split("\\")[0]

            # print("vid_url = ", vid_url)

            choice = ""

            if len(cont_type)>0:
                choice += cont_type 

            if len(quality) > 0:
                choice += " - " + quality

            # print("choice = ", choice)
            # print(x, "\n")
            # print("vid_url = ", vid_url, "\n")
            # print("quality = ", quality)

            temp = (choice, vid_url)
            qualityChoices.append(temp)
            # print("\n\n\n")
        return qualityChoices
      
def playVid():
    # print("Quality = ", selectedQual.get())

    vid_url = ""

    aud_url = []
    for qual, url in choices:
        if qual == selectedQual.get():
            vid_url = url

            # print(vid_url)

            if "audio" in selectedQual.get():
                audio = []
                break
        if "audio" in qual:
            aud_url.append("--input-slave=" + url)

    vid_url = vid_url.split("&projection")[0]
    
    if len(aud_url) == 0:
        toPass = [vlc_path, vid_url, '--play-and-exit'] # '--fullscreen' - This command would make the player Fullscreen on start

    else:
        toPass = [vlc_path, vid_url]

        for item in aud_url:
            toPass.append(item)
        toPass = toPass + ['--play-and-exit'] 
    
    # print(toPass)
    
    subprocess.Popen(toPass)
    # '--play-and-exit' learnt from: https://stackoverflow.com/questions/10249261/play-video-file-with-vlc-then-quit-vlc


def getQuality():
    ## print(urlInput.get())

    try:
        global choices
        choices = getQualityChoice(urlInput.get())
        # print(choices)
        # choices = [("1080p", "x"),("1080p60", "y"), ("720p", "z")] 
    except Exception as e:
        print(e)
        return

    if len(choices) == 0:
        return

    else:
        global selectedQual, qualFrame

        selectedQual = StringVar()
        qlty = [] 
        
        for quality, url in choices:
            qlty.append(quality)      

        selectedQual.set(qlty[0])

        try:
            qualFrame.destroy()
        except Exception:
            pass
        
        qualFrame = Frame(YTFrame)
        qualFrame.grid(row=7)
        
        qualSelect = Label(qualFrame, text="Select Quality: ")
        qualSelect.grid(row=0, column=0)
        qualOptions = OptionMenu(qualFrame, selectedQual, *qlty)
        qualOptions.grid(row=0, column=1)
        
        qualSubmit = Button(root, text="Play Video", command=playVid)
        qualSubmit.grid(row=1, columnspan=2)
            
def addBlankSpace(frame, row):
    blank = Label(frame)
    blank.grid(row=row)

   
root = Tk()

root.title("YouTube Player")
# master.geometry("600x500")
# Adds as Window Title (https://stackoverflow.com/questions/2395431/using-tkinter-in-python-to-edit-the-title-bar)

YTFrame = Frame(root)
YTFrame.grid(row=0, column=1)

addBlankSpace(YTFrame, 1)

heading = Label(YTFrame, text="YOUTUBE PLAYER", font="Cambria 20 bold")
heading.grid(row=1, columnspan=2)

addBlankSpace(YTFrame, 2)
addBlankSpace(YTFrame, 3)

urltxt = Label(YTFrame, text="Enter/Paste YouTube Url Here: ")
urltxt.grid(row=4, column=0)
urlInput = Entry(YTFrame, width="50")
urlInput.grid(row=4, column=1)

#CREATING A context menu below to allow a user to cut, copy paste and select all, when they right-click the urlInput entry box.
#Learnt How to create right click context menu from:
    # http://effbot.org/zone/tkinter-popup-menu.htm     AND
    # https://stackoverflow.com/questions/12014210/tkinter-app-adding-a-right-click-context-menu
    # https://mail.python.org/pipermail/tutor/2004-July/030398.html  

def copy():
    try:
        root.clipboard_clear()
        text = urlInput.selection_get()
        root.clipboard_append(text)
    except Exception: pass
    
def cut():
    try:
        copy()
        urlInput.delete("sel.first", "sel.last")
    except Exception: pass
    
def paste():
    try:
        urlInput.delete("sel.first", "sel.last")
    except Exception: pass

    text = root.selection_get(selection='CLIPBOARD')
    urlInput.insert('insert', text)

def select_all():
    #Learnt from: https://stackoverflow.com/questions/41477428/ctrl-a-select-all-in-entry-widget-tkinter-python?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
    urlInput.select_range(0, "end")
    urlInput.icursor('end')

popup = Menu(root, tearoff=0)
popup.add_command(label="Copy", command=copy)
popup.add_command(label="Cut", command=cut)
popup.add_command(label="Paste", command=paste)
popup.add_command(label="Select All", command=select_all)

def do_popup(event):
    # display the popup menu
    try:
        popup.tk_popup(event.x_root, event.y_root, 0)
    finally:
        # make sure to release the grab (Tk 8.0a1 only)
        popup.grab_release()
        
urlInput.bind("<Button-3>", do_popup)

## Right-Click context menu end


addBlankSpace(YTFrame, 5)
submit = Button(YTFrame, text="Get Video Links", command=getQuality)
submit.grid(row=6, column=0)



root.mainloop()

