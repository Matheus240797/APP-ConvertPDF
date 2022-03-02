#from PyPDF2 import PdfFileReader, PdfFileWriter
#
#file_path = r'D:\MATHEUS AMARAL\Python\MainWorkspace\read-pdf\00a1addc-4c2c-4937-b728-9ad8b6083f89.pdf'
#pdf = PdfFileReader(file_path)
#
#with open('Arquivo.txt', 'w') as f:
#    for page_num in range(pdf.numPages):
#        #print('Page: {0}'.format(page_num))
#        pageObj = pdf.getPage(page_num)
#
#        try:
#            txt = pageObj.extractText()
#            print(''.center(100, '-'))
#        except:
#            pass
#        else:
#            #f.write('Page {0}\n'.format(page_num+1))
#            #f.write(''.center(100, '-'))
#            f.write(txt)
#    f.close()
#
## Import the required Module
#import tabula
## Read a PDF File
#df = tabula.read_pdf("D:\\MATHEUS AMARAL\\Python\\MainWorkspace\\read-pdf\\00a1addc-4c2c-4937-b728-9ad8b6083f89.pdf", pages='all')[0]
## convert PDF into CSV
#tabula.convert_into("D:\\MATHEUS AMARAL\\Python\\MainWorkspace\\read-pdf\\00a1addc-4c2c-4937-b728-9ad8b6083f89.pdf", "D:\\MATHEUS AMARAL\\Python\\MainWorkspace\\read-pdf\\clsarquivo.csv", output_format="csv", pages='all')
#print(df)