

![logo](img/amazonas.jfif)

# CODEFEST AD ASTRA 2023
##  Team ADL

Este proyetco está enfocado en lograr los retos propuestos por la Fuerza Aérea Colombiana y la Universidad de los Andes para el Codefest Ad Astra 2023.

### Objetivo 1. Identificación objetos de interés en videos

Para el desarrollo de este reto se realizaron los siguientes pasos:

1. Obtención de imágenes a partir de videos disponibles
2. Taggeo de imágenes: de acuerdo con el requerimiento se procedio a utilizar la aplicación disponible en la págima [https://www.makesense.ai/](https://www.makesense.ai/) identificando Construcciones, Vehiculos, Deforestacion para poder entrenar el modelo.

# Cómo usar

Enfoque de Zero-Shot (PreEtiquetado de Imagenes) - Objetivo realizar un etiquetado rapido y que permita descartar gran cantidad de imagenes que no aporten información valiosa a la generación de un modelo de detección de objetos posterior.

Clasificador de Imágenes Amazonia Obtenida Videos FAC

🐯 Tratamiento de Datos

Se utiliza la librería ffmpeg extraer imágenes de los videos y generar los fotogramas que seran procesados porteriormente, para instalar la librería se utiliza el comando:

!apt-get update --yes && apt-get install ffmpeg –yes

Una vez instalada ffmpeg se procede a tomar los videos de la ubicación donde se encuentren almacenados y se generan imágenes en una nueva carpeta la cual debe crear antes de ejecutar el comando. NOTA: Reemplace las rutas por las ubicaciones de sus archivos, este comando se debera ejecuatar para todos los videoes se observa un ejemplo a continuación

!ffmpeg -i Videos/VideoCodefest_001-11min.mpg -vf fps=1 Imagenes/VideoCodefest_001-11min/imagen_%04d_seg.jpg

# Cómo usar
Para su uso:
1. Es necesario descargar el proyecto
2. Copiar el archivo codefestImagenes.py en la ruta del proyecto que necesita usar la libreria
3. Llamar la funcion detect_objects_in_video(video_path, output_path) ingresando los respectivos atributos:
   La salida donde se espera se escriba el json con el resultado


### Objetivo 2: Identificación de entidades en noticias

Para el desarrollo de este reto se uso la libreria [WikiNEuRal](https://github.com/Babelscape/wikineural) 
el cual es un modelo preentrenado para reconocimiento de Entidades.

In a nutshell, WikiNEuRal consists in a novel technique which builds upon a multilingual lexical knowledge base (i.e., [BabelNet](https://babelnet.org/)) and transformer-based architectures (i.e., [BERT](https://arxiv.org/abs/1810.04805)) to produce high-quality annotations for multilingual NER. It shows consistent improvements of up to **6 span-based F1-score points against state-of-the-art alternative** data production methods on common benchmarks for NER. Moreover, in our paper we also present a new approach for creating **interpretable word embeddings** together with a **Domain Adaptation algorithm**, which enable WikiNEuRal to create **domain-specific training corpora**.




* Objetivo 2:
Se crearon las funciones de ner_from_str y ner_from_file con la finalidad de obtener las entidades de los textos partiendo de una cadena de texto y un archivo respectivamente.


# Cómo usar
Para su uso:
1. Es necesario descargar el proyecto
2. Copiar el archivo codefestTextos.py en la ruta del proyecto que necesita usar la libreria
3. Importar la funcion a usar, ya sea ner_from_str o ner_from_file de este archivo de la siguiente forma
    from codefestTextos import ner_from_str, ner_from_file
4. Llamar cualquiera de las dos funciones segun sea la necesidad con los siguientes atributos:
    - Para el caso de querer obtener las entidades a partir de una cadena de texto, ingresa la cadena a procesar
    - Para el caso de querer obtener las entidades a partir de un archivo, ingresar la ruta del archivo a procesar
    Para el segundo atributo de ambas funciones se ingresar la ruta del archivo de salida donde se espera se escriba el json con el resultado

# Licencia

Este proyecto está licenciado bajo licencia MIT de código abierto.

# Agradecimientos

Amplio agradecimiento a la Universidad de los Andes por brindarnos la oportunidad de participar de este Reto.  
A la Fuerza Aérea Colombiana por su apoyo, coordinación y gran iniciativa en beneficio del Amazonas Colombiano. 
A ADL Digital Lab por fortalecer y habilitar espacios de trabajo que faciliten este tipo de ejercicios.
A AWS por su apoyo en la habilitación de la infraestructura utilizada. 
