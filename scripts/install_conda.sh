#!/bin/bash
# Ubuntu, run script - 'bash install_conda.sh'

# Define the Anaconda version
ANACONDA_VERSION="Anaconda3-2024.02-1-Linux-x86_64"

# Check if conda exists and uninstall if it does
if command -v conda &> /dev/null; then
    echo "Conda detected. Uninstalling..."
    conda install anaconda-clean -y
    anaconda-clean --yes
    rm -rf ~/anaconda3
    rm -rf ~/.condarc ~/.conda ~/.continuum

    # Remove Anaconda-related entries from .bashrc
    sed -i '/export CONDA_HOME="\$HOME\/anaconda3"/d' ~/.bashrc
    sed -i '/export PATH="\$CONDA_HOME\/bin:\$PATH"/d' ~/.bashrc
    echo "Conda uninstalled."
fi

sudo apt install curl -y

# Install anaconda (3 GB), Miniconda less 
cd /tmp
curl https://repo.anaconda.com/archive/${ANACONDA_VERSION}.sh --output anaconda.sh
sha256sum anaconda.sh
bash anaconda.sh

# Update bashrc
echo 'export CONDA_HOME="$HOME/anaconda3"' >> ~/.bashrc
echo 'export PATH="$CONDA_HOME/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

# Verify installation
conda info
conda --version

# Anaconda Update 
conda update conda -y
conda install anaconda -y
conda update anaconda -y

# Configure conda to not auto-activate base environment
conda config --set auto_activate_base false

# Check base conda env
conda init
conda deactivate
