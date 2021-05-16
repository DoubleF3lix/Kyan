# Kyan
A soundboard program written in python

## Installation
You can install Kyan with pip by running `pip install kyan`, or by downloading the source and running `pip install --upgrade -e .` in the directory of `setup.py`.

## Usage
You can start Kyan by running `py -m kyan`.<br>
In the interface, you'll find numerous controls. A sounds list, 2 volume sliders (one for microphone and the other for sounds), and buttons to play and stop sounds, import or delete audio, and configure audio devices.

In order to use Kyan, you'll need a Virtual Audio Cable (VAC), which you can download [here](https://vb-audio.com/Cable/). Once this is installed, select the VAC using the "Configure Audio Devices" button:

![Select VAC Cable](https://i.imgur.com/XZ5LxLY.png)

You may need to configure your microphone, however Kyan will use the default microphone on your system by default.

To play sounds, you'll first need to import them. Click "Import Audio File", and then select an audio file by clicking the "..." button. Edit the audio name if you wish, and then click "Import". This field will be the file name of the file you selected by default (without the extension). After clicking "Import", you'll notice a new entry in the sounds list. You can select this entry and click "Play Selected Sound", or just double click the entry to play it. 

To stop any playing sounds, click "Stop All Sounds". To delete a sound, select the sound you want to remove in the sounds list and click "Delete Selected Sound". 

You can also edit the volume of any sounds you play or your microphone. Use the sliders or input boxes as needed. Any sound you play will also be played to you (if you're going to play really loud sounds, then you have to endure it too). You can check the "Hear Microphone Input" checkbox to hear what you sound like in real time. Note that this setting will not do anything if your VAC device is set to your speakers (which it is by default).

If you have any problems or errors, [create an issue](https://github.com/DoubleF3lix/Kyan/issues) on the GitHub repository.
