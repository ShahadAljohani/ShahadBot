# ShahadBot
A terminal-based, voice-enabled chatbot integrated with a Cohere LLM.


## How to run it on CLI ?

1- get your: cohere API key, ElevenLabs API key

2- change the API key code segment in the file with your API keys

3- Open your terminal (anaconda preferable) 

4- initiate your environment and activate it using the following prompts:

 ```
conda create -n chatbot python=3.10 -y
conda activate chatbot
 ```

5- install required packages:

```
pip install cohere elevenlabs sounddevice scipy numpy requests speechrecognition
```

6- Navigate to the project folder:

```
cd path/to/project
```

*edit the path 

7- Run the file:

```
python shahadbot.py
```








