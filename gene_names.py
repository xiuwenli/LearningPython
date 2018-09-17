#!/usr/bin/python
import fileinput
import re
import json

Lookup_geneID={}

print "Name   chromosom   the starting position   the ending position"
for each_line_of_text in fileinput.input(['/home/xiuwenli/data/Homo_sapiens.GRCh37.75.gtf']):
    gene_name_matches = re.findall(r'gene_name \"(.*?)\";',each_line_of_text)
    gene_id_matches = re.findall(r'gene_id \"(.*?)\";',each_line_of_text)
    text_in_columns = re.split('\t',each_line_of_text)
    if len(text_in_columns)>3:
       if text_in_columns[2] == "gene":
          if gene_name_matches:
             if gene_id_matches:
                Lookup_geneID[gene_id_matches[0]] = gene_name_matches[0]
                print str(Lookup_geneID[gene_id_matches[0]]) + "\t" + text_in_columns[0] + "\t" + text_in_columns[3] + "\t" + text_in_columns[4]
