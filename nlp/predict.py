from typing import List, Tuple
from transformers import BertForTokenClassification, BertTokenizerFast, Trainer
from datasets import Dataset

from core.config import settings


class NERPredictor:
    """
    Named Entity Recognition (NER) predictor using a pre-trained BERT model.
    """

    def __init__(self) -> None:
        self.model_path = settings.MODELS_DIR + "/ner"
        self.label_list = [
            "O",
            "B-PER",
            "I-PER",
            "B-ORG",
            "I-ORG",
            "B-LOC",
            "I-LOC",
            "B-MISC",
            "I-MISC",
        ]

        self.model: BertForTokenClassification = (
            BertForTokenClassification.from_pretrained(self.model_path)
        )
        self.tokenizer: BertTokenizerFast = BertTokenizerFast.from_pretrained(
            self.model_path
        )
        self.trainer: Trainer = Trainer(model=self.model)

    def _prepare_dataset(self, sentence: str) -> Dataset:
        """
        Converts a sentence into a dataset with tokenized words.

        :param sentence: Input sentence as a string.
        :return: A dataset containing tokenized words.
        """
        tokens: List[str] = sentence.split()
        return Dataset.from_dict({"tokens": [tokens]})

    def _tokenize_data(self, dataset: Dataset) -> Dataset:
        """
        Tokenizes the dataset properly for model inference.

        :param dataset: The dataset to tokenize.
        :return: Tokenized dataset.
        """

        def tokenize_example(example: dict) -> dict:
            return self.tokenizer(
                example["tokens"],
                truncation=True,
                padding="max_length",
                max_length=128,
                is_split_into_words=True,
            )

        return dataset.map(tokenize_example)

    def predict(self, sentence: str) -> Tuple[List[str], List[str]]:
        """
        Runs Named Entity Recognition (NER) prediction on the given sentence.

        :param sentence: Input sentence as a string.
        :return: Tuple containing tokens and their corresponding predicted entity labels.
        """
        dataset: Dataset = self._prepare_dataset(sentence)
        tokenized_data: Dataset = self._tokenize_data(dataset)
        predictions = self.trainer.predict(tokenized_data)
        predicted_labels = predictions.predictions.argmax(-1)
        tokens: List[str] = sentence.split()
        predicted_tags: List[str] = [
            self.label_list[p] for p in predicted_labels[0][: len(tokens)]
        ]

        return tokens, predicted_tags
