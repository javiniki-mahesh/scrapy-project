class Single:
    def __init__(self, response, single_page):
        self.response = response
        self.single_page = single_page

    def extract_from_single_page(self):
        extraction_text_from_single_page = self.response.xpath("//*[self::h1 or self::h2 or self::h3 or self::h4 or self::h5 or self::h6 or self::p or self::ul or self::ol or self::li or self::strong or self::em]/text()").extract()
        return{
            'Extracted page' : self.single_page,
            'Extracted content from single page' : extraction_text_from_single_page
        }
    

class Get_indivisible:
    def get_indivisible(self,indivisible_tag, text, image, href, datetime, imp_u):
        return {
                'indivisible tag' : indivisible_tag,
                'text' : text,
                'image' : image,
                'href' : href,
                'datetime' : datetime,
                'urls' : imp_u
            }


class Element_wise:
    def all_data_element_wise(self,imp_u, indv_tag, text_child, image_child, href_child, date_time_child):
        return {
            'url' : imp_u,
            'indivisible tag' : indv_tag,
            'text_child' : text_child,
            'image_child' : image_child,
            'href_child' : href_child,
            'date_time_child' : date_time_child
        }
    


class All_in_one:
    def get_all_in_one(self, all_text_child, all_image_child, all_href_child, all_date_time_child, all_indv_tag, url_to_extract):
        return {'text child': all_text_child,
            'image child': all_image_child,
            'href child': all_href_child,
            'date_time child': all_date_time_child,
            'indv_tag': all_indv_tag,
            'url': url_to_extract
            }
    



    
# I have tried to implement getting text from multiple urls that is not getting here
# class Travel_on_each_url:
#     def __init__(self, response, all_urls_to_extract):
#         # self.response = response
#         self.all_urls_to_extract = all_urls_to_extract

#     def multiple_url_text_extraction(self,response):
#         for url in self.all_urls_to_extract:
#             yield response.follow(url, self.extract_text_from_multiple)
    
#     def extract_text_from_multiple(self,response):
#         extraction_text_from_multiple_pages = response.xpath("//*[self::h1 or self::h2 or self::h3 or self::h4 or self::h5 or self::h6 or self::p or self::ul or self::ol or self::li or self::strong or self::em]/text()").extract()
#         yield {
#             'Extracted page' : response.url,
#             'Extracted content from single page' : extraction_text_from_multiple_pages
#         }