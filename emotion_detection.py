"""
emotion_detection.py - Top-level module for emotion detection.

This module provides a wrapper function for using the EmotionDetection package.
"""

from EmotionDetection.emotion_detection import emotion_detector


def run_emotion_detector(text):
    """
    Run the emotion detector on the given text and print results.

    Args:
        text (str): The text to analyze for emotions.
    """
    result = emotion_detector(text)
    print(f"Emotion Analysis Result:")
    print(f"  Anger:    {result['anger']}")
    print(f"  Disgust:  {result['disgust']}")
    print(f"  Fear:     {result['fear']}")
    print(f"  Joy:      {result['joy']}")
    print(f"  Sadness:  {result['sadness']}")
    print(f"  Dominant: {result['dominant_emotion']}")
    return result


if __name__ == "__main__":
    sample_text = "I am so happy today! This is wonderful news."
    run_emotion_detector(sample_text)
