import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration


# Load the pre-trained model
def load_model(model_dir):
    model = T5ForConditionalGeneration.from_pretrained(model_dir)
    return model


# Load the tokenizer
def load_tokenizer(model_dir):
    tokenizer = T5Tokenizer.from_pretrained(model_dir)
    return tokenizer


def get_model_output(input_text, model, tokenizer):
    input_ids = tokenizer.encode(input_text, truncation=True, return_tensors='pt')
    output = model.generate(input_ids=input_ids, max_length=512)
    output_text = tokenizer.decode(output[0])
    return output_text





