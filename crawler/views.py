# importing libraries
from bs4 import BeautifulSoup
import requests

class productMap(dict):
 
  # __init__ function
  def __init__(self):
    self = dict()
 
  # Function to add key:value
  def add(self, key, value):
    self[key] = value

def getProductSpec(soup,product):
	try:
		specTable = soup.find(
			"table", attrs={'id': 'productDetails_techSpec_section_1'})
		specRows = specTable.find_all('tr')
		for i in range(0,len(specRows)):
			specRow=specRows[i]
			rowHead=specRow.find("th",attrs={'class':'a-color-secondary a-size-base prodDetSectionEntry'}).string.strip()
			rowData=specRow.find("td",attrs={'class':'a-size-base prodDetAttrValue'}).string.strip()
			product.add(rowHead,rowData.encode("ascii","ignore"))
		product.add("spec","ALL")
	except AttributeError:
		spec = "NA"
		product.add("spec","NA")
	print(product)
	return product


def getProductDetails(URL):
	# opening our output file in append mode
	product=productMap()

	# specifying user agent, You can use other user agents
	# available on the internet
	HEADERS = ({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/44.0.2403.157 Safari/537.36',
								'Accept-Language': 'en-US, en;q=0.5'})

	# Making the HTTP Request
	webpage = requests.get(URL, headers=HEADERS)

	# Creating the Soup Object containing all data
	soup = BeautifulSoup(webpage.content, "html.parser")

	# retrieving product title
	try:
		# Outer Tag Object
		title = soup.find("span",
						attrs={"id": 'productTitle'})

		# Inner NavigableString Object
		title_value = title.string

		# Title as a string value
		title_string = title_value.strip().replace(',', '')

	except AttributeError:
		title_string = "NA"
	print("product Title = ", title_string)

	# saving the title in the file
	product.add("title_string",title_string)

	# retrieving MRP
	try:
		MRP = soup.find(
			"span", attrs={'class': 'a-price a-text-price a-size-base'})
		price=MRP.find("span",attrs={'class':'a-offscreen'}).string.strip().replace(',', '')
		# we are omitting unnecessary spaces
		# and commas form our string
	except AttributeError:
		price = "NA"
	print("Product MRP = ", price)
	# saving
	product.add("mrp",price)

        # retrieving Discounted Price
	try:
		dis_price = soup.find(
			"span", attrs={'class': 'a-price a-text-price a-size-medium apexPriceToPay'})
		discountedPrice=dis_price.find("span",attrs={'class':'a-offscreen'}).string.strip().replace(',', '')
		# we are omitting unnecessary spaces
		# and commas form our string
	except AttributeError:
		discountedPrice = "NA"
	print("Discounted Price = ", discountedPrice)
	
	product.add("discountedPrice",discountedPrice)
	
	# retrieving product rating
	try:
		rating = soup.find("i", attrs={
						'class': 'a-icon a-icon-star a-star-4-5'}).string.strip().replace(',', '')

	except AttributeError:

		try:
			rating = soup.find(
				"span", attrs={'class': 'a-icon-alt'}).string.strip().replace(',', '')
		except:
			rating = "NA"
	print("Overall rating = ", rating)
	product.add("rating",rating)
	
       # retrieving product review count
	try:
		review_count = soup.find(
			"span", attrs={'id': 'acrCustomerReviewText'}).string.strip().replace(',', '')

	except AttributeError:
		review_count = "NA"
	print("Total reviews = ", review_count)
	product.add("review_count",review_count)
	
	# print availablility status
	try:
		available = soup.find("div", attrs={'id': 'availability'})
		available = available.find("span").string.strip().replace(',', '')

	except AttributeError:
		available = "NA"
	print("Availability = ", available)
	product.add("available",available)

	# retrieving product spec.
	

	return getProductSpec(soup,product)

