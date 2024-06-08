# CPD

Python Course

## Installation

Create and activate conda environment:

```sh
conda env create -f CPD_env.yml
conda activate CPD_env
```

## Usage

Run the main script:

```sh
python src/subproject/module.py
```

## Testing

Run the tests

```sh
pytest
pytest tests/test_subproject.py
```

## Others: update, delete conda enviroment

```sh
conda info --envs
conda env update --file CPD_env.yml
conda deactivate 
conda env remove --name CPD_env 
```
