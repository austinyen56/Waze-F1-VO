# Waze F1 VO

![](https://img.shields.io/badge/Platform-Mobile-brightgreen)

Bring Jeff, the race engineer from F1 2020, to Waze navigation.



## How to download and install this program

Simply open the following link on an Android device with Waze installed:

https://waze.com/ul?acvp=ee1b5f92-af3f-4e3e-a184-66759cd59709

Waze should launch automatically and prompt you to download the voice pack.

[Old Method]

* ~~Go to [Releases](https://github.com/austinyen56/Waze-F1-VO/releases/) and click on the apk file to download~~
* ~~After downloading the apk file, go to the Google Play store and download [Apk-signer](https://play.google.com/store/apps/details?id=com.haibison.apksigner&hl=en&gl=US)~~
* ~~Load the apk file into apk-signer and install it~~
* ~~Open and log in to Waze and have fun :)  Note: (might not work if you are using guest user)~~

## Things to note

* All audio was extracted from F1 2020 game.
* Some prompts are assembled from multiple voice clips, so a few transitions may sound slightly unnatural.
* Created Waze sharable link using [pipeeeeees/waze-voicepack-links](https://github.com/pipeeeeees/waze-voicepack-links/tree/main/mp3_upload)
* Compressed audio zip file is [here](https://voice-prompts-ipv6.waze.com/ee1b5f92-af3f-4e3e-a184-66759cd59709.tar.gz)

Here are all the transcriptions to the corresponding sound files:
<details>
<summary>Full voice list (Open me if its hiden)</summary>

| File | Voice Line |
|------|------------|
| `200.mp3` | In .1 miles... |
| `200meters.mp3` | In .2 km... |
| `400.mp3` | In .25 miles... |
| `400meters.mp3` | In .4 km... |
| `800.mp3` | In .5 miles... |
| `800meters.mp3` | In .8 km... |
| `1000meters.mp3` | In 1 kilometer... |
| `1500.mp3` | In 1 mile... |
| `1500meters.mp3` | In 1.5 kilometers... |
| `AndThen.mp3` | And then... |
| `ApproachAccident.mp3` | Be aware, theres an incident in the next part of the track. No overtaking through the yellow flags. |
| `ApproachHazard.mp3` | Track conditions are bad. Recommend you slow down and remain a positive delta. |
| `ApproachRedLightCam.mp3` | The radar suggests that they seem to have a red camera ahead of you. |
| `ApproachSpeedCam.mp3` | The radar suggests that they seem to have a speed camera ahead. |
| `ApproachTraffic.mp3` | The radar suggests that there will be some traffic at the pit exit, its gonna be busy at the rejoin. |
| `Arrive.mp3` | Thats the end of the race. We will see you at parc ferme. |
| `ExitLeft.mp3` | Exit on the left |
| `ExitRight.mp3` | Exit on the right |
| `Fifth.mp3` | Take the fifth pit window |
| `First.mp3` | Take the first pit window |
| `Fourth.mp3` | Take the fourth pit window |
| `KeepLeft.mp3` | Stay on the left |
| `KeepRight.mp3` | Stay on the right |
| `Police.mp3` | Safety car deployed, approaching the safety car. No overtaking, reduce your pace. |
| `Roundabout.mp3` | At the end of the following corners |
| `Second.mp3` | Take the second pit window |
| `Seventh.mp3` | Take the seventh pit window |
| `Sixth.mp3` | Take the sixth pit window |
| `StartDrive1.mp3` | Morning, I'm delighted to be able to work with you as your race engineer. The car is just about ready if you want to head out onto the circuit. |
| `StartDrive2.mp3` | Ok good to have you on board. I'm Jeff and I will be you race engineer. Our system checks are A-OK, so we can get under way whenever you like. |
| `StartDrive3.mp3` | This is Jeff speaking, I've been assigned as your race engineer. Car is good to go so head out onto track whenever you like. |
| `StartDrive4.mp3` | Ok its Jeff here. And it looks like we're just about ready to get out on track. I'll be working with you as your race engineer. |
| `StartDrive5.mp3` | Same as `StartDrive1.mp3` |
| `StartDrive6.mp3` | Same as `StartDrive2.mp3` |
| `StartDrive7.mp3` | Same as `StartDrive3.mp3` |
| `StartDrive8.mp3` | Same as `StartDrive4.mp3` |
| `StartDrive9.mp3` | Ok the circuit is clear at the moment, we are ready to go. |
| `Straight.mp3` | Go straight ahead. |
| `Third.mp3` | Take the third pit window |
| `TickerPoints.mp3` | Ok, check your MFD for a new strategy option. |
| `TurnLeft.mp3` | Turn left |
| `TurnRight.mp3` | Turn right |
| `uturn.mp3` | Turn 180 degrees |
</details>

If there are any errors or bugs, please post an issue and I will respond asap. Also, feel free to request any new features and I'll try my best to make it happen 😊

## Audio Extraction & Speech-to-Text Guide
This part doesn't pertain to the Waze F1 VO, but basically this is how I was able to extract the game files and create these VOs. If you happen to see this part while scrolling, feel free to read along!

* Navigate to ```C:\F1 2020\audio\2020\speech``` to obtain the .nfs files. These files are also used in the Need for Speed games for audio/ speech files.

* Download QuickBMS from:
http://aluigi.altervista.org/quickbms.htm and select [codemasters_nefs.bms](http://aluigi.altervista.org/bms/codemasters_nefs.bms)
* Using QuickBMS to extract the .nfs files, it should give you a Wwise file named `Wwise.dat`
* Download [ww2ogg](https://github.com/hcs64/ww2ogg) and copy the ww2ogg024 folder into the extracted directory
* Create a .bat file with the following code to convert all .wem files to .ogg.
```bat
for %%f in (*.wem) do "./ww2ogg024/ww2ogg.exe" %%f --pcb "./ww2ogg024/packed_codebooks_aoTuV_603.bin"
pause
for %%f in (*.ogg) do revorb.exe %%f
pause
```
* Optional: Remove the .wem files
      
Now with THOUSANDS (literally) of audio files. How do I know which ones I need? I'm not gonna listen to all of them individually right?
* Initially, this project used [SpeechRecognition]((https://pypi.org/project/SpeechRecognition/)), which worked but often misidentified phrases.

Example:

> "Increasing the gap by nine tenths"

became

> "Increasing the gap by 910 salon"


* Very short phrases such as timecodes were either undetected or erroring. Which were pretty important for this project.

Example:
> .2 miles per hour

became

> point to mph

* Coming back to it now, I decided to use [faster_whisper](https://pypi.org/project/faster-whisper/0.3.0/) and rewrote the transcription logic which proved to be much faster and accurate. GPU/cuda acceleration also made the runtime faster as well.
* After having a list of all files transcribed, I just pieced them together and exported using FL Studio!

*Disclaimer: This is a fan-made project and is not affiliated with Codemasters, EA, or Waze.*