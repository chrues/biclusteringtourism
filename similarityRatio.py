import difflib

#Calculates similarity index ratio between each bicluster and save in a file
def similarityRatio(biclusters):
    """Calculates similarity index ratio between each bicluster and save results to a file"""

    simRatios = []
    name = "SimIndexRatio4.txt" #.format(txt, exec, paramA, avgSprmnIndex)
    newFile = open(name, "w")
    for i in range(0, len(biclusters)//2 + 1):
        for j in range(0, len(biclusters)):
            if not i == j:
                bicl1, bicl2 = biclusters[i], biclusters[j]
                similarity = difflib.SequenceMatcher(None, bicl1, bicl2)
                simRatio = similarity.ratio()
                simRatios.append(simRatio)

                #Writes the similarity index ratio between the two biclusters at hand on file
                newFile.write("Similarity index between bicluster {} and bicluster {}: {}".format(i, j, simRatio))
    newFile.close()

    return simRatios
