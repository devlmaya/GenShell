from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

def obtener_desde_archivo(ruta):
    return list(SeqIO.parse(ruta, 'fasta'))[0]

def obtener_manual():
    sec = input("Ingresa la secuencia de ADN: ")
    return SeqRecord(Seq(sec), id="Manual", description="Input directo")