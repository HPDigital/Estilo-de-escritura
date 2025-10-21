"""
Estilo de escritura
"""

#!/usr/bin/env python
# coding: utf-8

# In[20]:


import os
from langchain.text_splitter import CharacterTextSplitter
from dotenv import load_dotenv
from openai import OpenAI

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener clave API de OpenAI desde variable de entorno
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Ruta donde se encuentran tus textos
ruta_textos = r"C:\Users\HP\Downloads"

# Función para leer los textos y combinarlos
def cargar_textos(ruta):
    textos = []
    for archivo in os.listdir(ruta):
        if archivo.endswith(".txt"):
            with open(os.path.join(ruta, archivo), "r", encoding="utf-8") as f:
                textos.append(f.read())
    return " ".join(textos)

# Cargar los textos
contenido_textos = cargar_textos(ruta_textos)

# Dividir en fragmentos para procesar con la API de OpenAI
text_splitter = CharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
fragmentos = text_splitter.split_text(contenido_textos)

# Analizar los textos y guardar el estilo como prompt personalizado
prompt_base = "Utiliza este texto como base para adaptarte a mi estilo: "
for i, fragmento in enumerate(fragmentos):
    prompt = prompt_base + fragmento
    try:
        response = client.chat.completions.create(
            model="gpt-4o",  # Cambia a 'gpt-3.5-turbo' si no tienes acceso a 'gpt-4'
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": "Describe mi estilo de redacción en términos de tono, estructura y vocabulario."}
            ]
        )
        estilo = response.choices[0].message.content.strip()
        print(f"Fragmento {i + 1}: {estilo}")
    except Exception as e:
        print(f"Error al conectar con la API de OpenAI: {str(e)}")  # Cambiado 'return' por 'print'

print("Análisis completado. Puedes usar el estilo identificado en tus programas.")


# In[22]:


import os
from langchain.text_splitter import CharacterTextSplitter
from dotenv import load_dotenv
from openai import OpenAI

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener clave API de OpenAI desde variable de entorno
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Ruta donde se encuentran tus textos
ruta_textos = r"C:\Users\HP\Downloads"

# Función para leer los textos y combinarlos
def cargar_textos(ruta):
    textos = []
    for archivo in os.listdir(ruta):
        if archivo.endswith(".txt"):
            with open(os.path.join(ruta, archivo), "r", encoding="utf-8") as f:
                textos.append(f.read())
    return " ".join(textos)

# Cargar los textos
contenido_textos = cargar_textos(ruta_textos)

# Dividir en fragmentos para procesar con la API de OpenAI
text_splitter = CharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
fragmentos = text_splitter.split_text(contenido_textos)

# Identificar estilo de redacción
def identificar_estilo(client, fragmentos, prompt_base):
    estilo_identificado = []
    for i, fragmento in enumerate(fragmentos):
        prompt = prompt_base + fragmento
        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "Eres un asistente que ayuda a identificar estilos de redacción, vocabulario y frases mas usadas."},
                    {"role": "user", "content": prompt + " Describe mi estilo de redacción en términos de tono, estructura y vocabulario."}
                ]
            )
            estilo = response.choices[0].message.content.strip()
            print(f"Estilo identificado del fragmento {i + 1}: {estilo}")
            estilo_identificado.append(estilo)
        except Exception as e:
            print(f"Error al conectar con la API de OpenAI para el fragmento {i + 1}: {str(e)}")
    return estilo_identificado

# Aplicar estilo de redacción a nuevos textos
def redactar_con_estilo(client, estilo, contenido):
    try:
        prompt = f"Adapta este contenido a mi estilo de redacción. Mi estilo es: {estilo}\nContenido:\n{contenido}"
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Eres un asistente que redacta contenido respetando un estilo de redacción específico."},
                {"role": "user", "content": prompt}
            ]
        )
        texto_redactado = response.choices[0].message.content.strip()
        return texto_redactado
    except Exception as e:
        print(f"Error al redactar texto: {str(e)}")
        return None

# Identificar el estilo basado en los fragmentos
prompt_base = "Utiliza este texto como base para adaptarte a mi estilo: "
estilo_identificado = identificar_estilo(client, fragmentos, prompt_base)

# Usar el estilo identificado para redactar un nuevo texto
nuevo_contenido = "Este es un texto de ejemplo que quiero que adaptes a mi estilo."
if estilo_identificado:
    # Combina los estilos identificados en caso de múltiples fragmentos
    estilo_combinado = " ".join(estilo_identificado)
    texto_redactado = redactar_con_estilo(client, estilo_combinado, nuevo_contenido)
    if texto_redactado:
        print("\nTexto redactado con tu estilo:")
        print(texto_redactado)
    else:
        print("No se pudo redactar el texto.")
else:
    print("No se pudo identificar el estilo de redacción.")


# In[26]:


import os
from langchain.text_splitter import CharacterTextSplitter
from dotenv import load_dotenv
from openai import OpenAI

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener clave API de OpenAI desde variable de entorno
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

contenido ="""1. Función: Pegar

La función "Pegar" en Excel, situada en el grupo Portapapeles de la pestaña Inicio, es una herramienta esencial para la manipulación de datos. Su principal objetivo es transferir información de una ubicación a otra dentro del mismo documento o entre diferentes archivos de Excel. Esto facilita la reorganización, duplicación o transformación de datos. Para usarla, primero se debe seleccionar y copiar la celda o rango de celdas requerido, luego se selecciona la celda destino y se aplica la función "Pegar". Esta función acelera la productividad y optimiza el flujo de trabajo al evitar la necesidad de reingresar los datos manualmente.

Para usar la función "Pegar" en Excel, siga estos pasos:

1. Abra el programa Microsoft Excel e ingrese al capítulo 1 de su documento.
2. Navegue hasta la pestaña "Inicio" ubicada en la parte superior de la interfaz de Excel. Esta pestaña se encuentra en la cinta de opciones, que es la barra de herramientas principal de Excel.
3. Una vez en la pestaña "Inicio", busque el grupo "Portapapeles". Este grupo se encuentra generalmente en el extremo izquierdo de la cinta de opciones.
4. Dentro del grupo "Portapapeles", encontrará la función "Pegar". Esta función permite insertar los datos que previamente ha copiado al portapapeles de su computadora.

Recuerde que debe tener datos ya copiados para poder usar la función "Pegar".

En el Capítulo 1, bajo la pestaña "Inicio" de Excel, encontramos el grupo "Portapapeles". Aquí se ubica la función "Pegar". Esta se utiliza después de copiar o cortar alguna celda, imagen o texto. Al seleccionar la opción "Pegar", el contenido copiado o cortado se inserta en la celda actualmente seleccionada. Es una herramienta indispensable para transferir rápidamente datos entre celdas, hojas o incluso libros de trabajo.
"""

prompt_base = """
A partir de ahora, redacta todo el contenido con este estilo de redacción:
- Tono: Profesional y cercano.
- Estructura: Frases claras y concisas, con párrafos bien definidos.
- Vocabulario: Uso de palabras precisas y neutras, evitando términos muy técnicos.
- Estilo: Incluye ejemplos cuando sea relevante y adapta el contenido para que sea fácil de entender.

Redacta este contenido con mi estilo: {contenido}
"""



def generar_con_estilo(client, contenido, prompt_base):
    prompt = prompt_base.format(contenido=contenido)
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Eres un asistente que redacta contenido siguiendo un estilo específico."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error al generar texto: {str(e)}")
        return None


generar_con_estilo(client, contenido, prompt_base)


# In[ ]:






if __name__ == "__main__":
    pass
