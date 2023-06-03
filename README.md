
![logo](img/amazonas.jfif)

# CODEFEST AD ASTRA 2023
##  Team ADL

Este proyetco está enfocado en lograr los retos propuestos por la Fuerza Aérea Colombiana y la Universidad de los Andes para el Codefest Ad Astra 2023.

### Objetivo 1. Identificación objetos de interés en videos

Para el desarrollo de este reto se realizaron los siguientes pasos:

1. Obtención de imágenes a partir de videos disponibles
2. Taggeo de imágenes: de acuerdo con el requerimiento se procedio a utilizar la aplicación disponible en la págima [https://www.makesense.ai/](https://www.makesense.ai/) identificando Construcciones, Vehiculos, Deforestacion para poder entrenar el modelo.
3. 

Enfoque de Zero-Shot (PreEtiquetado de Imagenes) - Objetivo realizar un etiquetado rapido y que permita descartar gran cantidad de imagenes que no aporten información valiosa a la generación de un modelo de detección de objetos posterior.

Clasificador de Imágenes Amazonia Obtenida Videos FAC

🐯 Tratamiento de Datos

Se utiliza la librería ffmpeg extraer imágenes de los videos y generar los fotogramas que seran procesados porteriormente, para instalar la librería se utiliza el comando:

!apt-get update --yes && apt-get install ffmpeg –yes

Una vez instalada ffmpeg se procede a tomar los videos de la ubicación donde se encuentren almacenados y se generan imágenes en una nueva carpeta la cual debe crear antes de ejecutar el comando. NOTA: Reemplace las rutas por las ubicaciones de sus archivos, este comando se debera ejecuatar para todos los videoes se observa un ejemplo a continuación

!ffmpeg -i Videos/VideoCodefest_001-11min.mpg -vf fps=1 Imagenes/VideoCodefest_001-11min/imagen_%04d_seg.jpg




### Objetivo 2: Identificación de entidades en noticias

Para el desarrollo de este reto se uso la libreria [WikiNEuRal](https://github.com/Babelscape/wikineural) 
el cual es un modelo preentrenado para reconocimiento de Entidades.

In a nutshell, WikiNEuRal consists in a novel technique which builds upon a multilingual lexical knowledge base (i.e., [BabelNet](https://babelnet.org/)) and transformer-based architectures (i.e., [BERT](https://arxiv.org/abs/1810.04805)) to produce high-quality annotations for multilingual NER. It shows consistent improvements of up to **6 span-based F1-score points against state-of-the-art alternative** data production methods on common benchmarks for NER. Moreover, in our paper we also present a new approach for creating **interpretable word embeddings** together with a **Domain Adaptation algorithm**, which enable WikiNEuRal to create **domain-specific training corpora**.





# How to use


# License 

Este proyecto está licenciado bajo licencia MIT de código abierto.

# Agradecimientos

Amplio agradecimiento a la Universidad de los Andes por brindarnos la oportunidad de participar de este Reto.  
A la Fuerza Aérea Colombiana por su apoyo, coordinación y gran iniciativa en beneficio del Amazonas Colombiano. 
A ADL Digital Lab por fortalecer y habilitar espacios de trabajo que faciliten este tipo de ejercicios.
A AWS por su apoyo en la habilitación de la infraestructura utilizada. 