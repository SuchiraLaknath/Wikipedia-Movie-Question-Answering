Here’s a **professionally formatted and grammatically correct** version of your `README.md` file — clear, concise, and ready for GitHub presentation:

---

# 🎬 Wikipedia Movie Question Answering (RAG System)

A **Retrieval-Augmented Generation (RAG)** system designed to answer questions about movie plots using the [Wikipedia Movie Plots Dataset](https://www.kaggle.com/datasets/jrobischon/wikipedia-movie-plots?resource=download).

---

## 🧠 Overview

This application retrieves and generates responses from the dataset using OpenAI models.
It is built for **OpenAI’s API** with the following configuration:

* **Language Model (LLM):** `gpt-5`
* **Embedding Model:** `text-embedding-3-large`
* **Vector Store:** [ChromaDB](https://www.trychroma.com)
* **Python Version:** 3.12
* **Operating System:** Linux

---

## ⚙️ Setup Instructions

1. **Create a Virtual Environment**

   ```bash
   python3.12 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Configure Environment Variables**

   * Rename `sample.env` to `.env`
   * Add your OpenAI API key:

     ```
     OPENAI_API_KEY=your_openai_api_key_here
     ```

3. **Download the Dataset**

   * Get the dataset from [Kaggle](https://www.kaggle.com/datasets/jrobischon/wikipedia-movie-plots?resource=download).
   * Extract and place the CSV file (`wiki_movie_plots_deduped.csv`) inside the `data/` directory.

---

## 🗄️ Storing Data in the Vector Database

1. Ensure the CSV path in `configs.py` is correctly set:

   ```python
   CSV_PATH = "data/wiki_movie_plots_deduped.csv"
   ```
2. Run the following script to insert data into the vector store:

   ```bash
   python store_database.py
   ```

---

## 💬 Querying the System

Once the data has been stored, you can start interacting with the system:

1. Run the main chat interface:

   ```bash
   python main.py
   ```
2. Type your questions in the terminal (e.g., *“What happend in Inception?”*).
3. To exit the chat, type `q` and press **Enter**.

---

## 📂 Directory Structure

```
.
├── data/
│   └── wiki_movie_plots_deduped.csv
├── chroma_db
├── retrivals
├── utils
├── store_database.py
├── main.py
├── configs.py
├── requirements.txt
├── sample.env
└── README.md
```

---

## 📝 Notes

* Ensure your OpenAI API key has access to the GPT-5 model.
* If you encounter incomplete rows in the dataset, they will be automatically ignored during processing.
* The chunk size for text embeddings is limited to **300 words** per segment.

---

- Video Demo : [Video Demonstration](https://drive.google.com/file/d/1NlSCS3s-FmPI_aWbz2amK-cKlwyg5pJW/view?usp=sharing).