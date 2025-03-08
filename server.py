# Task 6: Deploy as web application using Flask
# Task 7: Incorporate Error handling

''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package : TODO DONE
# Import the sentiment_analyzer function from the package created: TODO DONE
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app : TODO DONE
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    # TODO DONE
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    # Check if the status is None, indicating an error or invalid input
    if response is None:
        return "Invalid text! Please try again!."
    else:
        # Return a formatted string with the sentiment label and score
        return (f"The system response is 'anger': {response['anger']}, 'disgust': {response['disgust']}, "
                f"'fear': {response['fear']}, 'joy': {response['joy']} and 'sadness': {response['sadness']}. "
                f"The dominant emotion is <span style='color: red; font-weight: bold;'>{response['dominant_emotion']}</span>.")
 

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    #TODO DONE
    return render_template('index.html')

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''#TODO DONE
    app.run(host="0.0.0.0", port=5004)

# python3.11 server.py
