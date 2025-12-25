# src/model_loader.py
import streamlit as st  # <--- THIS WAS MISSING
from transformers import RobertaTokenizer, T5ForConditionalGeneration
import torch


@st.cache_resource  # This works now because 'st' is imported
def load_model():
    model_name = "Salesforce/codet5-base-multi-sum"

    # Using st.write or print here might clutter the UI, so we just log to console
    print("Downloading Model... this might take a minute...")

    tokenizer = RobertaTokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name)

    return tokenizer, model


def summarize_code(snippet, tokenizer, model):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = model.to(device)

    input_ids = tokenizer(snippet, return_tensors="pt").input_ids.to(device)

    # Generate the summary
    generated_ids = model.generate(input_ids, max_length=150)
    summary = tokenizer.decode(generated_ids[0], skip_special_tokens=True)

    return summary