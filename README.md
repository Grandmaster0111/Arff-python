# Arff-python

A Python utility that generates ARFF (Attribute-Relation File Format) files — the standard input format for the [Weka](https://www.cs.waikato.ac.nz/ml/weka/) machine learning toolkit.

## What it does

- Generates random attribute values for dataset construction
- Writes properly formatted `.arff` files with `@relation`, `@attribute`, and `@data` sections
- Useful for quickly creating test datasets for Weka experiments

## Prerequisites

- Python 3.6+

## Usage

```bash
python ark.py
```

The script writes a file called `usef.arff` in the current directory.

## ARFF Format Example

```
@relation my_dataset

@attribute age {1,2,3,4,5,6,7,8,9}
@attribute income {1,2,3,4,5,6,7,8,9}

@data
3,7
5,2
```

## Learning More

- [Weka ARFF documentation](https://www.cs.waikato.ac.nz/ml/weka/arff.html)
