ih dfh


# 🧠 LogicLens: AI-Powered Code Assistant

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit)
![HuggingFace](https://img.shields.io/badge/Hugging%20Face-Transformers-yellow?style=for-the-badge&logo=huggingface)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

> *An intelligent tool that reads code and explains it in plain English using State-of-the-Art NLP models.*

---

## 📖 Table of Contents
- [About the Project](#-about-the-project)
- [Key Features](#-key-features)
- [Tech Stack](#-tech-stack)
- [Folder Structure](#-folder-structure)
- [Installation & Setup](#-installation--setup)
- [Usage](#-usage)
- [Future Enhancements](#-future-enhancements)
- [Troubleshooting](#-troubleshooting)

---

## 🧐 About the Project
**LogicLens** is a developer tool designed to bridge the gap between complex code syntax and human readability. By leveraging the **Salesforce CodeT5** model (based on the T5 architecture), LogicLens can analyze Python code snippets and generate accurate, human-readable summaries.

Additionally, it calculates **Cyclomatic Complexity** to provide a "Risk Score," helping developers identify code that is prone to bugs or difficult to maintain.

## 🚀 Key Features
* **🤖 AI Code Summarization:** Instantly converts Python functions into clear English explanations.
* **📉 Complexity Analysis:** visualizes the risk level of code using industry-standard metrics (Cyclomatic Complexity).
* **⚡ Real-Time Processing:** Powered by `st.cache_resource` for fast inference after the initial model load.
* **🎨 Clean UI:** Built with Streamlit for a responsive and modern user interface.

---

## 🛠 Tech Stack
| Component | Technology | Description |
| :--- | :--- | :--- |
| **Frontend** | Streamlit | Web application framework |
| **AI Model** | CodeT5 (Salesforce) | Text-to-Text Transformer specialized for Code |
| **ML Engine** | PyTorch & Transformers | Deep learning backend |
| **Analysis** | Radon | Static code analysis tool for metrics |

---

## 📂 Folder Structure
```text
LogicLens/
│
├── app.py                 # Main Streamlit application entry point
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
│
└── src/                   # Source code package
    ├── __init__.py        # Package initializer
    ├── model_loader.py    # Model caching and inference logic
    └── analyzer.py        # Complexity calculation algorithms

```

---

## ⚙️ Installation & Setup

Follow these steps to set up the project locally.

### 1. Clone the Repository

```bash
git clone [https://github.com/your-username/LogicLens.git](https://github.com/your-username/LogicLens.git)
cd LogicLens

```

### 2. Create a Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate

```

### 3. Install Dependencies

```bash
pip install -r requirements.txt

```

*Note: This will install PyTorch and Transformers. The download size may be approx 1-2GB.*

### 4. Run the Application

```bash
streamlit run app.py

```

---

## 🖥 Usage

1. Open the link provided in your terminal (usually `http://localhost:8501`).
2. Wait for the model to download (only happens on the first run).
3. Paste a Python function into the text area.
4. Click **"Analyze Code 🚀"**.
5. View the **AI Explanation** on the left and the **Bug Probability** on the right.

---

## 🔮 Future Enhancements

*These are features planned for V2.0 to make LogicLens a production-grade tool:*

1. **Multi-Language Support:** Extend support to C++, Java, and JavaScript using the `CodeT5-multi` model capabilities.
2. **IDE Extension:** Wrap this logic into a **VS Code Extension** so developers can get explanations directly in their editor.
3. **Code Optimization Suggestions:** Upgrade the AI to not just explain, but also *refactor* the code (e.g., "Suggest changing O(n²) loop to O(n)").
4. **GitHub Integration:** Allow users to paste a GitHub URL instead of raw code to analyze entire files.
5. **Dark Mode & Syntax Highlighting:** Improve the UI to auto-detect language syntax for better readability.

---

## 🔧 Troubleshooting

**Q: The app crashes with `NameError: name 'st' is not defined`.** A: Ensure you have `import streamlit as st` at the top of your `src/model_loader.py` file.

**Q: The model download is stuck.** A: Check your internet connection. The model is large (~800MB). If it fails, delete the cache and try again.

**Q: "Out of Memory" (OOM) error?** A: If you are on a machine with low RAM, try using a smaller model version like `Salesforce/codet5-small` in `model_loader.py`.

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📜 License

Distributed under the MIT License. See [LICENSE](https://github.com/Dharm3112/LogicLens/blob/main/LICENSE) for more information.

---

<p align="center">
  <b>LogicLens</b> • Created by <a href="https://github.com/Dharm3112"><b>Dharm Patel</b></a>
</p>
