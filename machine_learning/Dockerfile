FROM continuumio/anaconda3

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt /tmp/requirements.txt

# Instala las dependencias desde requirements.txt
RUN conda install --yes --file /tmp/requirements.txt

# Descarga las stopwords de NLTK
RUN python -m nltk.downloader stopwords

# Establece el directorio de trabajo
WORKDIR /opt/notebooks

# Ejecuta Jupyter Notebook
CMD ["/bin/bash", "-c", "source activate base && jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root --notebook-dir=/opt/notebooks"]
