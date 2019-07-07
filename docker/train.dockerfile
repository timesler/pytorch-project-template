FROM tiangolo/uvicorn-gunicorn-machine-learning:cuda9.1-python3.7

# Build conda environment
COPY environment.yml /environment.yml
RUN conda env update -n base -f /environment.yml --prune && \
    conda clean -ya
