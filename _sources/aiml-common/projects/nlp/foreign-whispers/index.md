# Foreign Whispers

In this project you will develop a solution that will accept as input youtube videos from the [60 minutes channel](https://www.youtube.com/@60minutes) and output the video but with spoken and written subtitles to another language of your choosing. 

## Milestone 1: Source Videos and Closed Captions (10 points)

Write a python API  that will download the video and its closed captions from youtube.

Access 10 videos from the [60 minutes channel](https://www.youtube.com/@60minutes) and more specifically from the [Interviews playlist](https://www.youtube.com/playlist?list=PLI1yx5Z0Lrv77D_g1tvF9u3FVqnrNbCRL) and download them to your local environment. 

![](images/cc.png)

The youtube service give you the ability of downloading the closed captions of a video. You can do that by clicking on the three dots on the bottom right of the video and then clicking on the "Open transcript" option. The downloaded subtitles/closed captions will serve as the ground truth for the English language. 

## Milestone 2: Speech to Text (20 points)

Write a Python API that will separate the audio from the video and convert it to text. For this you will use libraries such as https://github.com/openai/whisper

[Whisper](https://github.com/openai/whisper) is a general-purpose speech recognition model. It is trained on a large dataset of diverse audio and is also a multitasking model that can perform multilingual speech recognition, speech translation, and language identification.

![](images/approach.png)


## Milestone 3:Source Text to Target Text (25 points)

Write a Python API that will translate the text from English to a language of your choosing. Please note you need to select the language from the list of languages that can be served by the TTS Milestone. You can use any library you want for this task except commercial ones that include Google Translate, Microsoft Translate, OpenAI etc. 

## Milestone 4: Target Text to Speech (25 points)

Write a Python API that will convert the translated text to speech. You can use any library you want for this task except commercial ones. For example, you can use [TTS](https://tts.readthedocs.io/en/latest/tutorial_for_nervous_beginners.html)

## Milestone 5a: Stitching it all together (20 points)

(15 points) Build a UI in [Hugging Face](https://huggingface.co/) Spaces and [Streamlit Spaces](https://huggingface.co/docs/hub/spaces-sdks-streamlit) that will accept as input a youtube video and will output the video with subtitles to a language of your choosing.

The UI must look similar to this one:

![](images/aisub.png)

Note: ignore the OpenAI part of the UI. You will not be using OpenAI for this project.

(5 points) Create a 30sec video as a pitch to your project. Upload it to youtube and include the link in your submission. 

## Milestone 6: Extra Credit (10 points)

Implement the above as components (apps) of [a Django application](https://docs.djangoproject.com/en/4.2/intro/tutorial01/) that wll be deployed via Docker compose.  In this case the UI in Milestone 5 will be a web application and you can use any UI framework you want including Bootstrap. 

The extra credits are not transferrable to other assignments.  They can be used as a safeguard to max out the project grade (100%).




