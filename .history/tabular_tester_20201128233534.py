from tabula import read_pdf

## a build-in ssl module of python
import ssl

url = "url.pdf"

try:
	df =read_pdf("file:///Users/balderbongaerts/Downloads/1065912916639138-1.pdf")

# print the data frame (pandas)
	print(df)

except Excemtion as e:
	print("Error {}".format(e))


