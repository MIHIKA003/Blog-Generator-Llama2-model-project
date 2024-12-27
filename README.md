# Blog-Generator-Llama2-model-project
A Streamlit-powered blog generator using a local Llama 2-based LLM for customizable blog writing. Enter topics, select audience types, and generate content with ease!

# BlogBot - A Blog Generator Powered by Llama 2

![Streamlit](https://img.shields.io/badge/Streamlit-v1.0-brightgreen) 
![Llama 2](https://img.shields.io/badge/Llama--2-7B-blue)
![Python](https://img.shields.io/badge/Python-3.11-yellow)

## 📝 Project Overview

**BlogBot** is a blog generation tool built with **Streamlit** that uses a locally deployed **Llama 2-based Large Language Model (LLM)**. This app allows users to:
- Generate blogs on any topic.
- Customize the audience type (e.g., Researchers, Data Scientists, Students).
- Specify the desired word count.

Whether you're creating content for academic purposes, casual readers, or technical audiences, BlogBot makes it simple and efficient!

---

## 🚀 Features

- **Customizable Blog Generation**:
  - Define your topic, word count, and audience type.
- **Local Model Execution**:
  - Runs the Llama 2 7B model locally using the **CTransformers** library.
  - Quantized model for efficient inference on standard hardware.
- **Interactive UI**:
  - Built with Streamlit for a seamless and intuitive user experience.

---

### Prerequisites
1. Python 3.11 or 3.10 (recommended).
2. Dependencies:
   - Streamlit
   - LangChain
   - CTransformers
3. Llama 2 7B quantized model (`ggmlv3.q8_0.bin`).

---

  
