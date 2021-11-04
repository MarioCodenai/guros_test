import re

def has_mutation(dna):
    
    for i in dna:
        mutation = re.findall(r'(.)\1{3}', i)
        if mutation:
            return True
            
    return False
