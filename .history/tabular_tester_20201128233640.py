from tabula import read_pdf

## a build-in ssl module of python
import ssl

url = "url.pdf"

try:
	df =read_pdf("https://journals.sagepub.com/doi/abs/10.1177/1065912916639138")

# print the data frame (pandas)
	print(df)

except Excemtion as e:
	print("Error {}".format(e))


