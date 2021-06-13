import os
import re
from Bio import SeqIO
now_dir = os.getcwd()    


def get_file_list():
    #函数get_file_list：获取当前文件夹中指定文件
    #输入：无
    #输出：指定文件列表：file_list
    file_temp = os.listdir()
    file_list = []
    for each in file_temp:       
        if ".fas" in each:
            file_list.append(each)
    return file_list

def main():
    fasta_file_list = get_file_list()
    concat_list = []
    for each_file in fasta_file_list:
        with open(each_file, "r") as read_file:
            for each_line in  read_file:
                if each_line[0] == ">":
                    if each_line not in concat_list:
                        concat_list.append(each_line)
    n = 0
    for each_file in fasta_file_list:
        fasta_dict = SeqIO.to_dict(SeqIO.parse(each_file, "fasta"))
        for each_len in fasta_dict:
            seq_len = len(fasta_dict[each_len].seq)
            break
        for index, each_species in enumerate(concat_list):
            if each_species.split("\n")[0][1:] in fasta_dict:
                concat_list[index] = concat_list[index] + str(fasta_dict[each_species.split("\n")[0][1:]].seq)
            else:
                concat_list[index] = concat_list[index] + "?"*seq_len
        n = n + 1
        print("have finished " + str(n) + " genes")
    with open("result.fasta", "a") as write_file:
        for each_line in concat_list:
            write_file.write(each_line + "\n")
                
            


if __name__ == "__main__":
    main()