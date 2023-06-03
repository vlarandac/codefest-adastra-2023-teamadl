import pandas as pd
import json

from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
import torch

device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

tokenizer = AutoTokenizer.from_pretrained("Babelscape/wikineural-multilingual-ner")
model = AutoModelForTokenClassification.from_pretrained("Babelscape/wikineural-multilingual-ner")

classifier = pipeline("zero-shot-classification", 
                       model="Recognai/bert-base-spanish-wwm-cased-xnli")
nlp = pipeline("ner", model=model, tokenizer=tokenizer, grouped_entities=True)
ruta = "NOTICIAS DE LA AMAZONIA_CODEFEST.xlsx"
data = pd.read_excel(ruta)

def etiquetado_textos(texto):
    x= classifier(
            texto,
            candidate_labels=["mineria", "deforestacion", "contaminacion", "ninguno"],
            hypothesis_template="Este ejemplo es {}."
            )
    resultado = x['scores']   
    etiqueta = x['labels'] [resultado.index(max(resultado))]
    return etiqueta

def ner_from_str(text, output_path):
    ner_results = nlp(text)
    salida = {}
    salida["text"] = text
    salida["ORG"] = []
    salida["LOC"] = []
    salida["PER"] = []
    salida["DATES"] = []
    salida["MISC"] = []
    salida["IMPACT"] = [etiquetado_textos(text)]
    for i in ner_results:
        salida[i["entity_group"]].append(i["word"])
    for i in salida:
        if i != "text":
            salida[i] = list(dict.fromkeys(salida[i]))

    with open(output_path, "w") as outfile:
        json.dump(salida, outfile)

def ner_from_file(file_path, output_path):
    with open(file_path) as f:
        text = " ".join(f.readlines())

    ner_results = nlp(text)
    salida = {}
    salida["text"] = text
    salida["ORG"] = []
    salida["LOC"] = []
    salida["PER"] = []
    salida["DATES"] = []
    salida["MISC"] = []
    salida["IMPACT"] = [etiquetado_textos(text)]
    for i in ner_results:
        salida[i["entity_group"]].append(i["word"])
    for i in salida:
        if i != "text":
            salida[i] = list(dict.fromkeys(salida[i]))
    with open(output_path, "w") as outfile:
        json.dump(salida, outfile)
