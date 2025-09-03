import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post

# Options for length and language
length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]

# Main app layout
def main():
    st.title("LinkedIn Post Generator 🤖")
    
    # About the Project section
    with st.expander("About This Project"):
        st.write("""
        **Project Overview:**
        Ye project ek AI-powered tool hai jo **Groq Llama-3** LLM ko use karke LinkedIn posts generate karta hai. Iska maqsad hai logon ko engaging aur human-like content create karne mein help karna.
        
        **Tech Stack:**
        - **Frontend:** Streamlit 🎈
        - **Backend:** Python
        - **Core Logic:** LangChain and Groq API
        - **Data Handling:** Pandas 🐼
        
        **How it Works:**
        - **Few-Shot Learning:** Humne few-shot examples use kiye hain taake LLM best performing posts ka style aur tone seekh sake.
        - **Prompt Engineering:** Har post ke liye dynamic prompts banaye hain jo user ki selections (topic, length, language) par depend karte hain.
        """)

    st.subheader("Generate Your Post ✍️")

    # Create three columns for the dropdowns
    col1, col2, col3 = st.columns(3)

    fs = FewShotPosts()
    tags = fs.get_tags()
    with col1:
        selected_tag = st.selectbox("Topic", options=tags)

    with col2:
        selected_length = st.selectbox("Length", options=length_options)

    with col3:
        selected_language = st.selectbox("Language", options=language_options)

    # Generate Button
    if st.button("Generate"):
        post = generate_post(selected_length, selected_language, selected_tag)
        st.write(post)

# Run the app
if __name__ == "__main__":
    main()