# Task 3: Format the output of the application
# Task 7: Incorporate Error handling

import requests
import json

def emotion_detector(text_to_analyse):
    # URL of the sentiment analysis service
    url = url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Custom header specifying the model ID for the sentiment analysis service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Sending a POST request to the sentiment analysis API
    response = requests.post(url, json=myobj, headers=header)

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # Getting emotion scores
    emotions = formatted_response["emotionPredictions"][0]["emotion"]

    # Determining the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)

    # Forming the result
    result = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }

    print(result)
    return result

# export PS1="[\[\033[01;32m\]\u\[\033[00m\]: \[\033[01;34m\]\W\[\033[00m\]]\$ "
# from emotion_detection import emotion_detector
# emotion_detector("I am so happy I am doing this.")# Task 3: Format the output of the application

import requests
import json

def emotion_detector(text_to_analyse):
    # URL of the sentiment analysis service
    url = url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Custom header specifying the model ID for the sentiment analysis service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Sending a POST request to the sentiment analysis API
    response = requests.post(url, json=myobj, headers=header)

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:

        # Getting emotion scores
        emotions = formatted_response["emotionPredictions"][0]["emotion"]

        # Determining the dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)

        # Forming the result
        result = {
            'anger': emotions['anger'],
            'disgust': emotions['disgust'],
            'fear': emotions['fear'],
            'joy': emotions['joy'],
            'sadness': emotions['sadness'],
            'dominant_emotion': dominant_emotion
        }

    elif response.status_code == 400:
        # Forming the result
        result = None
    print(response.status_code)
    #print(result)
    return result

# export PS1="[\[\033[01;32m\]\u\[\033[00m\]: \[\033[01;34m\]\W\[\033[00m\]]\$ "
# from emotion_detection import emotion_detector
# emotion_detector("I am so happy I am doing this.")
# python3.11
# from EmotionDetection.emotion_detection import emotion_detector
# emotion_detector("I hate working long hours.")  
# python3.11
# from EmotionDetection.emotion_detection import emotion_detector
# emotion_detector("I hate working long hours.")