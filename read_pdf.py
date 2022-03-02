import tabula

# Read pdf into a list of DataFrame
dfs = tabula.read_pdf("caminho do arquivo.pdf", pages='all')

# convert PDF into CSV
tabula.convert_into("caminho do arquivo.pdf", "output.csv", output_format="csv", pages='all')

# convert all PDFs in a directory
tabula.convert_into_by_batch("D:\\MATHEUS AMARAL\\Python\\MainWorkspace\\read-pdf", output_format='csv', pages='all')