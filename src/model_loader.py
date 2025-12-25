# src/model_loader.py
from transformers import RobertaTokenizer, T5ForConditionalGeneration
import torch


@st.cache_resource  # This is a Streamlit magic command to cache the model so it doesn't reload every time
def load_model():
    model_name = "Salesforce/codet5-base-multi-sum"

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