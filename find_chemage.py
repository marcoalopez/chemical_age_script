# ============================================================================ #
#                                                                              #
#    Chemical age Script                                                       #
#    A Python script for estimating the age of monazites analyzed in           #
#    electron microprobes                                                      #
#                                                                              #
#    Copyright (c) 2016-present   Marco A. Lopez-Sanchez                       #
#                                                                              #
#    Licensed under the Apache License, Version 2.0 (the "License");           #
#    you may not use this file except in compliance with the License.          #
#    You may obtain a copy of the License at                                   #
#                                                                              #
#        http://www.apache.org/licenses/LICENSE-2.0                            #
#                                                                              #
#    Unless required by applicable law or agreed to in writing, software       #
#    distributed under the License is distributed on an "AS IS" BASIS,         #
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  #
#    See the License for the specific language governing permissions and       #
#    limitations under the License.                                            #
#                                                                              #
#    Version: 1.1.1                                                            #
#    For details see: https://github.com/marcoalopez/chemical_age_script       #
#                                                                              #
#    Requirements:                                                             #
#        Python version 2.7.x or 3.4.x or higher                               #
#        Numpy version 1.5 or higher                                           #
#        Matplotlib version 1.4.2 or higher                                    #
#        Scipy version 0.13 or higher                                          #
#                                                                              #
# ============================================================================ #

from __future__ import division, print_function  # avoid python 2.x - 3.x compatibility issues
from math import exp, log
import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.style.use('ggplot')  # set plot style


def find_chemage(Th, U, Pb, r=1, p=True):
    """Find the 'chemical' age of a monazite by applying iteratively the equation
    that relates the age and the concentrations of Th and U with the total radiogenic
    Pb. It uses a bisection search approach to estimate the age and assume that the
    age is within the 0-5000 Ma interval. It returns the age in million years.

    INPUTS:
    Th: the concentration of Th in parts per million
    U: the concentration of U in parts per million
    Pb: the concentration of Pb in parts per million
    r: number of digits after the decimal point. It is set to 1 by default.
    """

    age_min = 0.0
    age_max = float(5000e6)
    num_guesses = 0
    t = (age_max + age_min) / 2.0
    Pb_estimate = 0.0  # Initialize object

    while abs(Pb - Pb_estimate) >= 0.1:
        #print('age_min =', round(age_min/1e6, 2), 'age_max =', round(age_max/1e6, 2))

        if num_guesses >= 100:
            print('Something has gone wrong, check the inputs!')
            return None

        Pb_estimate = age_equation(t, Th, U)
        #print('guess =', round(t/1e6, 2), '  -  ', 'Pb_estimate', round(Pb_estimate, 1))

        if Pb_estimate < Pb:
            age_min = t
        else:
            age_max = t

        t = (age_max + age_min) / 2.0
        num_guesses += 1

    if p is True:
        print(' ')
        print('age =', round(t / 1e6, r), 'Ma (after', num_guesses, 'guesses)')
    return round(t / 1e6, r)


def find_chemage_array(Th, U, Pb, r=1):
    """Do the same as the function find_chemage but for arrays instead of
    individual Th, U and Pb values. It returns a numpy array with the ages.
    The Th, U and Pb arrays have to be of the same lenght.
    """

    ages = []  # Initialize Python list

    for i in range(len(Th)):
        age = find_chemage(Th[i], U[i], Pb[i], r, False)
        ages.append(age)

    return np.array(ages)


