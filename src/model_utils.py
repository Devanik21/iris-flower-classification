import joblib

def load_model(filepath: str):
    """Loads a pre-trained model pipeline from disk."""
    return joblib.load(filepath)
