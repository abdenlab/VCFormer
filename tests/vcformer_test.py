from vcformer import (
    read_info_schema,
    read_sample_schema,
    read_vcf_as_pandas,
    read_vcf_as_polars,
)

vcf_path = "tests/fixtures/DRR259113.ref.snpeff.vcf.gz"
# index file f"{vcf_path}.tbi" is also present, but isn't required by pysam


def test_read_info_schema():
    df = read_info_schema(vcf_path)
    assert not df.empty


def test_read_sample_schema():
    df = read_sample_schema(vcf_path)
    assert not df.empty


def test_read_vcf_as_pandas():
    df = read_vcf_as_pandas(vcf_path)
    assert not df.empty


def test_read_vcf_as_polars():
    df = read_vcf_as_polars(vcf_path)
    assert not df.is_empty()
