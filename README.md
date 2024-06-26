# CSE185-Final-Project
UCSD CSE 185 Spring 2024 Final Project Elliott Ou, Audria Montalvo, and Leny Lei

## Note to CSE185 peer reviewers
While installation works, the command may not run correctly for some and we are working on fixing the main. In the meantime if the program doesn't run, please copy and paste the code from mygwas_tools.py in the mygwas folder into a datahub notebook and upload the test files in the testfiles directory to the same directory as the notebook. Run gwas(geno file, pheno file) to run gwas and get the output files in the directory. 

# MyGWAS

MyGWAS is a command line tool designed to perform Genome-Wide Association Studies (GWAS). It processes genotype and phenotype data, conducts linear regression to obtain statistical associations, and generates visualizations such as Manhattan plots and QQ plots.

## Features
- Read and preprocess genotype data from VCF files.
- Read phenotype data from text files.
- Conduct linear regression to obtain beta coefficients and p-values.
- Generate Manhattan plots and QQ plots for visualizing GWAS results.

## Requirements
- Python 3.x
- pandas
- numpy
- matplotlib
- qqman (or equivalent package for GWAS plotting)

## Installation
Clone the directory into your own terminal. 
```
git clone https://github.com/ou-elot/CSE185-Final-Project
```
Now change directory into the project folder:

```
cd CSE185-Final-Project
```
Download the requirements.
```
pip install -r requirements.txt
```

Run the following commands in the terminal before installation to ensure installation is successful.
```
export PATH=$PATH:$HOME/.local/bin
export PYTHONPATH=$HOME/lib/python3.9/site-packages
```

Both installation commands below need to be ran:
```
python setup.py install --prefix=$HOME
pip install . #do not forget the period!
```

You should now be able to run the command. Type the following to check:
```
mygwas --help
```
## Usage
The mygwas tool is a command line tool that takes in a vcf file containing genotypes and a csv file containing phenotypes, and ouputs files to the current directory. In the current version, the program only takes files as input if they are in the current working directory.
```
usage: mygwas --geno [genotype file] --pheno [phenotype file] 
example: mygwas --geno geno.vcf --pheno pheno.phen
```
Output files will be named the following:
```
p-values and beta values: linreg.txt
qq-plot: qq.png
manhattan plot: manhattan.png
```
