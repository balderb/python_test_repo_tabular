install tabula-py

from tabula import read_pdf

## a build-in ssl module of python
import ssl

url = "url.pdf"

try:
	df =read_pdf(file:///Users/balderbongaerts/Downloads/ast_sci_data_tables_sample.pdf)

# print the data frame (pandas)
	print(df)

except Excemtion as e:
	print("Error {}".format(e))

