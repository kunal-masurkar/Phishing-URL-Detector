# 🚀 Phishing URL Detector Setup Guide

This guide will help you set up and run the **Phishing URL Detector** on your system.

## 🔧 Prerequisites

- 🐍 Python 3.8 or higher
- 📂 Dataset (`phishing_urls.csv`)
- 🔍 Network access (if WHOIS lookups are enabled)

## 📥 Installation Steps

### 1️⃣ Clone or Download the Project Files
Ensure you have all the necessary files in your project directory.

### 2️⃣ Set Up a Virtual Environment (Recommended)

```bash
# Create a virtual environment
python -m venv phishing-env

# Activate the virtual environment
# On Windows:
phishing-env\Scripts\activate
# On Linux/Mac:
source phishing-env/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Prepare the Dataset
Ensure `phishing_urls.csv` is placed in the `dataset/` directory.

### 5️⃣ Train the Model

```bash
python main.py
```
This script will extract features, train a **RandomForestClassifier**, and save the model as `models/phishing_model.pkl`.

### 6️⃣ Running the Detector

#### 🖥️ Command Line Mode

```bash
python main.py --mode test --url "http://example.com"
```

#### 🖥️ GUI Mode

Run the following command to launch the GUI:

```bash
python main.py
```

## 📂 Project Structure

- `main.py` 🖥️: Main script for feature extraction, training, and testing
- `main.py` 🌍: GUI for real-time URL classification
- `models/phishing_model.pkl` 🔍: Trained ML model
- `dataset/phishing_urls.csv` 📂: Dataset of phishing and safe URLs
- `requirements.txt` 📜: Required dependencies

## 🔌 Customization and Extension

To extend the project:

1. 🔍 Modify `extract_features()` in `main.py` to include more URL-based heuristics.
2. 📡 Use a different machine learning model for better accuracy.
3. 🌐 Create an API to check URLs dynamically.

## 🛠️ Troubleshooting

### ⚠️ Common Issues

- **Dataset Not Found** 📂: Ensure `phishing_urls.csv` is in the correct directory.
- **Module Import Errors** 📜: Install dependencies using `pip install -r requirements.txt`.
- **GUI Not Opening** 🖥️: Ensure `tkinter` is installed (`sudo apt-get install python3-tk` on Linux).

## 🔒 Security Notes

- 🛑 Use the model responsibly and validate sources before blocking URLs.
- 🔐 Secure the dataset and model files from unauthorized modifications.
- 🌍 If integrating into a web service, consider rate-limiting requests.

## 🏆 Author

🌐 [GitHub](https://github.com/kunal-masurkar) <br> 👉 [LinkedIn](https://linkedin.com/in/kunal-masurkar-8494a123a)
