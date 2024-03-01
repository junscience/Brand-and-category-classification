import requests
from sentence_transformers.util import semantic_search
import torch
import numpy as np


model_id = "sentence-transformers/all-MiniLM-L6-v2"
hf_token = "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"

api_url = f"https://api-inference.huggingface.co/pipeline/feature-extraction/{model_id}"
headers = {"Authorization": f"Bearer {hf_token}"}


def query(texts):
    response = requests.post(api_url, headers=headers, json={"inputs": texts, "options": {"wait_for_model": True}})
    return response.json()


def embedding_data(text):
    embedding = query(text)
    embedding_tensor = torch.from_numpy(np.array(embedding)).to(torch.float)
    return embedding_tensor


def semantic(DB_embed, input_embed):
    hits = semantic_search(input_embed, DB_embed, top_k=1)
    return hits


def model_hits(hits):
    predict = []
    predict_quality = []

    for element in hits:
        for i in element:
            predict.append(str(i['corpus_id']))
            predict_quality.append(str(i['score']))

    dictionary = {'predict': predict, 'predict_quality': predict_quality}
    return dictionary

