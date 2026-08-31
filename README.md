# Name-Entity-Recognition Application (NER)
# Named Entity Recognition (NER) 🧠

A simple **Named Entity Recognition (NER)** web application built using **Python, Streamlit, and Hugging Face Transformers**.

## 🎯 Purpose of the Project

This project was created to demonstrate how **Natural Language Processing (NLP)** and **Named Entity Recognition** can be implemented using a pre-trained Transformer model and a simple Streamlit interface.


The application takes text from the user and identifies named entities such as **people, organizations, locations, dates, and other entities** using a pre-trained BERT-based NER model.

## 🚀 Features

* Enter any text for analysis
* Detect named entities automatically
* Display entity names
* Display entity types/labels
* Display confidence scores
* Simple and user-friendly Streamlit interface
* Uses a pre-trained BERT NER model

## 🛠️ Technologies Used

 Python
 
 Streamlit — for the web interface
 
 Hugging Face Transformers — for the pre-trained NER model

## 🤖 Model

This project uses the following pre-trained model from Hugging Face:

 https://huggingface.co/learnrr/bert-base-ontonotes5-ner

## 📂 Project Structure
NER-Project/

│

├── main.py

├── README.md

└── requirements.txt

### `app.py`

Contains the Streamlit user interface and the Named Entity Recognition code.

### `requirements.txt`
streamlit
transformers
torch

Contains the Python libraries required to run the project.

### `README.md`

Contains information and instructions about the project.

## 📦 Installation
### 1. Install the Required Libraries
## bash
requirements.txt

pip install streamlit transformers torch


## ▶️ Run the Application

## bash
streamlit run app.py


The application will open in your web browser.

## 🔍 How Named Entity Recognition Works

1. The user types a sentence into the **Streamlit application**.
2. The **Transformers pipeline** receives and processes the text.
3. The **BERT model** examines the words and their context.
4. The model detects important names and assigns categories such as **Person, Location, Organization**, and others.
5. The detected entities and their categories are shown to the user in the **Streamlit interface**.
 
## 📋 Other Requirements

 Model
 
 requirement.txt
 
 libraries
 
 app.py

> **Note:** Depending on your Python environment and Transformers setup, a backend such as PyTorch may also be required to run the model.


## 👨‍💻 Author

**Muhammad Rayyan Khan**

---

⭐ If you find this project useful, consider giving the repository a star!
