import io
import os
import pandas as pd
import numpy as np
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt

def genotype(genotype_path):
    geno= pd.read_csv(genotype_path, comment="#", sep="\t", header = None)
    y=-1
    for index, row in geno.iterrows():
        y=y+1
        for i in range (9, len(geno.axes[1]) ):
            gt = row[i]
            alleles = gt.split("|") 
            alleles = [int(item) for item in alleles]
            final_genotype = sum(alleles)
            geno.at[y, i] = final_genotype 
    return geno


def getPhenotype(phenotype_path):
    phen = pd.read_csv(phenotype_path, sep='\t', header =None)
    return phen

def Linreg(gts, pts):
    """
    Perform a GWAS between the genotypes and phenotypes
    
    Parameters
    ----------
    gts : np.array of floats
        Genotypes (scaled to have mean 0, variance 1)
        of each person
    pts : np.array och personf floats
        Simulated phenotype value of each person
        
    Returns
    -------
    beta : float
        Estimated effect size
    pval : float
        P-value
    """
    X = sm.add_constant(gts)
    model = sm.OLS(pts, X)
    results = model.fit()
    beta = results.params[1]
    pval = results.pvalues[1]
    return beta, pval

def gwas (geno_file, pheno_file):
    a = []
    genoCopy = genotype(geno_file)
    geno = genotype(geno_file)
    geno.drop(geno.columns[[0,1,2,3,4,5,6,7,8]], axis=1, inplace=True)
    pheno = getPhenotype(pheno_file)
    pts = pheno[2]
    for index, row in geno.iterrows():
        gts = geno.iloc[index].to_numpy()
        gts = gts.astype(np.float)
        beta, pval = Linreg(gts, pts);
        b = [genoCopy[2][index], pval, beta]
        a.append(b)
    data = pd.DataFrame(a, columns = ['Gene Name', 'p-value', 'Beta value'])
    data.to_csv('beta_pval.txt', sep='\t', index=False)
    return data
