from tabula import read_pdf
import tabula

## a build-in ssl module of python
import ssl

url = "https://www.frontiersin.org/articles/10.3389/fpsyg.2019.02623/full"

try:
	df =read_pdf(url)

# print the data frame (pandas)
	print(df)

except Excemtion as e:
	print("Error {}".format(e))


