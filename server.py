"""
server.py - Flask web server for the Emotion Detector application.

This module provides a REST API and web interface for detecting emotions
in text using the IBM Watson NLP Emotion Predict API.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_detector():
    """
    Analyzes the emotion of text provided via query parameter.

    Query Parameters:
        textToAnalyse (str): The text to analyze for emotions.

    Returns:
        str: A formatted string with emotion scores and dominant emotion,
             or an error message if input is invalid.
    """
    text_to_analyse = request.args.get("textToAnalyse")

    result = emotion_detector(text_to_analyse)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again."

    anger = result["anger"]
    disgust = result["disgust"]
    fear = result["fear"]
    joy = result["joy"]
    sadness = result["sadness"]
    dominant_emotion = result["dominant_emotion"]

    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )


@app.route("/")
def render_index_page():
    """
    Renders the main index page of the Emotion Detector application.

    Returns:
        str: Rendered HTML template for the index page.
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
