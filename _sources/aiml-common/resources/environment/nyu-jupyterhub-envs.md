# NYU JupyrterHub Environments

The steps to define an environment by the instructor is as follows:


1.  Create the environment

```bash
conda create -n sidewalks-torch
```

2. Activate the environment

```bash 
conda activate sidewalks-torch
```

3. Install the packages

```bash
mamba install cudatoolkit=11.8 ipykernel pytorch=*=*cuda11.8* ipykernel pip numpy pandas pyarrow matplotlib statsmodels scikit-learn seaborn requests tqdm nltk joblib spacy openpyxl wordcloud gensim transformers umap-learn plotly openai langchain sentence-transformers ultralytics opencv segment-geospatial groundingdino-py segment-anything-fast -c pytorch -c nvidia -c conda-forge
```
4. Export the requirements.txt  and move the file into the /shared folder.

```bash
conda list --export > environment-name-requirements.txt
```

The above steps should be done by the TAs and instructors and in this way the students can easily select the kernel without having to install the packages themselves.