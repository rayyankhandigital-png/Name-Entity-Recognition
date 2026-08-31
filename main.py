import streamlit as st
from transformers import pipeline

ner = pipeline(
    "ner",
    model="learnrr/bert-base-ontonotes5-ner",
    aggregation_strategy="simple"
)

st.title("Named Entity Recognition")

text = st.text_input(
    "Enter your text:",
    "Apple hired John Smith in London"
)

if st.button("Find Entities"):

    result = ner(text)

    st.subheader("Results")

    for entity in result:

        if entity["entity_group"] == "LOC":
            st.write("Location:", entity["word"])

        elif entity["entity_group"] == "PER":
            st.write("Person:", entity["word"])

        elif entity["entity_group"] == "ORG":
            st.write("Organization:", entity["word"])

        else:
            st.write(
                entity["entity_group"] + ":",
                entity["word"]
            )

