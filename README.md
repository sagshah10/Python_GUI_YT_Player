# Python_GUI_YT_Player

This is a simple Python script which has a simple GUI developed using the python Tkinter module. The aim of this program is to retreive all the different video quality options for a given youtube url, and then allowing a user to pick a specific quality and have the video play on VLC Media Player for windows.


## Requirements For It To Work

- Python 3 (Not sure if it will work in previous versions, I have used python 3 to develop it)
- vlc media player for windows.
(If the path of your VLC installed directory is not "C:/Program Files/VideoLAN/VLC/vlc.exe", then simply open GUIYoutubeScraper.py and add your vlc path for the variable 'vlc_path' )

And thats all you most probably need, as I have only used libraries that come with python 3, and therefore you would not have to install any external libraries to make this program work.


## How To Use
As I mentioned this is a very basic program I wished to build, in order to allow me to better learn web scraping, regular expressions and the development of a GUI Application using Python. 

To use this application is very simple, after having installed vlc, and having entered the right path on the GUIYoutubeScraper.py file, all you have to do is launch GUIYoutubeScraper.py. 


### Step 1)

Once launched,  you will find a textbox to paste or enter your youtube url. 

### Step 2)

thereafter click the 'Get Video Links' button. You will then find new options appearing. 

### Step 3)

The first new option is a drop-down menu, to allow you to pick a particular quality/ video format. 

### Step 4)

After selecting your desired quality simply click on "Play Video" button. (This will automatically launch vlc and play the video)



# Known Issues

- It is way too basic, it doesnt even show simple youtube video descriptions (How can you call it a youtube player? :D) - I Will add more features over time, please be patient.

- When you click "Play Video", once VLC Launches it takes a long while for it to load the video. If you are patient press CTRL + J on VLC for windows, and it should show you the "Current Media Information" Menu, Keep staring at the large white box under the codec menu, the video will only begin once the codecs appear on the white textbox. 