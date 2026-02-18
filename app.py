from flask import Flask, request, render_template
import joblib
import tldextract

# Load the trained phishing email model and vectorizer
email_model = joblib.load('phishing_email_model.joblib')
vectorizer = joblib.load('tfidf_vectorizer.joblib')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_email', methods=['POST'])
def predict_email():
    email_content = request.form['email_content']
    email_features = vectorizer.transform([email_content])
    prediction = email_model.predict(email_features)[0]
    result = 'Phishing' if prediction == 1 else 'Legitimate'
    return render_template('result.html', email=email_content, result=result)

@app.route('/scan_url', methods=['POST'])
def scan_url():
    url = request.form['url']
    
    # Feature extraction for the URL
    extracted = tldextract.extract(url)
    domain = f"{extracted.domain}.{extracted.suffix}"
    
    # Simple check for malicious patterns (customize this logic later if needed)
    keywords = ['login', 'verify', 'update', 'secure', 'bank']
    if any(keyword in url.lower() for keyword in keywords):
        result = "Potentially Malicious"
    else:
        result = "Safe"
    
    return render_template('result.html', url=url, url_result=result)

if __name__ == "__main__":
    app.run(debug=True)
