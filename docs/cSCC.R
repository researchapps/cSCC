calculateProb = function(X, params) {
  age = X[[1]]
  modSunburn = X[[2]]
  highSunburn = X[[3]]
  modRisk = X[[4]]
  highRisk = X[[5]]
  AK = X[[6]]
  inSituhx = X[[7]]
  invhx = X[[8]]
  
  term1 = exp(params[1]+params[3]*age/10+params[4]*modSunburn+params[5]*highSunburn
                +params[6]*modRisk+params[7]*highRisk+params[8]*AK+params[9]*inSituhx+params[10]*invhx)
  
  term2 = exp(3*params[2])-1
  term3 = (1+params[11]/params[2]*term1*term2)
  Prob = 1 - term3^(-1/params[11])
  return(Prob)
}

female_param = c(-10.5, 0.17, 0.67, 0.08, 0.27, 0.16, 0.54, 1.74, 0.98, 1.51, 3.42)
male_param = c(-9.89, 0.17, 0.62, 0.09, 0.13, 0.30, 0.66, 1.80, 1.02, 1.37, 2.60)

femaleProbs = apply(femaleSamples, 1, function(x) calculateProb(x, female_param))
maleProbs = apply(maleSamples, 1, function(x) calculateProb(x, male_param))
