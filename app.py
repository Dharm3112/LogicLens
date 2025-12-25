# app.py
import streamlit as st
from src.model_loader import load_model, summarize_code
from src.analyzer import analyze_complexity

# --- Page Config ---
st.set_page_config(page_title="LogicLens", page_icon="🧠", layout="wide")

# --- Header ---
st.title("🧠 LogicLens: AI Code Explainer")
st.markdown("""
    **BTech 3rd Year Project** | Powered by *Salesforce CodeT5* & *Hugging Face Transformers*

    Paste a Python function below, and the AI will:
    1. 📝 **Explain** what the code does in plain English.
    2. 🐛 **Analyze** the complexity and predict bug probability.
""")

# --- Sidebar ---
st.sidebar.header("About")
st.sidebar.info(
    "This tool uses a Large Language Model (LLM) fine-tuned on millions of lines of code to understand syntax and logic.")

# --- Load Model (Cached) ---
with st.spinner('Loading AI Model... (First run takes ~30 seconds)'):
    tokenizer, model = load_model()

# --- User Input ---
code_input = st.text_area("Paste your Python Code here:", height=200,
                          value="def hello_world():\n    print('Hello World')")

if st.button("Analyze Code 🚀"):
    if code_input.strip() == "":
        st.warning("Please paste some code first!")
    else:
        col1, col2 = st.columns(2)

        # 1. AI Summarization
        with col1:
            st.subheader("📝 AI Explanation")
            with st.spinner("Analyzing logic..."):
                try:
                    summary = summarize_code(code_input, tokenizer, model)
                    st.success(summary)
                except Exception as e:
                    st.error(f"Error analyzing code: {e}")

        # 2. Complexity Analysis
        with col2:
            st.subheader("🐛 Bug Probability")
            risk_level, advice = analyze_complexity(code_input)

            st.metric(label="Risk Level", value=risk_level)
            st.info(advice)

            # Visual Indicator
            if risk_level == "Low":
                st.progress(10)
            elif risk_level == "Medium":
                st.progress(50)
            else:
                st.progress(90)

# --- Footer ---
st.markdown("---")
st.caption("Built with Streamlit & Transformers")