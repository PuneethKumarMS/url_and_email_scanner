import joblib
import pandas as pd

# Load the saved model and vectorizer
model = joblib.load('phishing_email_model.joblib')
vectorizer = joblib.load('tfidf_vectorizer.joblib')

# New emails to test
new_emails = [
    "Congratulations! You have won a $1,000 gift card. Click here to claim your prize.",
    "Hello, I hope you are doing well. Here is the report I promised to send you."
]

# Preprocess the new emails using the fitted vectorizer (this is where the fitting happens)
new_email_features = vectorizer.transform(new_emails)

# Make predictions
predictions = model.predict(new_email_features)

# Display predictions
for email, prediction in zip(new_emails, predictions):
    print(f"Email: {email}")
    print(f"Prediction: {'Phishing' if prediction == 1 else 'Legitimate'}")
    print('-' * 50)
