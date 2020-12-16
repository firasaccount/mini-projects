from Bio import Entrez
e=input('Entrer votre email :') 
Entrez.email=e
x='nucleotide' 
y=input('Entrer mots clés:')
z=input('Entrer le nombre max de fichier(doit être un entier positif):') 
a=int(z)
print('Recherche en cours...')

recherche=Entrez.esearch(db=x, term=y, retmax=a) 
resultat=Entrez.read(recherche) 
liste_id=resultat['IdList'] 
print('les ID trouvés sont:')
print( liste_id)

print('Affichage des reusltats en cours..')

from Bio import SeqIO
download=Entrez.efetch(db=x, id=liste_id,rettype='gb',retmode='text') 
for i in SeqIO.parse(download,'gb'): 
    print("%s %s"%(i.id,i.description))

b=str (input('Entrer id de fichier que vous voulez telecharger:')) 
    
NAgene=Entrez.efetch(db='nucleotide', id=b, idtype='acc', rettype='gb',)  
records=SeqIO.parse(NAgene,'gb')
for i,record in enumerate(records):
    print(len(record.features))
    for feature in record.features:
        if  feature.type == "CDS":
            print ('id de proteine de cette sequence est:',feature.qualifiers["protein_id"])
            sequence=feature.location.extract(record).seq
            print ('la region codonte est:',sequence)
from Bio import Restriction
Ana = Restriction.Analysis(Restriction.CommOnly, sequence, linear=True)
Carte_de_restriction=Ana.print_that()
print('La carte de restriction est:'
print(Carte_de_restriction)


    
          




