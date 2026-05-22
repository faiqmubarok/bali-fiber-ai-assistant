# Bali Fiber AI Assistant

AI-powered customer segmentation analysis tool using RAG (Retrieval-Augmented Generation) technology. Get actionable business insights from cluster data powered by K-Prototypes clustering and Google Gemini AI.

## Features

- **Smart Clustering Analysis**: Analyze 1000+ customer records across 6 distinct clusters
- **RAG-Powered Insights**: Semantic search using ChromaDB and sentence transformers
- **AI Business Analyst**: Get strategic recommendations from Gemini AI
- **Modern UI**: Clean, professional interface with orange brand identity
- **Optimized Performance**: Pre-processed data with pickle files for fast loading

## Installation

1. Clone this repository:
```bash
git clone <your-repo-url>
cd tubes-ai
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure your Gemini API key in `.streamlit/secrets.toml`:
```toml
GEMINI_API_KEY = "your-api-key-here"
```

## Data Processing

**First time setup:** Process the raw data to generate embeddings and vector database:

```bash
python process_data.py
```

This will generate:
- `cluster_docs.pkl` - Cluster text documents
- `cluster_metadata.pkl` - Cluster statistics  
- `cluster_db/` - ChromaDB vector database

**Alternative:** You can also use the Jupyter notebook `AI_2_LOCAL.ipynb` for step-by-step processing.

**Note:** You only need to run this once, or when you update the source data in `dataset/data_hasil_preprocessing.csv`

## Running the App

```bash
streamlit run app.py
```

The app will be available at `http://localhost:8501`

## Project Structure

```
tubes-ai/
├── app.py                          # Main Streamlit application
├── process_data.py                 # Data processing script
├── AI_2_LOCAL.ipynb               # Jupyter notebook for data processing
├── dataset/
│   └── data_hasil_preprocessing.csv  # Source data (1060 records)
├── cluster_db/                     # ChromaDB vector database
├── cluster_docs.pkl               # Pre-processed cluster documents
├── cluster_metadata.pkl           # Cluster statistics
├── .streamlit/
│   ├── config.toml                # Streamlit configuration
│   └── secrets.toml               # API keys (not in git)
└── requirements.txt               # Python dependencies
```

## How It Works

1. **Data Processing**: Customer data is clustered using K-Prototypes algorithm (6 clusters)
2. **Document Generation**: Each cluster is converted to descriptive text with statistics
3. **Embedding Creation**: Text is embedded using sentence-transformers
4. **Vector Storage**: Embeddings stored in ChromaDB for semantic search
5. **RAG Pipeline**: User queries retrieve relevant clusters and generate AI insights

## Technology Stack

- **Frontend**: Streamlit
- **AI Model**: Google Gemini 2.5 Flash
- **Vector DB**: ChromaDB
- **Embeddings**: Sentence Transformers (all-MiniLM-L6-v2)
- **Framework**: LangChain
- **Clustering**: K-Prototypes

## Usage

1. Start the app with `streamlit run app.py`
2. Choose a suggested question or type your own
3. Ask questions about:
   - Customer clusters and segmentation
   - Churn risk analysis
   - Sales priorities
   - Revenue potential
   - Business strategy
4. View AI-generated insights with source context

## Troubleshooting

**"Failed to load vector database"**
- Run `python process_data.py` to generate the database

**"API key not found"**
- Create `.streamlit/secrets.toml` and add your Gemini API key

**"Question outside scope"**
- Use keywords like: cluster, customer, sales, churn, potential, strategy, analysis

**App is slow on first run**
- Normal - downloading embedding model (~90MB)
- Subsequent runs will be faster (models are cached)

## Sharing the Database

If you need to share the processed data with team members:

1. **Share the pickle files and database folder:**
   ```bash
   # Create a zip file
   zip -r bali-fiber-data.zip cluster_db/ cluster_docs.pkl cluster_metadata.pkl
   ```

2. **Team members can extract and use directly:**
   ```bash
   unzip bali-fiber-data.zip
   streamlit run app.py
   ```

No need to re-run `process_data.py` if using shared files.

## License

This project is for educational purposes.