def CHIME(Th, U, Pb):
    """Find the 'chemical' age of a set of cogenetic monazites or a single monazite
    by applying the CHIME method of Suzuki and Adachi 1991. This method is only
    useful when monazites are Th-rich and show a range of Th contents instead of
    similar values. The method assumes that there are no initial Pb or Pb-loss in
    the monazites.

    INPUTS:
    Th: an array with the concentration of Th in parts per million
    U: an array with the concentration of U in parts per million
    Pb: an array with the concentration of Pb in parts per million
    diff: the precision of the estimate by the CHIME method.
    """

    Th_equiv_or = []  # Initialize Python list
    num_guesses = 1

    # Calculate ages
    chem_ages = find_chemage_array(Th, U, Pb)

    # Calculate the equivalent ThO2 required assuming no UO2 in the system
    for i in range(len(chem_ages)):
        x = recalc_Th(Pb[i], chem_ages[i])
        Th_equiv_or.append(x)

    # Determine the least square fit to the data PbO vs ThO2 and the age
    slope_or, intercept_or, r_value_or, p_value_or, std_err_or = linregress(Th_equiv_or, Pb)
    first_age = (1 / 4.95e-11) * log(1 + slope_or) * (232. / 207.2)
    #print('first_age =', round(first_age/1e6, 1))

    if intercept_or == 0.0:
        print('Slope =', slope_or)
        print('Intercept =', intercept_or)
        print('Age =', round(first_age / 1e6, 1))
        print('std (2-sigma) =', 2 * std_err_or)
        return plot_CHIME(Th_equiv_or, Pb, slope_or, intercept_or, first_age)

    # Approximate a solution iteratively if required
    while True:
        if num_guesses > 50:
            print('Too much guesses, something is wrong!')
            return None

        Th_equiv = []
        for i in range(len(Pb)):
            x = recalc_Th(Pb[i], first_age / 1e6)
            Th_equiv.append(x)
        slope, intercept, r_value, p_value, std_err = linregress(Th_equiv, Pb)
        current_age = (1 / 4.95e-11) * log(1 + slope) * (232. / 207.2)
        print('current_age =', round(current_age / 1e6, 1))
        print('intercept =', intercept)

        num_guesses += 1

        if intercept == 0.0:
            print('')
            print('Slope =', slope)
            print('Intercept =', intercept)
            print('Age =', round(current_age / 1e6, 1))
            #print('std (2-sigma) =', 2*std_err)
            print('numguesses =', num_guesses)
            return plot_CHIME(Th_equiv_or, Pb, slope, intercept, current_age)

        first_age = current_age


def age_equation(t, Th, U):
    """Applies the equation that relates the age with the Th, U and Pb concentrations.
    Specifically, it returns the radiogenic Pb estimated in ppms taking into
    account the initial quantities of Th232, U238 and U235.The decay constants
    considered are:

    Th232 = 4.95e-11/year
    U238 = 1.55e-10/year
    U235 = 9.85e-10/year

    INPUTS:

    t: the age in years
    Th: the concentration of Th in parts per million
    U: the concentration of U in parts per million
    """
    return (Th / 232. * (exp(4.95e-11 * t) - 1) * 208) + (U / 238. * 0.9928 * (exp(1.55e-10 * t) - 1) * 206) + (U / 235. * 0.0072 * (exp(9.85e-10 * t) - 1) * 207)


def recalc_Th(Pb, age):
    """Calculates the equivalent amount of ThO2 that would be required to produce the
    measured amount of PbO if there was no UO2 in the monazite.

    INPUTS:
    Pb: the concentration of Pb in parts per million
    age: the age in million years
    """

    return (232. / 208.) * Pb / (exp(4.95e-11 * (age * 1e6)) - 1)


def plot_CHIME(Th_equiv, Pb, slope, intercept, current_age):
    """Generate a plot for the CHIME method"""

    plt.figure(tight_layout=True)
    plt.gcf().subplots_adjust(bottom=0.15)  # this is to prevent x-label cut off

    plt.plot(Th_equiv, Pb, 'o', color='#7570b3')
    plt.plot([0, max(Th_equiv)], [intercept, slope * max(Th_equiv) + intercept], color='#525252', linewidth=2)
    plt.title('CHIME age', color='#525252', fontsize=16, y=1.02)
    plt.xlabel('Th* (ppm)', fontsize=15)
    plt.ylabel('Pb (ppm)', fontsize=15)
#    plt.annotate('Slope =', slope, '\n', 'Intercept =', intercept, '\n', 'Age =', current_age, 'Ma', '\n', '2-sigma', horizontalalignment='left', verticalalignment='upper')

    return plt.show()
