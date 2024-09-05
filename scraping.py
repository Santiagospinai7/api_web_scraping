class Scraper:
  def __init__(self, url, price):
    self.url = url
    self.price = price

  def scrape(self):
    # some scraping logic
    return {"name": "shirt", "price": self.price, "is_offer": True, "url": self.url} 

