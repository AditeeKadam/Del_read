#Make the search seq for minisatllite removal

# The input_file_name is a file containing details related  the cooridnates of the homolog
# The following columns are required:

# Column 1 – Start of the homolog1
# Column 2 - Start of the homolog2
# Column 3 – Length of the homolog
# Column 4 – Chromsome


def search_seq(fasta1, input_file ):  
    
   
    chr_list = ['1','2','3','4', '5', '6', '7', '8', '9','10', '11', '12', 
        '13', '14', '15', '16', '17', '18','19','20', '21',  '22', 'X', 'Y']
    num_list = list(range(0,24))
    chr_key = dict(zip(chr_list,num_list ))
    ref_genome_chr = '/home/labs/shlush/shared/broad_hg19/Homo_sapiens_assembly19.fa'
    chr_seq = list(SeqIO.parse(ref_genome_chr, "fasta"))
    count_total = []  
    ofile = open(fasta1, 'w')
    with open(input_file,'r') as f:
        f.readline()
        for i,line in enumerate(f):

            Start1,Start2,Length, Chr = (x for x in line.strip().split())
            #do not forget to close it


            Chr1 = chr_key[str(Chr)]



            str1 =  str(chr_seq[Chr1][int(Start_del)  :int(End_del) ].seq)
            count_total.append(">" + "{c}_{s}_{e}_{l}".format(c = Chr, s = Start_del, e = End_del, l = Homolog) + "\n" + str1 + "\n" )

            if i % 100000:


                ofile.writelines(count_total)
                count_total = []



        ofile.writelines(count_total)
        ofile.close() 

