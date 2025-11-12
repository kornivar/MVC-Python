from Model.SequenceModel import SequenceModel


class DNKController:
    def __init__(self):
        self.__model = SequenceModel("")

    def add_seq(self, sequence):
        if isinstance(sequence, SequenceModel):
            self.__model = sequence
            self.__model.seq = self.__model.seq.upper()
        else:
            self.__model.seq = str(sequence).upper()

    def get_sequence(self):
        return self.__model.seq

    def validate(self, seq):
        seq = seq.upper()
        dna = False
        rna = False
        for char in seq:
            if char not in 'ACGTU':
                return -1
            else:
                if char == 'T':
                    dna = True
                elif char == 'U':
                    rna = True

                if dna and rna:
                    return -1

        return 0 if dna else 1 if rna else -1

    def transcribe(self, seq):
        seq = seq.upper()
        if self.validate(seq) != 0:
            return None
        return seq.replace('T', 'U')

    def reverse_transcribe(self, seq):
        seq = seq.upper()
        if self.validate(seq) != 1:
            return None
        return seq.replace('U', 'T')

    def reverse_complement(self, seq):
        seq = seq.upper()
        if self.validate(seq) == -1:
            return None
        comp_map = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C', 'U': 'A'}
        try:
            comp = ''.join(comp_map[ch] for ch in seq)
        except KeyError:
            return None
        return comp[::-1]

    def gc_content(self, seq):
        seq = seq.upper()
        length = len(seq)
        if length == 0:
            return 0.0
        gc_count = seq.count('G') + seq.count('C')
        gc_percent = (gc_count / length) * 100
        return gc_percent, length

    def mutate_base(self, seq, index, new_base):
        seq = seq.upper()
        new_base = new_base.upper()
        if index < 0 or index >= len(seq):
            return None
        seq_type = self.validate(seq)
        if seq_type == -1:
            return None
        allowed = "ACGT" if seq_type == 0 else "ACGU"
        if new_base not in allowed:
            return None
        lst = list(seq)
        lst[index] = new_base
        return ''.join(lst)