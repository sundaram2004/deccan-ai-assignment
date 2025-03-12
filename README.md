# Deccan AI Assignment

## Requirements

- [Docker](https://docs.docker.com/engine/install/)
- Download the trained model from [here](https://drive.google.com/file/d/1RQg2UpplJ4lTFCSj7q8murmxYI8GjjY-/view?usp=sharing)

## Setup

- Clone the repository:
  ```bash
  git clone https://github.com/sundaram2004/deccan-ai-assignment.git
    ```
- Run `cp .env.sample .env` and update the environment variables in the `.env` file.
- Move the downloaded model files to the `models/ner` directory. 
- Run `make` or `docker compose up --build -d` to start the api server and streamlit app
at the configured ports.

Explore Makefile for more commands.

# **Report**

## Introduction
Named Entity Recognition (NER) is a Natural Language Processing (NLP) task that identifies entities such as persons, organizations, locations, and others in textual data. This report outlines the approach taken to preprocess data, train and evaluate an NER model using BERT.

## Data Preprocessing
### Dataset Selection
I used the CoNLL-2003 Named Entity Recognition dataset, which is a standard benchmark dataset for NER tasks. The dataset consists of tokenized text along with entity labels.

### Exploratory Data Analysis (EDA)
- Loaded and examined dataset size.
- Visualized entity tag distribution using a bar plot to understand class imbalance.
- Extracted named entity tags from the dataset.

### Preprocessing Steps
- **Tokenization:** Used BERT's tokenizer (`BertTokenizerFast`) to split text into subword tokens.
- **Entity Alignment:** Aligned entity labels with tokenized words, ensuring that subword tokens inherited entity labels from the original words.
- **Padding and Truncation:** Applied `max_length=128` to ensure uniform input size.
- **Stopword Removal & Lemmatization:** These were not explicitly performed since transformer-based models inherently handle contextual information.

## Model Training & Evaluation
### Model Selection
I fine-tuned a `bert-base-cased` transformer model from Hugging Face (`BertForTokenClassification`) for NER.

### Loss Function with Class Weights
- Computed class weights to address class imbalance.
- Modified the model to incorporate weighted `CrossEntropyLoss`.

### Hyperparameter Tuning
Used `Optuna` to optimize hyperparameters:
- Learning rate (`1e-5` to `5e-5`)
- Batch size (`8, 16, 32`)
- Weight decay (`0.01` to `0.1`)
- Number of epochs (`3-5`)

Best hyperparameters found:
- Learning rate: `2.23e-05`
- Batch size: `32`
- Epochs: `3`
- Weight decay: `0.027`

### Training Strategy
- Used `Trainer` from `transformers` with evaluation after each epoch.
- Set `load_best_model_at_end=True` to retain the best model.
- Fine-tuned the model using the training dataset and validated performance on the development dataset.

### Evaluation Metrics
- **F1 Score (Weighted):** `Final F1 Score = 0.91`
- **Precision, Recall, and Accuracy:** Evaluated using `seqeval` and `sklearn.metrics`.

## Conclusion
This project successfully implemented an NER model using BERT and fine-tuned it for optimal performance. The model achieved high accuracy and F1-score.
