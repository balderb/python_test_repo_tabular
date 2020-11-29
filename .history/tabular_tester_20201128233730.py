from tabula import read_pdf

## a build-in ssl module of python
import ssl

url = "url.pdf"

try:
	df =read_pdf("https://www.frontiersin.org/articles/10.3389/fpsyg.2019.02623/full")

# print the data frame (pandas)
	print(df)

except Excemtion as e:
	print("Error {}".format(e))


