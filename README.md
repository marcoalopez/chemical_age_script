![](https://raw.githubusercontent.com/marcoalopez/chemical_age_script/master/header.png)

This is a free and open-source script written in Python to estimate the 'chemical' age or *date*<sup>1</sup>
in monazites analyzed in electron microprobes. It uses the following equation
(Williams et al. 2007):

![](https://raw.githubusercontent.com/marcoalopez/chemical_age_script/master/fig_01.png)

that relates the age (*t*, in years) and the concentrations of *Th*, *U*, and the total radiogenic
*Pb* in parts per million. *λ*<sup>232</sup>, *λ*<sup>238</sup>, and *λ*<sup>235</sup> are the decay
constants for Th<sup>232</sup> (4.95E-11/year), U<sup>238</sup> (1.55E-10/year), and U<sup>235</sup>
(9.85E-10/year), respectively. 

The script solves the individual ages iteratively by entering age guesses with the known
concentrations of *U* and *Th* until the calculated *Pb* value matches the measured *Pb*
with an error below 0.1. It uses a bisection search algorithm<sup>2</sup> and returns the
age in million years.

*<sup>1</sup>Since indivual ages may or may not have geological significance, Williams et al. (2006)
refer to these as "dates" instead of "ages". They use term "age" for a result (a date or mean of dates) that
is interpreted to have geological significance*

*<sup>2</sup>This means that the algorithm is pretty fast. Tipically, the script gets an age in less than
15 guesses.*

## Download
https://github.com/marcoalopez/chemical_age_script/releases/tag/v1.0
https://figshare.com/articles/Chemical_age_script/2815144/1

## Getting started

The script requires [Python](https://www.python.org/) 2.7.x or 3.4.x installed in the system.
The Python Programming Language comes installed by default on OS X and Ubuntu Linux. In any event,
you can install Python from [here](http://conda.pydata.org/miniconda.html) for any operating
system.

The first step requires to open and run the script. The second and last one requires to write in the shell:

```python
>>> find_chemage(64586, 2519, 1626)
```

where the three inputs separated by commas within the parentheses are the concentrations of *Th*, *U*
and *Pb*, respectively. Press the Enter key and that's it. See an example below.

![](https://raw.githubusercontent.com/marcoalopez/chemical_age_script/master/fig_02.png)
*At left, running the script in the IDLE (the default Python's integrated development environment).
At right, the Python shell window showing the results (in blue) after calling the* ```find_chemage()```
*Python function (in black)*

**A more detailed tutorial explaining how to use the script with tabular-like data will be released soon**

## References
Williams, M.L., Jercinovic, M.J., Hetherington, C.J., 2007. Microprobe Monazite Geochronology: Understanding Geologic Processes
by Integrating Composition and Chronology. *Annu. Rev. Earth Planet. Sci.* **35**, 137–175.
doi:[10.1146/annurev.earth.35.031306.140228](http://dx.doi.org/10.1146/annurev.earth.35.031306.140228)

Williams, M.L., Jercinovic, M.J., Goncalves, P., Mahan, K., 2006. Format and philosophy for collecting, compiling, and reporting
microprobe monazite ages. *Chem. Geol.* **225**, 1–15. doi:[10.1016/j.chemgeo.2005.07.024](http://dx.doi.org/10.1016/j.chemgeo.2005.07.024)

## License
Chemical age script is a free script available under the [Apache License, Version 2.0 (the "License")](http://www.apache.org/licenses/LICENSE-2.0)
