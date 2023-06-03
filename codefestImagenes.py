import os
from glob import glob as gb
import os
import pandas as pd
import json
import codefestImagenes as ci
from PIL import Image
import requests
from transformers import CLIPProcessor, CLIPModel

def obtener_rutas_archivos(ubicacionCarpeta):
    ruta = os.path.abspath(ubicacionCarpeta)
    pathArchivos = gb(ruta + '/*.jpg')
    return pathArchivos


def preEtiquetadoImagenes(listaubicaArchivos):
    model = CLIPModel.from_pretrained("openai/clip-vit-large-patch14")
    processor = CLIPProcessor.from_pretrained("openai/clip-vit-large-patch14")
    etiquetado = {}
    for imag in listaubicaArchivos:
        df = {}
        url = imag
        image = Image.open(url)
        inputs = processor(text=["deforestation", "construction","jungle","river","boat","machinery","builds","clouds"],images=image, return_tensors="pt", padding=True)
        imagen = imag.split("/")[-1] +"_"+ imag.split("/")[-2]
        outputs = model(**inputs)
        logits_per_image = outputs.logits_per_image # this is the image-text similarity score
        probs = logits_per_image.softmax(dim=1) # we can take the softmax to get the label probabilities
        Etiqueta = ["deforestation", "construction","jungle","river","boat","machinery","builds","clouds"]
        Probabilidad = probs[0]*100
        df['Etiqueta'] = Etiqueta
        lista = list(Probabilidad.detach().numpy())
        df['Probabilidad'] = list(map(str, lista))
        etiquetado[imagen] = df
    with open("archivo-salida.json", "w") as outfile:
        json.dump(etiquetado, outfile)
