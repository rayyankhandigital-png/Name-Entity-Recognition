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

## Python
## Streamlit — for the web interface
## Hugging Face Transformers — for the pre-trained NER model

## 🤖 Model

This project uses the following pre-trained model from Hugging Face:

## https://huggingface.co/learnrr/bert-base-ontonotes5-ner

## 📂 Project Structure


NER/
│
├── main.py
├── requirements.txt
└── README.md

### `app.py`

Contains the Streamlit user interface and the Named Entity Recognition code.

### `requirements.txt`

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

## 💻 How It Works

The project uses the Hugging Face `pipeline()` function to perform Named Entity Recognition.

## python
from transformers import pipeline

ner = pipeline(
    "ner",
    model="learnrr/bert-base-ontonotes5-ner",
    aggregation_strategy="simple"
)

text = "Apple hired John Smith in London"

result = ner(text)

for entity in result:
    print(entity)
```

The model analyzes the input text and identifies entities along with their labels and confidence scores.

## 📝 Example

### Input

```text
Apple hired John Smith in London.
```

### Output

```text
Apple       → Organization
John Smith  → Person
London      → Location
```

The exact entities and labels depend on the model's prediction.

## 📋 Requirements

## Model
## requirement.txt
## libraries
## app.py

> **Note:** Depending on your Python environment and Transformers setup, a backend such as PyTorch may also be required to run the model.


## 👨‍💻 Author

**Muhammad Rayyan Khan**

---

⭐ If you find this project useful, consider giving the repository a star!
