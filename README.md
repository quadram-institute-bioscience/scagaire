Todo:
Script to produce genes vs species all in 1 table
documentation

Dependancies
--
ncbi genome downloader
mash - for genera
abricate

# identifying species
ncbi-genome-download  -l all --parallel 8 -R reference -F fasta --human-readable bacteria 
gets 120 very high quality genomes


# Inputs supported
* [Abricate](https://github.com/tseemann/abricate)
* [Staramr](https://github.com/phac-nml/staramr) (resfinder.tsv)
* [RGI](https://xxx) CARD


# Feedback/Issues
Please report any issues or to provide feedback please go to the [issues page](https://github.com/quadram-institute-bioscience/scagaire/issues). If you make improvements to the software, add databases or extend profiles, please send us the changes though a [pull request](https://github.com/quadram-institute-bioscience/scagaire/pulls) so that the whole community may benefit from your work.

# Etymology
[Scagaire](https://www.teanglann.ie/en/eid/Scagaire) (scag-aire) is the word for filter/refiner in Irish (Gaeilge). 
