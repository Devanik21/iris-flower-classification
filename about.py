import streamlit as st

def about_page():
    # Custom CSS for styling
    st.markdown("""
        <style>
        .title {
            font-size: 40px;
            color: #4A90E2;
            font-weight: bold;
            text-align: center;
        }
        .description {
            font-size: 18px;
            color: #eddada;
            text-align: center;
            margin: 20px;
        }
        .highlight {
            color: #4A90E2;
            font-weight: bold;
        }
        .content {
            background-color: #041329;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }
        </style>
    """, unsafe_allow_html=True)

    # Title with custom styling

    
    # Main description with custom styling
    st.markdown("""
        <div class="content">
            <p class="description">
                Welcome to the <span class="highlight">Iris Species Predictor</span> application! This Streamlit app allows you to <span class="highlight">predict</span> the species of Iris flowers based on different features. 
                You can interact with the model, visualize various data aspects, and gain insights through the different pages of this app.
            </p>
            <p class="description">
                Features include:
                <ul>
                    <li><span class="highlight">Data Visualization</span> to explore the Iris dataset.</li>
                    <li><span class="highlight">Model Prediction</span> to classify Iris species.</li>
                    <li><span class="highlight">Data Analysis</span> with statistical insights and feature importance.</li>
                </ul>
            </p>
            <p class="description">
                This app was developed by <span class="highlight"><a href="https://www.linkedin.com/in/devanik/" style="color: #4A90E2;">Devanik</a></span> and <span class="highlight">Niki</span> (ChatGPT) to showcase advanced data science and machine learning techniques.
            </p>
        </div>
    """, unsafe_allow_html=True)
