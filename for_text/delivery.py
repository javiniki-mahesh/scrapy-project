class Structure_images_urls:
    def __init__(self, base_url):
        self.__base_url = base_url # private variable
    
    def make_images_structured(self, images):
        for image in range(len(images)):
            if images[image]:
                if images[image].startswith('/'):
                    images[image] = self.__base_url + images[image]
        return images
    
    def make_urls_structured(self, urls):
        for url in range(len(urls)):
            if urls[url]:
                if urls[url].startswith('/'):
                    urls[url] = self.__base_url + urls[url]
        return urls
