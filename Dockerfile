FROM dsblab/single_cell_analysis:0.7

USER jovyan

RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
# Install libraries the right way
RUN pip install -U "https://storage.googleapis.com/jax-releases/cuda12/jaxlib-0.4.16+cuda12.cudnn89-cp311-cp311-manylinux2014_x86_64.whl"
RUN pip install jax==0.4.16 
