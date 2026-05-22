"""
Data Processing Script for Bali Fiber AI Assistant
This script processes the raw CSV data, generates cluster documents,
creates embeddings, and saves everything as pickle files for efficient loading.
"""

import pandas as pd
import pickle
from sentence_transformers import SentenceTransformer
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

print("=" * 60)
print("BALI FIBER DATA PROCESSING PIPELINE")
print("=" * 60)

# ============================================
# 1. LOAD DATASET
# ============================================
print("\n[1/4] Loading dataset...")
df = pd.read_csv(
    'dataset/data_hasil_preprocessing.csv',
    sep=',',
    encoding='utf-8'
)
df.columns = df.columns.str.strip()

print(f"✓ Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")
print(f"✓ Columns: {df.columns.tolist()}")

# ============================================
# 2. GENERATE CLUSTER DOCUMENTS
# ============================================
print("\n[2/4] Generating cluster documents...")
cluster_docs = []
cluster_metadata = {}

for cluster_id in sorted(df['Cluster'].unique()):
    cluster_data = df[df['Cluster'] == cluster_id]
    
    # Informasi dominan
    dominant_segment = cluster_data['Segmentasi'].mode()[0]
    dominant_status  = cluster_data['Status'].mode()[0]
    dominant_product = cluster_data['Product'].mode()[0]
    dominant_offer   = cluster_data['offer status'].mode()[0]
    
    # Statistik numerik
    avg_bw    = cluster_data['B/W (Mbps)'].mean()
    avg_otc   = cluster_data['OTC'].mean()
    avg_mrc   = cluster_data['MRC'].mean()
    avg_total = cluster_data['GRAND TOTAL'].mean()
    total_customer = len(cluster_data)
    
    text = f"""
    Cluster {cluster_id} terdiri dari {total_customer} data pelanggan.
    Cluster ini didominasi oleh segmentasi {dominant_segment} dengan status {dominant_status}.
    Produk yang paling banyak digunakan adalah {dominant_product}.
    Mayoritas pelanggan memiliki offer status {dominant_offer}.
    Nilai rata-rata bandwidth sebesar {avg_bw:.4f} Mbps,
    rata-rata OTC sebesar {avg_otc:.4f},
    rata-rata MRC sebesar {avg_mrc:.4f},
    dan rata-rata GRAND TOTAL sebesar {avg_total:.4f}.
    Cluster ini merepresentasikan pola pelanggan berdasarkan
    aktivitas sales, produk layanan, dan potensi revenue.
    """
    
    cluster_docs.append(text)
    cluster_metadata[cluster_id] = {
        'total_customer': total_customer,
        'dominant_segment': dominant_segment,
        'dominant_status': dominant_status,
        'dominant_product': dominant_product,
        'dominant_offer': dominant_offer,
        'avg_bw': avg_bw,
        'avg_otc': avg_otc,
        'avg_mrc': avg_mrc,
        'avg_total': avg_total
    }

print(f"✓ Generated {len(cluster_docs)} cluster documents")

# Save cluster documents
with open('cluster_docs.pkl', 'wb') as f:
    pickle.dump(cluster_docs, f)
print("✓ Saved cluster_docs.pkl")

# Save cluster metadata
with open('cluster_metadata.pkl', 'wb') as f:
    pickle.dump(cluster_metadata, f)
print("✓ Saved cluster_metadata.pkl")

# ============================================
# 3. CREATE EMBEDDINGS
# ============================================
print("\n[3/4] Creating embeddings...")
embedding_function = HuggingFaceEmbeddings(
    model_name='sentence-transformers/all-MiniLM-L6-v2'
)
print("✓ Embedding model loaded")

# ============================================
# 4. CREATE VECTOR DATABASE
# ============================================
print("\n[4/4] Creating vector database...")
vectordb = Chroma.from_texts(
    texts=cluster_docs,
    embedding=embedding_function,
    persist_directory='cluster_db'
)

doc_count = vectordb._collection.count()
print(f"✓ Vector database created with {doc_count} documents")
print(f"✓ Database saved to: cluster_db/")

# ============================================
# SUMMARY
# ============================================
print("\n" + "=" * 60)
print("PROCESSING COMPLETE!")
print("=" * 60)
print(f"✓ Processed {df.shape[0]} customer records")
print(f"✓ Generated {len(cluster_docs)} cluster documents")
print(f"✓ Created vector database with {doc_count} embeddings")
print("\nGenerated files:")
print("  - cluster_docs.pkl (cluster text documents)")
print("  - cluster_metadata.pkl (cluster statistics)")
print("  - cluster_db/ (ChromaDB vector database)")
print("\nYou can now run the Streamlit app with: streamlit run app.py")
print("=" * 60)
