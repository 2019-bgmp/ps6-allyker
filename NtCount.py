#!/usr/bin/env python

#counts nucleotides in fastq file

#current test files:
#/projects/bgmp/shared/Bi621/800_3_PE5_interleaved.fq_1
#/projects/bgmp/shared/Bi621/800_3_PE5_interleaved.fq_2
#/projects/bgmp/shared/Bi621/800_3_PE5_interleaved.fq.unmatched

file1='/projects/bgmp/shared/Bi621/800_3_PE5_interleaved.fq_1'
file2='/projects/bgmp/shared/Bi621/800_3_PE5_interleaved.fq_2'
file3='/projects/bgmp/shared/Bi621/800_3_PE5_interleaved.fq.unmatched'


NTcount=0
with open(file1,"r") as fh:
    i = 0
    for line in fh:
        i+=1
        line = line.strip('\n')
        if i%4 == 2:
            #print(line)
            NTcount+=int(len(line))
            #print(NTcount)
    print(file1, "total=", NTcount)

with open(file2,"r") as fh2:
    i = 0
    for line in fh2:
        i+=1
        line = line.strip('\n')
        if i%4 == 2:
            #print(line)
            NTcount+=int(len(line))
            #print(NTcount)
    print(file1, file2, "total=", NTcount)

with open(file3,"r") as fh3:
    i = 0
    for line in fh3:
        i+=1
        line = line.strip('\n')
        if i%4 == 2:
            #print(line)
            NTcount+=int(len(line))
            #print(NTcount)

print("final total=", NTcount)
