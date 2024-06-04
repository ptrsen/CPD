# CPD
Python Course 

## Installation
Create and activate the Conda environment:

```sh
conda env create -f CPD_env.yml
conda activate CPD_env
```

## Usage
Run the main script:

```sh
python src/subproject/main.py
```

## Testing
Run the tests

```sh
pytest tests/test_subproject.py
```


## Update, delete conda env

```sh
conda info --envs
conda env update --file CPD_env.yml
conda deactivate 
conda env remove --name CPD_env 
```