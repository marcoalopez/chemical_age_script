# Chemical age script

This is a simple script written in Python to find the 'chemical' age in monazites analized in
electron microprobes. It uses the following equation (Williams et al. 2007):

![](https://raw.githubusercontent.com/marcoalopez/chemical_age_script/master/fig_01.png)

that relates the age (*t*, in years) and the concentrations of Th, U, and the total radiogenic
Pb in parts per million. λ232, λ238, and λ235 are decay constants for Th232 (4.95E-11/year),
U238 (1.55E-10/year), and U235 (9.85E-10/year), respectively. 

The script solves the individual ages iteratively by entering age guesses with the known
concentrations of U and Th until the calculated Pb value matches the measured Pb (with an
error below 0.1). It uses a bisection search approach (meaning: it is pretty fast) and returns
the age in million years.

# Getting started: how to use the script

First, the scripts requires Python 2.7.x or 3.4.x installed in the system. The Python
Programming Language comes installed by default on OS X and Ubuntu. In windows, you can
install Python from [here](https://www.python.org/) or [here](http://conda.pydata.org/miniconda.html).

Then, you need to open the script and run it. Finally write in the shell:

```python
>>> find_chemage(64586, 2519, 1626)
```

where the three inputs within the parentheses are the concentrations of Th, U and Pb, respectively.
Press the Enter key and that's it.
