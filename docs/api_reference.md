# API Reference

This document outlines the API endpoints and programmatic interfaces for the Iris Flower Classification project.

## Streamlit Application
The main application is a Streamlit web app, which does not expose a traditional REST API. However, the underlying scripts can be imported and utilized as modules.

### Modules

#### `predict.py`
- Handles the core inference logic using the loaded scikit-learn model.
- Contains functions to preprocess input data and return predictions with confidence scores.

#### `analyze.py`
- Provides data analysis and exploration capabilities for the Iris dataset.
- Includes functions for generating statistical summaries.

#### `visualize.py`
- Contains plotting functions (e.g., using Plotly) to visualize data distributions, model evaluations (confusion matrix), and feature importance.

#### `main.py`
- The entry point for the Streamlit application, organizing the UI layout and calling functions from other modules.

#### `about.py` & `feedback.py`
- Provide information about the project and handle user feedback via the UI.
