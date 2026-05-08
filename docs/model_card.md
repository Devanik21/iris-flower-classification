# Model Card: Iris Flower Classification

## Model Details
- **Developer:** Devanik Debnath
- **Model Date:** 2024
- **Model Version:** 1.0
- **Model Type:** Random Forest Classifier (Iris_RF.pkl)
- **Information:** A multiclass classification model trained on the Iris dataset to predict flower species (setosa, versicolor, virginica) based on sepal and petal dimensions.

## Intended Use
- **Primary Use Cases:** Educational demonstration, interactive web application deployment, and real-world prediction analysis.
- **Out-of-Scope Uses:** Critical decision-making systems or domains outside of basic botanical classification.

## Training Data
- **Dataset:** Iris Dataset
- **Features:** Sepal Length, Sepal Width, Petal Length, Petal Width (in cm).

## Evaluation Results
- **Metrics:** Evaluated using standard classification metrics including accuracy, precision, recall, and F1-score on a held-out test set.

## Ethical Considerations
- **Bias:** The model is trained on a small, well-known dataset and is not expected to exhibit significant societal biases.
- **Risks:** The primary risk is misclassification, which is low given the simplicity of the task.
