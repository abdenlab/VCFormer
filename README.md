# VCFormer

VCF data is typically nested and difficult to work with. To facilitate analysis of VCF data, this library reads VCF files into Pandas or Polars DataFrames and extracts nested fields to the top level, with a focus on the INFO and sample genotype fields.

Note: This project builds off our [previous work](https://github.com/NCBI-Codeathons/vcf-4-population-genomics-team-abdennur) at the VCF Files for Population Genomics: Scaling to Millions of Samples codeathon co-hosted by NCBI and NIAID.


## Installation
In your preferred Python (virtual) environment, run the following from the root of the cloned project:
```sh
pip install -e .
```

You may also install from GitHub:
```sh
pip install git+https://github.com/abdenlab/VCFormer.git
```

We plan to publish to PyPI soon.


## Contribution
Install dev dependencies:
```sh
pip install '.[dev]'
```

Install pre-commit:
```sh
pip install pre-commit
pre-commit install
```

## Usage
```python
import vcformer as vcf

# Read info schema as pandas dataframe
info_schema = vcf.read_info_schema("<PATH TO VCF>")

# Read sample schema as pandas dataframe
sample_schema = vcf.read_sample_schema("<PATH TO VCF>")

# Pandas DataFrame
df = vcf.read_vcf_as_pandas("<PATH TO VCF>", "chr1:10M-20M", info_fields=["AC", "AF"], sample_fields=["GT"], samples=["SRR123456", "SRR98765"])

# Polars DataFrame
df = vcf.read_vcf_as_polars("<PATH TO VCF>", ...)
```

## Acknowledgements

Special thanks to team members from the NCBI VCF Codeathon:

* Lei Ma @microlei (USDA)
* Mehmet Kuscuoglu @kscgl (JCVI)
* David Adeleke (North Dakota State University)
* Clark Cucinell (University of Virginia)
* Se-Ran Jun (University of Arkansas for Medical Sciences)
