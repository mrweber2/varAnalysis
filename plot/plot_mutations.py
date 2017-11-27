#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
import csv


x = []
frame = []
nonfr = []
nonsyn = []
syn = []
stop = []
loss = []
unknown = []
total = []

isFirst = True

with open('Top50_geneMuts.tsv','r') as f:
    fin = csv.reader(f,delimiter='\t')
    for nrow in fin:
        if isFirst:
            isFirst = False
            continue
        else:
            #print(row)
            #nrow = row.split("\t")
            x.append(nrow[0])
            frame.append(nrow[1])
            nonfr.append(nrow[2])
            nonsyn.append(nrow[3])
            syn.append(nrow[4])
            stop.append(nrow[5])
            loss.append(nrow[6])
            unknown.append(nrow[7])
            total.append(nrow[8])

f.close()
#print(x,total)

fig, ax = plt.subplots(figsize=(200,20))

ax.set_xlabel("Genes")
ax.set_ylabel("Mutation Count",fontsize=12)

ax.set_ylim(0,600)
#ax.set_yticks(0,600,50)

ax.plot(total, label='total', color='red', linestyle='dashed')
ax.plot(frame, label='frameshifts', color='green', linestyle='dashed')
ax.plot(nonfr, label='nonframeshifts', color='blue', linestyle='dashed')
ax.plot(nonsyn, label='nonsynonymous', color='orange', linestyle='dashed')
ax.plot(syn, label='synonymous', color='forestgreen', linestyle='dashed')
ax.plot(stop, label='stop gain', color='yellow', linestyle='dashed')
ax.plot(loss, label='stop loss', color='magenta', linestyle='dashed')
ax.plot(unknown, label='unknown',color='black', linestyle='dashed')

legend = ax.legend(loc='upper right', shadow=True)

ax.set_title("Leiomyoma Mutation Types in Genes",fontsize=25)

plt.xticks(range(len(total)), x, rotation=60)
plt.show()

plt.savefig("GeneMuts_Leiomyoma.pdf")
