# the following is the soul of whole

        # through maximum occurred pattern we are creating a list of links by which we are moving forward
        # if any content is missing while scrapping the following plays major role 
        # till now focusing only one pattern
        # we can modify the following code for better scraping in the next level

class Data:
    def __init__ (self, original_anchor_links, base_url):
        self.original_anchor_links = original_anchor_links
        self.base_url = base_url

    def absolute_data(self, url_pattern_to_extract):
            """This function will return all possible combinations from given website"""
            self.original_helping_url = []
            for link in self.original_anchor_links:  # I think base_anchor_links should present instead original_anchor_links  -----> changed ---> rechanged to original_anchor_links for XPath we need only part of url not complete
                for pattern in url_pattern_to_extract:
                    if '/' + pattern in link:          # checking only '/category' values            # better to keep an eye
                        if link.startswith('/' + pattern) or link.startswith(self.base_url + '/' + pattern):
                            # above line is very important for segregating the urls by first category
                            self.original_helping_url.append(link)
            return self.original_helping_url
   

    def relative_data(self, max_occur_patten):
                """This function will return maximum repeated combination from given website"""
                self.original_helping_url = []
                for link in self.original_anchor_links:  # I think base_anchor_links should present instead original_anchor_links  -----> changed ---> rechanged to original_anchor_links for XPath we need only part of url not complete
                    if '/' + max_occur_patten in link:          # checking only '/category' values            # better to keep an eye
                        if link.startswith('/' + max_occur_patten) or link.startswith(self.base_url + '/' + max_occur_patten):
                            # above line is very important for segregating the urls by first category
                            self.original_helping_url.append(link)
                return self.original_helping_url