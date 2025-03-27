import pandas as pd
import numpy as np
import re
import tldextract
import whois
import requests
from urllib.parse import urlparse
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle
import tkinter as tk
from tkinter import messagebox

# Feature Extraction
def extract_features(url):
    features = {}
    parsed_url = urlparse(url)
    
    # Basic URL Features
    features['url_length'] = len(url)
    features['num_dots'] = url.count('.')
    features['https'] = 1 if parsed_url.scheme == 'https' else 0
    features['has_ip'] = 1 if re.match(r'\d+\.\d+\.\d+\.\d+', parsed_url.netloc) else 0
    
    # Domain-based Features
    domain_info = tldextract.extract(url)
    features['subdomain_length'] = len(domain_info.subdomain)
    features['domain_length'] = len(domain_info.domain)
    features['suffix_length'] = len(domain_info.suffix)
    
    # WHOIS Features
    try:
        domain_whois = whois.whois(domain_info.domain + '.' + domain_info.suffix)
        features['domain_age'] = (pd.Timestamp.now() - pd.to_datetime(domain_whois.creation_date)).days if domain_whois.creation_date else 0
    except:
        features['domain_age'] = 0
    
    return features

# Load Dataset
data = pd.read_csv('dataset/phishing_urls.csv')
X = pd.DataFrame([extract_features(url) for url in data['url']])
y = data['label']

# Train Model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate Model
y_pred = model.predict(X_test)
print(f'Accuracy: {accuracy_score(y_test, y_pred)}')

# Save Model
with open('models/phishing_model.pkl', 'wb') as f:
    pickle.dump(model, f)

# Prediction Function
def predict_url(url):
    with open('models/phishing_model.pkl', 'rb') as f:
        model = pickle.load(f)
    features = extract_features(url)
    features_df = pd.DataFrame([features])
    return model.predict(features_df)[0]

# GUI Application
def classify_url():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a URL")
        return
    result = predict_url(url)
    if result == 1:
        messagebox.showwarning("Result", "Phishing URL Detected!")
    else:
        messagebox.showinfo("Result", "URL is Safe.")

# Create GUI
root = tk.Tk()
root.title("Phishing URL Detector")
root.geometry("400x200")

tk.Label(root, text="Enter URL:").pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

tk.Button(root, text="Check URL", command=classify_url).pack(pady=20)

root.mainloop()

if __name__ == "__main__":
    root.mainloop()
