from Bio.SeqUtils import gc_fraction

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