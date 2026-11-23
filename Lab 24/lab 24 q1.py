class DNAseq:
    def __init__(self, seq):
        self.seq = seq
        # Removes all whitespace (spaces, tabs, newlines)
        self.cleaned_seq = ''.join(seq.split())

    def __str__(self):
        return f'input: {self.seq}\ncleaned DNA: {self.cleaned_seq}'

    def erro(self):

        valid_bases = {"A", "T", "G", "C"}


        for i in self.cleaned_seq:
            if i not in valid_bases:
                print("Not a valid DNA seq")

            else :
                print("Valid DNA")

            return
    def cout(self):
        self.A=0
        self.T=0
        self.G=0
        self.C=0
        for i in self.cleaned_seq:
            if i == "A":
               self.A+=1
            if i == "T":
                   self.T += 1
            if i == "G":
                   self.G += 1
            if i == "C":
                   self.C += 1
        print("Total A:", self.A)
        print("Total no. of T:", self.T)
        print("Total no. of C:", self.C)
        print("Total no. of G:", self.G)

    def analyse_dna(self):
        # def gc_content(self.A, self.G, self.G, self):
                self.gc = self.G + self.C
                self.atgc = self.A + self.T + self.C + self.G
                self.percentage = (self.gc / self.atgc) * 100
                # print(percentage)
                return self
    def complement(self):
        self.complementary_seq=""
        for i in self.cleaned_seq:
            if i=="A":
                i="T"
                self.complementary_seq+=i
            elif i=="T":
                i="A"
                self.complementary_seq+=i
            elif i=="C":
                i="G"
                self.complementary_seq+=i
            else:
                i="C"
                self.complementary_seq += i
        print("complementary seq: ", self.complementary_seq)

    def transcribe(self):
        transcrobed_seq = ""
        for i in self.complementary_seq:
            if i == "T":
                 i = "U"
                 transcrobed_seq += i
            else:
                transcrobed_seq += i
        print("transcrobed seq: ", transcrobed_seq)

    def search_seq(self):
        search_seq =input("Search DNA seq: ")
        print (self.cleaned_seq.count(search_seq))


input_seq = 'AT TT AAA CC CTT GC TA GT GTG TG TG TG TAGAGCGGCAGCG G  AG TGC T'
dna_seq = DNAseq(input_seq)

print(dna_seq)
print("Validation Result:")
dna_seq.erro()
dna_seq.cout()
print(dna_seq.analyse_dna())
dna_seq.complement()
dna_seq.transcribe()
dna_seq.search_seq()
