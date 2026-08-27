#Question 1(i)
sed -n'/and/p' vim question1.sh
#1(ii)
sed ' s/language/lang/g ' question1.sh
#1(iii)
sed '/is/d' question1.sh
#1(iv)
sed '=' question1.sh | sed 'N;s/\n/ /' question1.sh
#1(v)
sed '1,2d' question1.sh
#1(vi)
sed -n'1~2p' question1.sh
#1(vii)
sed 's/Python/python/ ; s/language/lang/' queston1.sh

#Question 2(i)
awk '$2<25 {print $1}' question1.sh
#2(ii)
awk '$3=="Physics" {print $1}' question2.sh
#2(iii)
awk '{ print "$1","$2","$3" }' question2.sh > data2.csv

#Question 3(i)
awk '!/>/' fasta.txt
#3(ii)
sed 's/T/U/g' fasta.txt
#3(iii)
sed 's/seq1/human_gene/' fasta.txt

#Question 4
awk '$4=="PHE"' 1HK0.pdb | awk '{print $2}' > PHE_atoms.xyz
