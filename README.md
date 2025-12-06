# RAG-QASystem  
### ***AI Powered Question Answering Using PDF & Websites***

---

##  **Overview**

**RAG-QASystem** is an intelligent **Retrieval-Augmented Generation** application that allows users to:

-  Upload **PDF documents**
-  Provide a **Website URL**
-  Ask questions based on the extracted content
-  Receive accurate, contextual responses powered by **Gemini AI + LlamaIndex + HuggingFace Embeddings**

This system performs **offline embeddings (free)** and uses **Gemini LLM only during the answer generation**, optimizing both cost and accuracy.

---

##  **Key Features**

| Feature | Status |
|--------|:------:|
|  PDF content extraction | ✔️ |
|  Website scraping & text cleaning | ✔️ |
|  Embedding-based semantic search | ✔️ |
|  Gemini AI answer generation | ✔️ |
|  User-friendly UI with Streamlit | ✔️ |
|  Session-based caching (fast queries) | ✔️ |

---

##  **Tech Stack**

| Category | Technology Used |
|---------|-----------------|
| Framework | **Streamlit** |
| AI Model | **Google Gemini** |
| RAG Engine | **LlamaIndex** |
| Embeddings | **HuggingFace MiniLM-L6-v2** |
| Web Scraper | **Requests + BeautifulSoup** |
| PDF Reader | **LlamaIndex SimpleDirectoryReader** |

---

##  How It Works

---

### ** Step 1 — Load Content**

-  **Upload a PDF**
-  **OR Enter a Website URL**
-  System automatically **extracts, cleans, and preprocesses the text**

---

### ** Step 2 — Ask a Question**

-  Type any natural language query, e.g.:


---

### ** Step 3 — RAG Pipeline**

-  **Local Embeddings (HuggingFace)** → Finds the most relevant content chunks  
-  **Gemini AI Model** → Generates a final high-quality answer using retrieved context


---

### ** Step 4 — Response**

-  System displays a precise, context-aware answer
-  Includes reference to the original source (PDF or Website)

---
##  Run the Application Locally

Follow the steps below to launch the QASystem on your local machine using **Streamlit**.

---

### **1️ Activate Virtual Environment**

Make sure your virtual environment is active:


source venv/Scripts/activate   # Windows
source venv/bin/activate       # macOS/Linux

### **2️ Start the Streamlit App**

Run the application using Streamlit:

streamlit run StreamlitApp.py

3️ Open in Browser

Once the server starts successfully, Streamlit will automatically launch in your default browser.

4️ Use the App

📄 Upload a PDF

🌍 Or enter a website URL

💬 Ask questions — and the AI will respond using contextual understanding

If it does not open automatically, manually visit
