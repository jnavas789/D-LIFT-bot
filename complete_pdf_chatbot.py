
import streamlit as st
import os
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Set password directly in the code for this standalone version
# In production, use environment variables or Streamlit secrets
import streamlit as st  

# Password setup  
try:  
    ADMIN_PASSWORD = st.secrets["ADMIN_PASSWORD"]  
except:  
    ADMIN_PASSWORD = "your_secure_password"  # Fallback password  
# Sample summaries embedded directly in the code
# In production, these would be loaded from files
POLICY_SUMMARY = """
# Policy Learning Review Summary

## Introduction
This document summarizes the key findings from the Policy Learning Review Final Report dated October 22. The review examines policy development processes and implementation challenges across multiple sectors.

## Key Findings
The policy review identified several critical areas for improvement in policy formulation and implementation. Stakeholder engagement was found to be inconsistent across departments, with some showing exemplary practices while others struggled to incorporate diverse perspectives. Data-driven decision making was highlighted as a strength in some policy areas but lacking in others.

## Recommendations
The report recommends establishing standardized processes for stakeholder consultation, improving data collection and analysis capabilities, and creating feedback mechanisms to evaluate policy effectiveness. Cross-departmental collaboration should be strengthened to ensure policy coherence.

## Implementation Challenges
Several barriers to effective policy implementation were identified, including resource constraints, competing priorities, and insufficient monitoring frameworks. The report suggests that addressing these challenges requires both structural changes and capacity building.
"""

AGROECOLOGY_SUMMARY = """
# Agroecology Transition Report Summary

## Introduction
This document summarizes key insights from the Agroecology Transition Report. It covers challenges and recommendations for transitioning to agroecological practices.

## Key Findings
The report identifies market development, measurement of impacts, and sustainability of practices as significant challenges. There is a special focus on the importance of aligning academic research with farmer requirements.

## Recommendations
It suggests improving market linkages, rigorous impact assessment, and fostering long-term networks among stakeholders for a successful transition.
"""

# Function to split text by markdown sections
def chunk_text_by_sections(text):
    sections = re.split(r'(?=^#{1,2}\s+)', text, flags=re.MULTILINE)
    return [section.strip() for section in sections if section.strip()]

# Create tagged chunks
policy_chunks = ["[Policy Review] " + chunk for chunk in chunk_text_by_sections(POLICY_SUMMARY)]
agroecology_chunks = ["[Agroecology Report] " + chunk for chunk in chunk_text_by_sections(AGROECOLOGY_SUMMARY)]
all_chunks = policy_chunks + agroecology_chunks

# Build TF-IDF matrix
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(all_chunks)

# Search function
def search_chunks(query, top_k=3):
    query_vector = vectorizer.transform([query])
    similarity_scores = cosine_similarity(query_vector, tfidf_matrix)[0]
    top_indices = similarity_scores.argsort()[-top_k:][::-1]
    results = []
    for idx in top_indices:
        results.append({
            'chunk': all_chunks[idx],
            'similarity': similarity_scores[idx]
        })
    return results

# Generate response based on search results
def generate_response(query):
    results = search_chunks(query, top_k=3)
    if not results or results[0]['similarity'] < 0.1:
        return "I don't have enough information to answer that question based on the provided PDFs."
    response = "Based on the document summaries:\n\n"
    for r in results:
        if r['similarity'] > 0.1:
            response += f"{r['chunk']}\n\n"
    return response

# Secure access: simple password validation
def secure_access():
    st.sidebar.title("Access Control")
    password = st.sidebar.text_input("Enter password to access the chatbot", type="password")
    if password != ADMIN_PASSWORD:
        st.error("Incorrect password. Access denied.")
        st.stop()

# Main app function
def main():
    secure_access()
    st.title("Secure PDF Chatbot Interface")
    st.write("This chatbot helps answer questions based on secure PDF summaries. Your documents remain private and under your control.")
    query = st.text_input("Enter your query here:")
    if st.button("Submit Query") and query:
        with st.spinner("Processing your query..."):
            response = generate_response(query)
        st.text_area("Chatbot Response", value=response, height=300)

if __name__ == '__main__':
    main()
