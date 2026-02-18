# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the dataset (replace with the correct filename if different)
# If the dataset is a CSV file, use pd.read_csv()
df = pd.read_csv('datasets/phishing_email.csv')  # If you're using the phishing_email file

# Or, if you're using the Nigerian_Fraud file, replace with:
df2 = pd.read_csv('datasets/Nigerian_Fraud.csv')  # Use this line if you want to load the Nigerian Fraud file
df3 = pd.read_csv('datasets/SpamAssasin.csv')
# Display the first few rows to understand the structure
print(df.head())

# Check for missing values in the dataset
print(df.isnull().sum())

# Handle missing data (example: fill with empty string)
df.fillna('', inplace=True)

# Example: Text preprocessing using TF-IDF Vectorizer
vectorizer = TfidfVectorizer()

# Assuming 'email_content' is the column with email text
X = vectorizer.fit_transform(df['text_combined'])

# Display the shape of the transformed text data
print(X.shape)

# Assuming 'label' column indicates phishing (1) or legitimate (0)
y = df['label']

# Check the distribution of the labels (optional)
print(y.value_counts())

# Save the preprocessed data (optional)
df.to_csv('preprocessed_data.csv', index=False)

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the logistic regression model
model = LogisticRegression(max_iter=1000)

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')

# Classification report for more detailed evaluation
print(classification_report(y_test, y_pred))

from sklearn.model_selection import train_test_split

# Split the data into training and testing sets
# Assuming 'X' is the feature set and 'y' is the target labels
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Print the sizes of the splits
print(f"Training data size: {X_train.shape}")
print(f"Testing data size: {X_test.shape}")



#Now, we will train a machine learning model to classify the emails as phishing (1) or legitimate (0).
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Initialize the model
model = LogisticRegression(max_iter=1000)

# Train the model using the training data
model.fit(X_train, y_train)

# Predict the labels for the test data
y_pred = model.predict(X_test)

# Calculate accuracy and print classification report
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")
print(classification_report(y_test, y_pred))


#The next step is to save the trained model so that you can use it for predictions later without needing to retrain it each time.
import joblib

# Save the trained model to a file
joblib.dump(model, 'phishing_email_model.joblib')

print("Model saved successfully!")

# After fitting the model, save it and the vectorizer
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, 'phishing_email_model.joblib')

# Save the vectorizer (this ensures you can transform new data in the future)
joblib.dump(vectorizer, 'tfidf_vectorizer.joblib')

print("Model and vectorizer saved successfully!")









