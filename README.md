﻿![](https://raw.githubusercontent.com/marcoalopez/chemical_age_script/master/header.png)

This is a free and open-source script written in Python to estimate the 'chemical' age or *date*<sup>1</sup> in monazites analyzed in electron microprobes.

For individual measures, it uses the following equation (Williams et al. 2007):

![](https://raw.githubusercontent.com/marcoalopez/chemical_age_script/master/fig_01.png)

that relates the age (*t*, in years) and the concentrations of *Th*, *U*, and the total radiogenic *Pb* in parts per million. *λ*<sup>232</sup>, *λ*<sup>238</sup>, and *λ*<sup>235</sup> are the decay constants for Th<sup>232</sup> (4.95E-11/year), U<sup>238</sup> (1.55E-10/year), and U<sup>235</sup> (9.85E-10/year), respectively.

The script solves the ages iteratively by entering age guesses with the known concentrations of *U* and *Th* until the calculated *Pb* value matches the measured *Pb* with an error below 0.1. It uses a bisection search algorithm and returns the age in million years.

Since version 1.1, it also adds an experimental implementation of the CHIME method (Suzuki and Adachi 1991)<sup>2</sup>.

*<sup>1</sup>Since individual ages may or may not have geological significance, Williams et al. (2006) refer to these as "dates" instead of "ages". They use term "age" for a result (a date or mean of dates) that is interpreted to have geological significance*

*<sup>2</sup>This method is only useful when monazites are cogenetic, Th-rich, and show a range of Th contents instead of similar values.*

## Download
https://github.com/marcoalopez/chemical_age_script/releases/  
https://figshare.com/articles/Chemical_age_script/2815144

## Getting started

The script requires [Python](https://www.python.org/) 2.7.x/3.x. Also, from version 1.1 onwards it requires Numpy, Scipy, and Matplotlib scientific packages. See an example [here](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/Requirements.md) for installing Python in different operating systems.

Once you open and run the script (Fig 1) and for estimating individual ages you need to write in the shell/console :

```python
>>> find_chemage(64586, 2519, 1626)
```

where the three inputs separated by commas within the parentheses are the concentrations of *Th*, *U* and *Pb*, respectively. Press the Enter key and that's it. See an example below.

![](https://raw.githubusercontent.com/marcoalopez/chemical_age_script/master/fig_02.png)
*At left, running the script in the IDLE (the default Python's integrated development environment).
At right, the Python shell window showing the results (in blue) after calling the* ```find_chemage()```
*Python function (in black)*

To estimate ages in a data set (i.e. arrays) use:

```python
>>> find_chemage_array(Th, U, Pb)
```
where Th, U and Pb are the arrays of data (Python list or Numpy arrays) that contains the values of Th, U and Pb in ppm.

Finally, to use the CHIME method use:

```python
>>> CHIME(Th, U, Pb)
```
where Th, U and Pb are the values of Th, U and Pb in ppm in the form of Python lists or Numpy arrays. This method is currently in alpha version and returns the age, the slope of the isochron and a plot with the isochron and the data, but no the error in the estimation.

**A detailed tutorial explaining how to use the script with tabular-like data will be released in the future**

## References
Suzuki, K. and Adachi, M., 1991. Precambrian provenance and Silurian metamorphism of the Tsubonosawa paragneiss in the South Kitakami terrane, Northeast Japan, revealed by the chemical Th-U-total Pb isochron ages of monazite, zircon and xenotime. *Geochem. J.* **25**, 357-376. doi:http://doi.org/10.2343/geochemj.25.357

Williams, M.L., Jercinovic, M.J., Hetherington, C.J., 2007. Microprobe Monazite Geochronology: Understanding Geologic Processes by Integrating Composition and Chronology. *Annu. Rev. Earth Planet. Sci.* **35**, 137–175. doi:[10.1146/annurev.earth.35.031306.140228](http://dx.doi.org/10.1146/annurev.earth.35.031306.140228)

Williams, M.L., Jercinovic, M.J., Goncalves, P., Mahan, K., 2006. Format and philosophy for collecting, compiling, and reporting microprobe monazite ages. *Chem. Geol.* **225**, 1–15. doi:[10.1016/j.chemgeo.2005.07.024](http://dx.doi.org/10.1016/j.chemgeo.2005.07.024)

## License
Chemical age script is a free script available under the [Apache License, Version 2.0 (the "License")](http://www.apache.org/licenses/LICENSE-2.0)
