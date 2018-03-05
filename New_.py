#Chris Gell Feb 2018
#Phython script to sort out all of the results


from ij import IJ  
from ij.measure import ResultsTable

IJ.run("Results... ", "")
rtLE=ResultsTable.getResultsTable()

overallEB=rtLE.clone()

IJ.run("Results... ", "")
rtRE=ResultsTable.getResultsTable()

rtLE.addResults()
rtLE.save("OverallResults")

#updateResults()



print rtLE.size()
print rtRE.size()
print overallEB.size()