# Scagaire
[![Build Status](https://travis-ci.org/quadram-institute-bioscience/scagaire.svg?branch=master)](https://travis-ci.org/quadram-institute-bioscience/scagaire)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-brightgreen.svg)](https://github.com/quadram-institute-bioscience/scagaire/blob/master/LICENSE)
[![codecov](https://codecov.io/gh/andrewjpage/scagaire/branch/master/graph/badge.svg)](https://codecov.io/gh/andrewjpage/scagaire)
[![Docker Pulls](https://img.shields.io/docker/pulls/andrewjpage/scagaire.svg)](https://hub.docker.com/r/andrewjpage/scagaire)  

# Contents
  * [Introduction](#introduction)
  * [Installation](#installation)
	* [Conda](#conda)
    * [Docker](#docker)
  * [Usage](#usage)
  * [License](#license)
  * [Feedback/Issues](#feedbackissues)
  * [Etymology](#etymology)
  * [Citation](#citation)


## Introduction
Scagaire allows you to take in AMR gene predictions from a metagenomic sample and filter them by pathogen.

# Installation
If you just want to quickly try out the software please try a Docker continer. This software is designed to run on Linux and OSX. It is not tested on Windows.

## Conda
[![Anaconda-Server Badge](https://anaconda.org/bioconda/scagaire/badges/latest_release_date.svg)](https://anaconda.org/bioconda/scagaire)
[![Anaconda-Server Badge](https://anaconda.org/bioconda/scagaire/badges/platforms.svg)](https://anaconda.org/bioconda/scagaire)
[![Anaconda-Server Badge](https://anaconda.org/bioconda/scagaire/badges/downloads.svg)](https://anaconda.org/bioconda/scagaire)

To install Scagaire, first install [conda with Python3](https://conda.io/en/latest/miniconda.html) then run:

```
conda install -c conda-forge -c bioconda mash abricate ncbi-genome-download
pip install git+git://github.com/quadram-institute-bioscience/scagaire.git
```

Actually if you just want to run scagaire and have no interest in building databases, then you dont need mash, abricate, or ncbi-genome-download.

## Docker
Install [Docker](https://www.docker.com/).  There is a docker container which gets automatically built from the latest version of Scagaire. To install it:

```
docker pull andrewjpage/scagaire
```

To use it you would use a command such as this (substituting in your filename/directories), using the example file in this repository:
```
docker run --rm -it -v /path/to/example_data:/example_data andrewjpage/scagaire scagaire xxxxx
```

# Usage

## Quick start example
Given a metagenomic assembly in FASTA format. Predict resistance genes with Abricate:
```
abricate my_assembly.fa > amr_results
```
Look up the species supported by scagaire:
```
scagaire_species
```
Filter your AMR results by a species:
```
scagaire "Klebsiella pneumoniae" amr_results 
```


## Input
The following inputs are supported
* [Abricate](https://github.com/tseemann/abricate)
* [Staramr](https://github.com/phac-nml/staramr) (the file resfinder.tsv)
* [RGI-CARD](https://github.com/arpcard/rgi)

## Output
The output is a filtered list of what was put in (in the same format).

## scagaire
This is the main script which takes in a set of AMR gene predictions and a species and outputs a filtered list specific to that species.

```
usage: scagaire [options] species amr_results

Filter AMR results by species

positional arguments:
  species               Species name, use scagaire_species to see all
                        available
  input_file            Input file of AMR results from Abricate etc...

optional arguments:
  -h, --help            show this help message and exit
  --database DATABASE, -d DATABASE
                        Database of species to genes. Defaults to bundled
                        (default: None)
  --results_type {abricate,rgi,staramr}, -t {abricate,rgi,staramr}
                        Format of input results. Defaults to automatically
                        detecting format. (default: None)
  --output_file OUTPUT_FILE, -o OUTPUT_FILE
                        Output filename, defaults to STDOUT (default: None)
  --minimum_occurances MINIMUM_OCCURANCES, -m MINIMUM_OCCURANCES
                        Minimum number of occurances of a gene in the database
                        to use (default: 0)
  --debug               Turn on debugging (default: False)
  --verbose, -v         Turn on verbose output (default: False)
  --version             show program's version number and exit
```

__species__: This is the name of a bacterial pathogens that you wish to filter on (within quotes). For multiple species, separate them with a comma. It must exactly match a name from the scagaire_species command. All the major pathogens are bundled with the software but if your pathogen of interest is missing you can use scagaire_download to create a database for it. For some pathogens this may be the genus.

__input_file__: The AMR gene prediction results from Abricate, StarAMR, CARD etc... Ideally the NCBI or CARD database should be used. 

__database__: A database is bundled with the software and is detected automatically. It contains the gene name, species and number of assemblies that gene is predicted in the public archives. You can provide the full path to your own database if you wish, such as the output of scagaire_download. It is in tab delimited format.

__results_type__: By default the format of the input file is detected, however if this is not working correctly, you can specifiy the format yourself.

__output_file__: You can choose to output the filtered results to a file instead of STDOUT (printing to screen).

__minimum_occurances__: You can exclude genes which have rarely been observed in a species. About 25% of genes are only observed once in a species/genus.

__help__: This will print out the extended help information, including default values, then exit.

__debug__: This will keep intermediate files, and print out profiling information about how long different parts of the software take to run. Its really only useful for software development debugging, hence the name.

__verbose__: Print out enhanced information while the program is running.

__version__: Print the version of the software and exit. If the version is 'x.y.z' it probably means you haven't installed the software in a standard manner (conda/pip).

## scagaire_species
This script lists all the available species in the database. Some pathogens are missing because gene predictions are of poor quality or because resistance is rarely observed.

```
usage: scagaire_species [options]

List all available species

optional arguments:
  -h, --help     show this help message and exit
  --debug        Turn on debugging (default: False)
  --verbose, -v  Turn on verbose output (default: False)
  --version      show program's version number and exit
```

__help__: This will print out the extended help information, including default values, then exit.

__debug__: This will keep intermediate files, and print out profiling information about how long different parts of the software take to run. Its really only useful for software development debugging, hence the name.

__verbose__: Print out enhanced information while the program is running.

__version__: Print the version of the software and exit. If the version is 'x.y.z' it probably means you haven't installed the software in a standard manner (conda/pip).

### scagaire_download
This script allows you to automatically create your own database of use with scagaire for a new species. Its probably best not to change any of the parameters as you'll break it.

```
usage: scagaire_download [options] species

Given a species, download all assemblies and add AMR genes to database

positional arguments:
  species               Species name, use scagaire_species to see all
                        available

optional arguments:
  -h, --help            show this help message and exit
  --assembly_level {all,complete,chromosome,scaffold,contig}, -l {all,complete,chromosome,scaffold,contig}
                        Assembly level (default: all)
  --threads THREADS, -t THREADS
                        No. of threads (default: 1)
  --mash_database MASH_DATABASE, -m MASH_DATABASE
                        Mash database for checking assembly species
                        classification, defaults to bundled (default: None)
  --output_file OUTPUT_FILE, -o OUTPUT_FILE
                        Output filename (default: species_to_genes.tsv)
  --output_directory OUTPUT_DIRECTORY, -i OUTPUT_DIRECTORY
                        Working output directory (default: None)
  --minimum_distance MINIMUM_DISTANCE
                        Mash minimum distance threshold (default: 0.1)
  --downloads_directory DOWNLOADS_DIRECTORY
                        Use this directory of NCBI genomes instead of
                        downloading (default: None)
  --refseq_category {all,reference,representative}
                        Quality of the assemblies (default: all)
  --abricate_database ABRICATE_DATABASE
                        Abricate database (default: ncbi)
  --min_coverage MIN_COVERAGE
                        Min percentage coverage over AMR gene (default: 95)
  --min_identity MIN_IDENTITY
                        Min percentage identity over AMR gene (default: 95)
  --debug               Turn on debugging (default: False)
  --verbose, -v         Turn on verbose output (default: False)
  --version             show program's version number and exit
```

__assembly_level__: By default the script will download all available assemblies in RefSeq (draft and complete). You can choose to restrict it to a subset. For example if you wanted fully complete genomes where the chromosome is in 1 piece you would select 'complete'.

__threads__: The number of threads to use. This must not exceed the number of cores/processors available on your computer. If it does exceed it, you will get obscure errors. 

__mash_database__: By default a mash database is bundled containing about 120 high quality reference genomes for species identification. Its quite good and its manually curated. However you can provide your own database. I cant promise your database will work though, and you need to make sure your naming is ./Genus/species/xxxx.

__output_file__: Specify the output filename.

__output_directory__: This is the working directory, by default this is the name of the species. This is useful for debugging.

__minimum_distance__: Set the distance to consider a MASH match. It is between  0-1, where 0 is a perfect match, and 1 is a total mismatch. 

__downloads_directory__: If you have already downloaded the NCBI genomes using ncbi-genome-download (or you want to repeat something that failed), you can provide the download directory here.

__refseq_category__: Dont change this because you will probably make everything stop working.

__abricate_database__: You can choose the gene prediction database to use such as card, resfinder, argannot or ncbi (default). You should be careful when changing it away from the default, because the database bundled uses the ncbi names and other databases can have subtle changes.

__min_coverage__: The minimum coverage required over a gene to say its present.

__min_identity__: The minimum identity required over a gene to say its present.

__help__: This will print out the extended help information, including default values, then exit.

__debug__: This will keep intermediate files, and print out profiling information about how long different parts of the software take to run. Its really only useful for software development debugging, hence the name.

__verbose__: Print out enhanced information while the program is running.

__version__: Print the version of the software and exit. If the version is 'x.y.z' it probably means you haven't installed the software in a standard manner (conda/pip).

# Method
The public archives of NCBI and EBI contain hundreds of thousands of bacterial pathogen isolates. Most are derived from short read sequencing data and have been assembled de novo with SKEASA [ref]. We can use this genomic information to survey the AMR gene landscape in the public domain. We focus only on acquired genes causing resistance rather than point mutations. There is substantial sampling bias in the underlying datasets towards pathogens which cause more serious illness in humans, so it must be treated with a pinch of salt. We downloaded the top 14 more frequently sequenced pathogens.

Database of AMR genes found in each Species/Genus
Manual download from NCBI
The NCBI Pathogen detection browser (https://www.ncbi.nlm.nih.gov/pathogens/) contains a curated database of genome assemblies to AMR genes with a primary focus on bacterial pathogens causing foodborne illness. The AMR profiles for each Genus/Species were downloaded as spreadsheets and summarised into AMR gene occurrence frequencies.  The database used to predict the AMR genes was AMRFinderPlus (https://www.ncbi.nlm.nih.gov/pathogens/antimicrobial-resistance/AMRFinder/).

Automatic download from NCBI
As many important pathogens are missing from the NCBI pathogen detection browser, a software tool is provided to automatically constructed a database of any given species. For a given species, all genome assemblies (draft and complete) are downloaded using ncbi-genome-download [ref] (version) in FASTA format. 

The taxonomic classification is set by the researcher who uploads the original genome data and so is subject to labelling errors, thus we check the species of each assembly against a database of high quality, manually curated, reference genomes. This high quality database consists of 120 (accessed 2019-10-21) genomes, covering the most important pathogens, and is downloaded by ncbi-genome-download (version). The genomes used to create a combined mash [ref](version xxx) sketch with default parameters.  Each assembly to be checked is compared to the high quality database, with the species with the lowest distance (closest match) compared (maximum distance <= 0.1). If there is a mismatch, the assembly is removed from further consideration. 

Abricate [ref](version) is used to predict AMR genes for each assembly which captures both plasmids and the chromosome.  A gene is said to be present if the coverage and identity are greater than or equal to 95% (user configurable) to allow for variation, but in practice virtually all genes are near 100% identical.  These AMR genes are summerised and their frequency of occurrence counted. If a gene appears more than once within an assembly, it is only counted once. This summary is outputted to a database of the species, gene and number of occurrences.


Given a set of AMR gene predictions from tools such as StarAMR, Abricate or RGI (CARD), and a pathogen (species/genus) of interest, scagaire will filter the list of predictions to include only those which have been observed in the same species/genus.  Rarely observed genes can additionally be filtered (default is any gene observed at least once). This removes background resistance genes of bacteria which are not of interest.   

# License
Scagaire is free software, licensed under [GPLv3](https://raw.githubusercontent.com/quadram-institute-bioscience/scagaire/master/VERSION/LICENSE).


# Feedback/Issues
Please report any issues or to provide feedback please go to the [issues page](https://github.com/quadram-institute-bioscience/scagaire/issues). If you make improvements to the software, add databases or extend profiles, please send us the changes though a [pull request](https://github.com/quadram-institute-bioscience/scagaire/pulls) so that the whole community may benefit from your work.

# Etymology
[Scagaire](https://www.teanglann.ie/en/eid/Scagaire) (scag-aire) is the word for filter/refiner in Irish (Gaeilge). 

# Citation
Scagaire,
Andrew J Page, Justin O'Grady
https://github.com/quadram-institute-bioscience/scagaire
