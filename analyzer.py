from Bio.SeqUtils import gc_fraction
from matplotlib import pylab

def procesar_gc(record):
    return f"{gc_fraction(record.seq):.2f}"

def procesar_complemento(record):
    return record.seq.complement()

def procesar_transcripcion(record):
    return record.seq.transcribe()

def procesar_traduccion(record):
    return record.seq.translate()

def procesar_inversa(record):
    return record.seq.reverse_complement()

def grafica_gc(record):
    pylab.clf()
    gc_val = gc_fraction(record.seq) * 100
    pylab.bar(["Secuencia Actual"], [gc_val], color="skyblue")
    pylab.title("Porcentaje de GC")
    pylab.ylabel("Porcentaje (%)")
    pylab.ylim(0, 100)
    pylab.show()