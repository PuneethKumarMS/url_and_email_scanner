# URL and Email Phishing Scanner

A Python-based web application designed to identify potential phishing emails and suspicious URLs using Machine Learning and rule-based detection techniques.

## Overview

Phishing attacks are one of the most common cybersecurity threats, targeting users through deceptive emails and malicious URLs to steal sensitive information such as login credentials, financial details, and personal data.

**URL and Email Phishing Scanner** provides a simple web-based interface to analyze email content and URLs for potential phishing indicators.

The application combines a pre-trained Machine Learning model for email classification with rule-based URL inspection to help users identify potentially malicious content.

## Features

- **Phishing Email Detection:** Classifies email content as Phishing or Legitimate using a trained Machine Learning model.
- **TF-IDF Text Vectorization:** Converts email text into numerical features for Machine Learning prediction.
- **URL Analysis:** Extracts domain information and checks URLs against predefined suspicious keyword patterns.
- **HTTP Response Inspection:** Checks URL responses using HTTP HEAD requests in the standalone URL scanning module.
- **Web-Based Interface:** Provides a simple interface for submitting emails and URLs and viewing scan results.
- **Pre-trained Model Integration:** Loads trained model and vectorizer artifacts using Joblib.

## Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Web Framework | Flask |
| Machine Learning | Scikit-learn |
| Feature Extraction | TF-IDF Vectorizer |
| Model Serialization | Joblib |
| Data Processing | Pandas, NumPy |
| URL Analysis | tldextract |
| HTTP Requests | Requests |
| Frontend | HTML, CSS |

## Project Structure

```text
url_and_email_scanner/
│
├── static/
│   └──                 # Static frontend assets
│
├── templates/
│   ├── index.html      # Main application interface
│   └── result.html     # Scan results page
│
├── app.py              # Flask application and detection routes
├── data_preprocessing.py  # Dataset preprocessing and feature extraction
├── url_scanner.py      # Standalone URL scanning module
│
├── phishing_email_model.joblib
├── tfidf_vectorizer.joblib
│
├── test_model.py       # Model testing
└── .gitignore
```

## How It Works

### 1. Phishing Email Detection

The application uses a pre-trained Machine Learning model to classify email content.

**Processing workflow:**

1. The user submits email content through the web interface.
2. The application receives the email using a Flask POST endpoint.
3. The TF-IDF vectorizer transforms the text into numerical feature representations.
4. The trained classification model processes the extracted features.
5. The application returns one of two classifications:
   - Phishing
   - Legitimate

**Machine Learning components:**
- TF-IDF (Term Frequency–Inverse Document Frequency)
- Pre-trained classification model
- Scikit-learn
- Joblib

### 2. Suspicious URL Detection

The application analyzes submitted URLs using domain extraction and predefined keyword-based checks.

**Processing workflow:**

1. The user submits a URL.
2. The application extracts domain information using `tldextract`.
3. The URL is checked for suspicious keywords such as:
   - login
   - verify
   - update
   - secure
   - bank
4. Based on the matching conditions, the application displays a result indicating whether the URL is potentially malicious or safe.

The standalone URL scanning module also includes an HTTP HEAD request check to inspect server responses.

## Installation and Setup

### Prerequisites

- Python 3.9 or later
- pip
- Git

### Step 1: Clone the Repository

```bash
git clone https://github.com/PuneethKumarMS/url_and_email_scanner.git
```

### Step 2: Navigate to the Project Directory

```bash
cd url_and_email_scanner
```

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment.

**Windows:**
```bash
venv\Scripts\activate
```

**Linux / macOS:**
```bash
source venv/bin/activate
```

### Step 4: Install Dependencies

```bash
pip install flask scikit-learn joblib tldextract requests pandas numpy
```

### Step 5: Run the Application

```bash
python app.py
```

### Step 6: Access the Application

Open your browser and navigate to:

```text
http://127.0.0.1:5000/
```

## Machine Learning Workflow

The email detection pipeline follows these stages:

```text
Email Input
     |
     v
Text Preprocessing
     |
     v
TF-IDF Vectorization
     |
     v
Trained ML Model
     |
     v
Classification
     |
     v
Phishing / Legitimate
```

## Security Considerations

- Detection results should be treated as preliminary indicators, not definitive security verdicts.
- Keyword-based URL inspection can produce false positives and false negatives.
- HTTP response status alone cannot establish whether a website is malicious.
- Do not enter real credentials or sensitive personal information into suspicious websites.
- Further improvements can include reputation-based URL analysis, advanced phishing feature extraction, and more robust validation.

## Future Enhancements

- Integrate threat intelligence APIs for URL reputation checking.
- Implement advanced URL feature extraction.
- Improve phishing detection using additional Machine Learning algorithms.
- Add domain reputation and blacklist checking.
- Introduce real-time scanning and detailed threat reports.
- Improve detection accuracy through larger and more diverse datasets.
- Add comprehensive input validation and security controls.

## Disclaimer

This project is developed for educational and cybersecurity research purposes. Detection results are not guaranteed to identify every phishing attempt.
