# VCFormer

VCF data is typically nested and difficult to work with. To facilitate analysis of VCF data, this library reads VCF files into Pandas or Polars DataFrames and extracts nested fields to the top level, with a focus on the INFO and sample genotype fields.

Note: This project builds off our [previous work](https://github.com/NCBI-Codeathons/vcf-4-population-genomics-team-abdennur) at the VCF Files for Population Genomics: Scaling to Millions of Samples codeathon co-hosted by NCBI and NIAID.


## Installation
In your preferred Python (virtual) environment, run the following from the root of the cloned project: `pip install -e .`


## Usage
```python
import vcformer as vcf

# Read info schema
vcf.read_info_schema("<PATH TO VCF>")

# Read sample schema
vcf.read_sample_schema("<PATH TO VCF>")

# Pandas DataFrame
vcf.read_vcf_as_pandas("<PATH TO VCF>")

# Polars DataFrame
vcf.read_vcf_as_polars("<PATH TO VCF>")
```

### Read Info Schema
::: vcformer.read_info_schema

### Read Sample Schema
::: vcformer.read_sample_schema

### Read VCF as Pandas DataFrame
::: vcformer.read_vcf_as_pandas

### Read VCF as Polars DataFrame
::: vcformer.read_vcf_as_polars
