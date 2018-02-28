import unittest
from pyImageSaver import pyImageSaver

class TestPyImageSaver(unittest.TestCase):

	def setUp(self):
		self.pimas= pyImageSaver()
	
	def tearDown(self):
		self.pimas = None
		
	def test_getBaseUrlHttp(self):
		baseUrl=(self.pimas).getBaseUrl(url="http://url.com/page/img.png/")
		self.assertTrue(baseUrl=="http://url.com/")
		
	def test_getBaseUrlHttps(self):
		baseUrl=(self.pimas).getBaseUrl(url="https://url.com/page/img.png/")
		self.assertTrue(baseUrl=="https://url.com/")
	
	def test_getBaseUrlNoHttp(self):
		baseUrl=(self.pimas).getBaseUrl(url="url.com/page/img.png/")
		self.assertTrue(baseUrl=="url.com/")	
	
	def test_getFileNameWS(self):
		name=self.pimas.getFileName(url="http://url.com/page/img.png/")
		self.assertTrue(name=="img.png")
		
	def test_getFileNameNS(self):
		name=self.pimas.getFileName(url="http://url.com/page/img.png")
		self.assertTrue(name=="img.png")
		
	def test_concatWS(self):
		self.pimas.baseUrl="http://url.com/"
		url=self.pimas.concat("/apage/")
		self.assertTrue(url=="http://url.com/apage/")
		
	def test_concatNS(self):
		self.pimas.baseUrl="http://url.com"
		url=self.pimas.concat("/apage/")
		self.assertTrue(url=="http://url.com/apage/")

	def test_isInternalT(self):
		self.assertTrue(self.pimas.isInternal("/apage/"))

	def test_isInternalF(self):
		self.assertFalse(self.pimas.isInternal("http://url.com/apage/"))
		
if __name__ == '__main__':
    unittest.main()