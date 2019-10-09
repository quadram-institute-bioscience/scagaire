FROM continuumio/anaconda3
RUN conda config --add channels defaults
RUN conda config --add channels bioconda
RUN conda config --add channels conda-forge
RUN conda install git
RUN conda install pip
RUN pip install git+git://github.com/quadram-institute-bioscience/scagaire.git
