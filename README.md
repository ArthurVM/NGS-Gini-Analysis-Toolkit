# Read Distribution Toolkit

This is a toolkit for analysing the coverage and distribution of reads over a genome sequence assembly.

The toolkit focusses on calculating coverage inequality statistics from read coverage files, using the Gini coefficient.

## The Gini-coefficient

The Gini coefficient is a metric used to measure the inequality within a dataset. 
It is commonly used in economics to measure the distribution of income within a population, where it is represented by a value 
between 0 and 1, with 0 representing perfectly even distribution, and higher values representing higher inequality of distribution. 
This toolkit applies this coefficient to measure inequality of depth of coverage across a genome.

The Gini coefficient is calculated as:

<a href="https://www.codecogs.com/eqnedit.php?latex=G&space;=&space;A/(A&plus;B)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?G&space;=&space;A/(A&plus;B)" title="G = A/(A+B)" /></a>

where 
<a href="https://www.codecogs.com/eqnedit.php?latex=A" target="_blank"><img src="https://latex.codecogs.com/gif.latex?A" title="A" /></a>
is the area under the line of equality, and 
<a href="https://www.codecogs.com/eqnedit.php?latex=B" target="_blank"><img src="https://latex.codecogs.com/gif.latex?B" title="B" /></a>
the area under the Lorenz curve, on the graph of data distribution. Further reading can be found in the references section.

The Gini-coefficient is mathematically equivillent to the sum of the absolute difference of all pairs of the population
(where a pair consists of positions on the Lorenz curve and the line of equality given any x) divided by the mean.
In the context of read coverage analysis, if 
<a href="https://www.codecogs.com/eqnedit.php?latex=x_i" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x_i" title="x_i" /></a>
is the coverage at position 
<a href="https://www.codecogs.com/eqnedit.php?latex=i" target="_blank"><img src="https://latex.codecogs.com/gif.latex?i" title="i" /></a>
within the a genome of size 
<a href="https://www.codecogs.com/eqnedit.php?latex=n" target="_blank"><img src="https://latex.codecogs.com/gif.latex?n" title="n" /></a>
then the mean absolute difference, and therefore Gini coefficient is calculated as:

<a href="https://www.codecogs.com/eqnedit.php?latex=
G&space;=&space;\dfrac{\sum\limits_{i=1}^{n}\sum\limits_{j=1}^{n}|x_i&space;-&space;x_j|}{2n\sum\limits_{i=1}^{n}x_i}"
target="_blank"><img src="https://latex.codecogs.com/gif.latex?G&space;=&space;\dfrac{\sum\limits_{i=1}^{n}\sum\limits_{j=1}^{n}|x_i&space;-&space;x_j|}{2n\sum\limits_{i=1}^{n}x_i}" title="G = \dfrac{\sum\limits_{i=1}^{n}\sum\limits_{j=1}^{n}|x_i - x_j|}{2n\sum\limits_{i=1}^{n}x_i}" /></a>

## Gini-Granularity curves

Gini-Granularity curves are presented as a manner of resolving two problems with the Gini coefficient:

- Two genomes with identical ordered coverage arrays will produce identical Lorentz curves, and therefore an identical Gini. 
This does not take into account the distribution of depth of coverage across the genome.
- The Gini coefficient is known to be confounded by data granularity.

Gini granularity curves are presented here as a more complete characterisation of the distributions of reads across a genome.

To generate a GG-curve, the Gini coefficient is calculated at a range of data granularities. This is achieved by calculating
across windows, where the mean coverage for each window is taken instead of the coverage at every position within the genome.
This has the effect of 'blurring' the coverage across the genome and making the data less granular.

Using this range of Gini values, a curve can be generated. The area under this curve, when normalised, can be used
to indicate the distribution of reads mapping across the genome, where higher values indicate greater levels of read aggregation.

**N.B.** This result must be analysed in context with the Gini value at maximum data granularity (window size 1).
