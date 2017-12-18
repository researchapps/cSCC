#!/usr/bin/env python
import math

## This python snippet was not tested or used for the application, but served
# as a "psuedo code" for @vsoch to write the JavaScript logic from the docs 
# included with this folder. If you do use this and write out a more clean
# script, please issue a pull request (PR) to the repository so others can
# benefit. Thank you!   @vsoch

## Input data

# Please indicate the most appropriate response:
# My gender is: 
gender = ['female', 'male']                

# My current age is: 
age_years = 60                  # age in years

# My tendency to sunburn is: 
sunburn_tendency = 0      # 0=low, 1=moderate, 2=high

# I have been diagnosed in the past with an invasive squamous cell skin cancer:
past_rx_invasive = 0               # 0=unchecked, 1=checked

### IF FALSE

# I have been diagnosed in the past with a non-invasive (also called in-situ) squamous cell skin cancer: 
past_rx_insitu = 0        # 0=unchecked, 1=checked

# I have been diagnosed in the past with an actinic keratosis: 
past_rx_keratosis = 0     # 0=unchecked, 1=checked

# I have been typed for the 16 genetic variants associated with increased risk of squamous cell skin cancer (option to see a list of risk alleles for these sixteen variants): 
genotyped = 0   # 0=false, 1=true

# Genoyped, we map number of alleles to risk
if genotyped == 1:

    # The number of risk alleles that I carry is:
    genomic_risk = 0  # 0: < 8   1: 8 or 9    2: 10 or more
                      # 0: low   1: moderate  2: high

# Not genotyped, we ask for family history
else:

    # Based on the squamous cell skin cancer histories of my parents, siblings and children, my genetic risk for this cancer is: 
    genomic_risk = 0  # 0: Low 1: Moderate 2: High


# Step 1: define variables based on gender.

if gender == "female"
    B = [0.67, 0.08, 0.27, 0.16, 0.54, 1.74, 0.98, 1.51]
    alpha0 = -10.50
    alpha1 = 0.17
    gamma = 3.42  # double check this name
else:
    B = [0.62, 0.09, 0.13, 0.30, 0.66, 1.80, 1.02, 1.37]
    alpha0 = -9.89
    alpha1 = 0.17
    gamma = 2.60

# Step 2: parse input for covariates

z1 = age_years/10.0
z2 = int(sunburn_tendency==1) # moderate
z3 = int(sunburn_tendency==2) # high
z4 = past_rx_invasive         # 1 indicates past diagnosis of invasive carcinoma
z5 = past_rx_insitu           # 1 indicates past diagnosis of non invasive (in-situ)
z6 = past_rx_keratosis        # 1 indicates past diagnosis of actinic keratosis
z7 = int(genomic_risk==1)     # moderate genetic risk
z8 = int(genomic_risk==2)     # high genetic risk (either by way of alleles or report)

Z = [z1, z2, z3, z4, z5, z6, z7, z8]
# The output is the probability P of developing a squamous cell cancer in the next three years. P is given by

summation = 0
for i in range(0,8):
    summation += B[i]*Z[i]

# assigned probability P of developing a new cancer in the next three years. 

inner = 1 + ((gamma/alpha1) * math.exp(alpha0+3*alpha1+summation))
exponent = -1*(1/gamma)
P = 1 - (inner**exponent)


# 2.2 Final Output to user: 
# Your probability of developing a new squamous cell skin cancer in the next three years is  _____ % (INSERT 100xP).
answer = "%s" %(P * 100) + "%"
