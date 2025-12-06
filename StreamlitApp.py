import streamlit as st
from QAWithPDF.data_ingestion import load_data
from QAWithPDF.embedding import create_or_load_index
from QAWithPDF.model_api import load_model
from QAWithPDF.web_loader import load_website
from logger import logging


@st.cache_resource(show_spinner=False)
def load_cached_model():
    return load_model()


@st.cache_resource(show_spinner=False)
def get_query_engine(model, documents):
    return create_or_load_index(model, documents)


def main():
    st.set_page_config(page_title="AI RAG - PDF + Website", layout="centered")

    st.title("AI Powered PDF & Website Question Answering System")
    st.write("Upload a PDF or enter a Website URL, then ask any question.")


    if "documents" not in st.session_state:
        st.session_state.documents = None
    if "source_name" not in st.session_state:
        st.session_state.source_name = None

    option = st.radio("Choose Input Source:", ["PDF", "Website URL"])

    
    if option == "PDF":
        uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
        
        if uploaded_file:
            st.success(f"Uploaded: **{uploaded_file.name}**")

            with open(f"data/{uploaded_file.name}", "wb") as f:
                f.write(uploaded_file.getbuffer())

            st.session_state.documents = load_data("data")
            st.session_state.source_name = uploaded_file.name

    elif option == "Website URL":
        url = st.text_input("Enter Website URL:")

        if st.button("Fetch Website"):
            if url.strip():
                with st.spinner("Extracting Website Content... "):
                    st.session_state.documents = load_website(url)
                    st.session_state.source_name = url
                st.success("Website loaded successfully!")
            else:
                st.warning("⚠ Please enter a valid URL.")

    st.divider()


    question = st.text_input("Ask your question:")

    if st.button("Run Query"):

        if st.session_state.documents is None:
            st.warning("⚠ Please upload a PDF or load a website first.")
            return

        if not question.strip():
            st.warning("⚠ Please enter a question.")
            return

        with st.spinner("Thinking... "):
            try:
                model = load_cached_model()
                query_engine = get_query_engine(model, st.session_state.documents)
                response = query_engine.query(question)

                st.subheader(" Answer:")
                st.write(response.response)

                st.caption(f" Source Used: {st.session_state.source_name}")

            except Exception as e:
                logging.error(f"Error: {e}")
                st.error(" Something went wrong while processing the query.")

if __name__ == "__main__":
    main()
