# Emotion Detector

## IBM Developer Skills Network | AI/ML with Python Final Project

This project is the **Final Project** for the **Developing AI Applications with Python and Flask** course on Coursera/IBM Developer Skills Network.

---

## Project Overview

The **Emotion Detector** is a web application that uses the **IBM Watson NLP (Natural Language Processing)** library to analyze emotions in text. The application identifies the following emotions:

- **Anger**
- **Disgust**
- **Fear**
- **Joy**
- **Sadness**

It also identifies the **dominant emotion** in the provided text.

---

## Project Structure

```
emotion-detector/
├── README.md
├── emotion_detection.py          # Top-level emotion detection module
├── test_emotion_detection.py     # Unit tests for the application
├── server.py                     # Flask web server
├── EmotionDetection/
│   ├── __init__.py               # Package initializer
│   └── emotion_detection.py      # Core emotion detection logic
├── templates/
│   └── index.html                # Web application HTML template
└── static/
    └── style.css                 # Web application styles
```

---

## Features

- **REST API Endpoint**: `/emotionDetector?textToAnalyse=<text>` — returns emotion scores and dominant emotion
- **Web Interface**: User-friendly UI to analyze text emotions in real time
- **Error Handling**: Returns appropriate messages for blank or invalid input
- **IBM Watson NLP Integration**: Uses the `EmotionPredict` model from IBM Watson NLP

---

## Setup and Installation

### Prerequisites

- Python 3.x
- pip (Python package manager)

### Install Dependencies

```bash
pip install flask requests
```

### Run the Application

```bash
python server.py
```

Open your browser and go to: [http://localhost:5000](http://localhost:5000)

---

## API Usage

**Endpoint:**
```
GET /emotionDetector?textToAnalyse=<your text here>
```

**Example Request:**
```
GET /emotionDetector?textToAnalyse=I am so happy today!
```

**Example Response:**
```
For the given statement, the system response is 'anger': 0.005, 'disgust': 0.002, 'fear': 0.003, 'joy': 0.891 and 'sadness': 0.052. The dominant emotion is joy.
```

---

## Running Unit Tests

```bash
python -m pytest test_emotion_detection.py
```

or

```bash
python -m unittest test_emotion_detection.py
```

---

## IBM Watson NLP API

This application uses the IBM Watson NLP Emotion Predict API:

- **URL**: `https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict`
- **Model**: `emotion_aggregated-workflow_lang_en_stock`

---

## Project Tasks Completed

- [x] **Task 1**: Clone the project repository and navigate to the project folder
- [x] **Task 2**: Create an emotion detection application using Watson NLP library
- [x] **Task 3**: Format the output of the application
- [x] **Task 4**: Package the application
- [x] **Task 5**: Run Unit Tests on your application
- [x] **Task 6**: Deploy as web application using Flask
- [x] **Task 7**: Incorporate Error handling
- [x] **Task 8**: Run static code analysis

---

## Technology Stack

- **Language**: Python 3
- **Web Framework**: Flask
- **NLP API**: IBM Watson NLP (Emotion Predict)
- **Testing**: unittest / pytest
- **Frontend**: HTML5, CSS3, JavaScript

---

## Author

**Pruthvi Chaudharii**

IBM Developer Skills Network — AI/ML with Python Final Project

---

## License

This project is submitted as part of the IBM Developer Skills Network course requirements.
