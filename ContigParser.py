#!/usr/bin/env python

#Parse the contigs.fa file that is output by velvetg.
#Extract the FASTA ID lines as you parse the file

#Extract the 2nd and 3rd #
#>NODE_11_length_3717_cov_19.315845

#kmer length 49
#C=N*L/G
#C=coverage, N=# of reads, L=read length, G=genome length
#Ck=C*(L-K+1)/L
#Ck=kmer coverage, K=kmer length

#file:
#contigs.fa
#testfiles:
#Smallcontigs.fa
#Unit_test.fa

Kmer=41
contigLength=[]
kCoverage=0
i=0
contigTotal=0

#regex setup
import re
p=re.compile('>.+')
with open ('/projects/bgmp/akershne/Bi621/PS6/Velvet/1/contigs.fa', 'r') as fh:
    for line in fh:
        line = line.strip('\n')
#regex to grab headers
        m=p.match(line)
        if m:
            i+=1
            #print(m.group())
#regex to get the last 2 numbers
            parts=re.split("_", line)
            #print(parts[3], parts[5])
#Calculate length of reads +store length
            L=int(parts[3])+Kmer-1
            #print(L)
            contigLength.append(L)
            contigTotal+=L
#store coverage value
            kCoverage+=((float(parts[5]))*L)

#Reverse sort lengths
contigLength.sort(reverse=True)
#calculate means
contigMean=contigTotal/len(contigLength)
meanKCoverage=kCoverage/contigTotal
#calculate coverage
Coverage=(meanKCoverage*contigMean)/(contigMean-Kmer+1)


#print(meanKCoverage)
#print(kCoverage)
#print(contigTotal)
#print(contigLength)
#print(kCoverage)
print("# of contigs:", i)
print("Max contig length:",contigLength[0])
print('Mean contig length:',contigMean)
print("Total length of genome assembly:",contigTotal )
print("Mean depth of coverage:",meanKCoverage, Coverage )

#Calculate NP50
n=0
p=0
while n < contigMean:
    n+=contigLength[p]
    p+=1
#print(n, contigMean, contigLength[p-1])
print("NP50:", contigLength[p-1])

#Put contigs into 100bp buckets
print("#Contig length    Number of contigs in this category")
b=0
while b <= (int(contigLength[0])):
    q=0
    count=0
    for q in range(len(contigLength)):
        if b <= contigLength[q] and contigLength[q] < b+100:
            count+=1
        q+=1
    print(b, count)
    b+=100

#print(contigLength)
