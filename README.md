# CPD
Python3 

## Installation
Create and activate the Conda environment:

```sh
conda env create -f CPD_env.yml
conda activate CPD_env
```

## Usage
Run the main script:

```sh
python src/subproject1/main.py
```

## Testing
Run the tests

```sh
pytest tests/test_subproject1.py
```


## Update, delete conda env

```sh
conda env update --file CPD_env.yml
conda deactivate CPD_env
conda info --envs
conda env remove --name CPD_env --all
```