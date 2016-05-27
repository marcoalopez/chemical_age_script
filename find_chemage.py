#==============================================================================#
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
#    Version: 1.0.2                                                            #
#    For details see: https://github.com/marcoalopez/chemical_age_script       #
#                                                                              #
#    Requirements:                                                             #
#        Python version 2.7.x or 3.4.x or higher                               #
#                                                                              #
#==============================================================================#

from __future__ import division, print_function # avoid python 2.x - 3.x compatibility issues
from math import exp

def age_equation(t, Th, U):
    """Applies the equation that relates the age with the Th, U and Pb concentrations.
    Specifically, it returns the radiogenic Pb estimated in ppms for taking into
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
    return (Th/232. * (exp(4.95e-11*t) - 1) * 208) + (U/238. * 0.9928 * (exp(1.55e-10*t) - 1) * 206) + (U/235. * 0.0072 * (exp(9.85e-10*t) - 1) * 207)

def find_chemage(Th, U, Pb, r=1):
    """Find the 'chemical' age of a monazite by applying iteratively the equation
    that relates the age and the concentrations of Th and U with the total radiogenic
    Pb. It uses a bisection search approach to estimate the age. It returns the age
    in million years.
    
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
    Pb_estimate = 0.0 # Initialize variable
    
    while abs(Pb - Pb_estimate) >= 0.1:
        #print('age_min =', round(age_min/1e6, 2), 'age_max =', round(age_max/1e6, 2))
                
        if num_guesses >= 100:
            print('Something has gone wrong, check the inputs!')
            return None
        
        Pb_estimate = age_equation(t, Th, U) # make a guess
        #print('guess =', round(t/1e6, 2), '  -  ', 'Pb_estimate', round(Pb_estimate, 1))
        
        if Pb_estimate < Pb:
            age_min = t
        else:
            age_max = t
        
        t = (age_max + age_min) / 2.0
        num_guesses += 1
    
    print(' ')
    print('age =', round(t/1e6, r), 'Ma (after', num_guesses, 'guesses)')
    return round(t/1e6, r)
