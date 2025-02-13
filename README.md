# RAG for PDF query





## Retrieval Augmented Generation (RAG)

### Introduction

RAG is a method designed to address knowledge-intensive tasks, particularly in information retrieval. It combines an information retrieval component with a text generator model to achieve adaptive and efficient knowledge processing. Unlike traditional methods that require retraining the entire model for knowledge updates, RAG allows for fine-tuning and modification of internal knowledge without extensive retraining.

### Workflow

1. **Input**: RAG takes multiple pdf as input.
2. **VectoreStore**: The pdf's are then converted to vectorstore using FAISS and all-MiniLM-L6-v2 Embeddings model from Hugging Face.
3. **Memory**: Conversation buffer memory is used to maintain a track of previous conversation which are fed to the llm model along with the user query.
4. **Text Generation with GPT-3.5 Turbo**: The embedded input is fed to the GPT-3.5 Turbo model from the OpenAI API, which produces the final output.
5. **User Interface**: Streamlit is used to create the interface for the application.



## Project Features

1. **User-friendly Interface**: User friendly interface for interacting with pdf.

2. **Seamless Navigation**: Reducing complexity and enhancing the overall user experience.

## Getting Started

To use the PDF Intelligence System:

1. Clone the repository to your local machine.
   ```bash
   git clone https://github.com/sumitdwivedi/ChatPDF.git
   ```

2. Install dependencies.
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application.
   ```bash
   streamlit run app.py
   ```

4. Open your browser and navigate to `http://localhost:8000` to access the user interface.

## License



