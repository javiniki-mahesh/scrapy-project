#                       back up
# import scrapy
# import re
# from scrapy import Selector

# class ExampleSpider(scrapy.Spider):
#     name = "example"
#     # allowed_domains = ["example.com"]
#     start_urls = [input('enter urls : ')]

#     def parse(self, response):
#         # getting urls
#         original_anchor_links = response.xpath("//a/@href").getall()

#         s = self.start_urls[0]
#         substring = s[:s.index('.com')+4]


#         base_anchor_links = []

#         for anchor in original_anchor_links:
#             if anchor.startswith('/'):
#                 base_anchor_links.append(substring + anchor)
#             else:
#                 base_anchor_links.append(anchor)

#         pattern = r'\.com\/(.*?)\/'
#         com_pattern = r'\.com\/(.*?)\/'
#         non_com_pattern = r'\/(.*?)\/'

#         # for link in original_anchor_links:
#         #     if '.com'  in link:


#         l = []
#         for link in base_anchor_links:
#             result = re.findall(pattern, link)
#             if len(result) >=1:
#                 l.append(result[0])


#         from collections import Counter

#         # Count the occurences of each value
#         counts = Counter(l)

#         # Get the value that has the highest count
#         max_value = counts.most_common(1)[0]


#         imp_urls = []
#         for i in base_anchor_links:
#             if max_value[0] in i:
#                 imp_urls.append(i)

# #-----------------------------------------
# # till here to get imp urls


#         # blogs lirqs
#         # passing achor links as they got  -----
#         for imp_u in imp_urls:
#             selector = Selector(response)
#             node = selector.xpath('//a[@href=' + '\"' + imp_u + '\"' + ']')
#             parent = node.xpath('..')
#             children = parent.xpath('*').extract()

#             # -----> dictionary to store child tags 
#             child_tags = dict()
#             for chi in children:
#                 child_tags[chi] = []

#             for ch in children:
#                 sel = Selector(text = ch)
#                 all_sub = sel.xpath('//*')

#                 for i in all_sub:
#                     print('\n\n i', i, '\n\n')
                
#                 # ----> to find all tags grand parent -> parent -> child -> grand child .....
#                 # for ex_i in all_sub.extract():
#                 #     print('\n\n extracted i : ', ex_i, '\n\n')

#                 #     yield {
#                 #         'extracted sub tags' : ex_i
#                 #     }

#                 indivisible = sel.xpath('//*[not(*)]')
#                 # text = indivisible.xpath('text()').extract()
#                 for indv in indivisible:
#                     tag_info = indv.extract()
#                     if 'src' in tag_info:                           # for finding images
#                         image = indv.xpath('@src').extract()        
#                     else:
#                         image = ''

#                     if 'href' in tag_info:                          # for finding href(anchor tag)
#                         href = indv.xpath('@href').extract()
#                     else:
#                         href = ''
                    
#                     if 'datetime' in tag_info:                      # for finding datetime
#                         datetime = indv.xpath('@datetime').extract()
#                     else :
#                         datetime = ''

#                     text = indv.xpath('text()').extract()
#                     # yield{
#                     #     # 'indivisible' : indv.extract(),
#                     #     # 'text' : [t.strip() for t in text],
#                     #     # 'image' : image,
#                     #     # 'href' : href,
#                     #     # 'datetime' : datetime,
#                     #     'urls' : imp_u
#                     #     # indv.xpath('text()').extract()
#                     # }
                
#         yield{
#             'anchor links ': original_anchor_links,
#             'base anchor links ' : base_anchor_links,
#             'important url' : imp_urls
#         }
           


#             # yield child_tags

#             # yield {
#             #     'children' : children,
#             #     # 'path' : path,
#             #     # 'result' : result,
#             #     # 'sub_child_result' : sub_child_result
#             # }



#                    ########     level 2       ##########


# import scrapy
# import re
# from scrapy import Selector
# from collections import Counter

# class ExampleSpider(scrapy.Spider):
#     name = "example"
#     # allowed_domains = ["example.com"]
#     start_urls = [input('enter urls : ')]

#     def parse(self, response):
#         # getting urls
#         original_anchor_links = response.xpath("//a/@href").getall()

#         # finding .com for .com domains
#         s = self.start_urls[0]
#         substring = s[:s.index('.com')+4]

#         # for base_anchor_links adding meaningful urls
#         base_anchor_links = []
#         for anchor in original_anchor_links:
#             if anchor.startswith('/'):
#                 base_anchor_links.append(substring + anchor)
#             else:
#                 base_anchor_links.append(anchor)

#         pattern = r'\.com\/(.*?)\/'
#         com_pattern = r'\.com\/(.*?)\/'
#         non_com_pattern = r'\/(.*?)\/'


#         # consolidation .com urls and non .com urls with finding pattern
#         com_list = []
#         non_com_list = []
#         pattern_list = []        
#         for link in original_anchor_links:
#             if '.com'  in link:
#                 com = re.findall(com_pattern, link)
#                 if len(com) >= 1 :
#                     com_list.append(com[0])
#                     pattern_list.append(com[0])
#             else:
#                 non_com = re.findall(non_com_pattern, link)
#                 if len(non_com) >= 1 :
#                     non_com_list.append(non_com[0])
#                     pattern_list.append(non_com[0])
        


#         counts = Counter(pattern_list)

#         max_value = counts.most_common(1)[0]

#         original_helping_url = []
#         for link in original_anchor_links:
#             if max_value[0] in link:
#                 original_helping_url.append(link)
        
#         l = []
#         for link in base_anchor_links:
#             result = re.findall(pattern, link)
#             if len(result) >=1:
#                 l.append(result[0])


#         # from collections import Counter

#         # Count the occurences of each value
#         counts = Counter(l)

#         # Get the value that has the highest count
#         max_value = counts.most_common(1)[0]


#         imp_urls = []
#         for i in base_anchor_links:
#             if max_value[0] in i:
#                 imp_urls.append(i)

# #-----------------------------------------
# # till here to get imp urls


#         # blogs lirqs
#         # passing achor links as they got  -----
#         for imp_u in imp_urls:
#             selector = Selector(response)
#             node = selector.xpath('//a[@href=' + '\"' + imp_u + '\"' + ']')
#             parent = node.xpath('..')
#             children = parent.xpath('*').extract()

#             # -----> dictionary to store child tags 
#             child_tags = dict()
#             for chi in children:
#                 child_tags[chi] = []

#             for ch in children:
#                 sel = Selector(text = ch)
#                 all_sub = sel.xpath('//*')

#                 for i in all_sub:
#                     print('\n\n i', i, '\n\n')
                
#                 # ----> to find all tags grand parent -> parent -> child -> grand child .....
#                 # for ex_i in all_sub.extract():
#                 #     print('\n\n extracted i : ', ex_i, '\n\n')

#                 #     yield {
#                 #         'extracted sub tags' : ex_i
#                 #     }

#                 indivisible = sel.xpath('//*[not(*)]')
#                 # text = indivisible.xpath('text()').extract()
#                 for indv in indivisible:
#                     tag_info = indv.extract()
#                     if 'src' in tag_info:                           # for finding images
#                         image = indv.xpath('@src').extract()        
#                     else:
#                         image = ''

#                     if 'href' in tag_info:                          # for finding href(anchor tag)
#                         href = indv.xpath('@href').extract()
#                     else:
#                         href = ''
                    
#                     if 'datetime' in tag_info:                      # for finding datetime
#                         datetime = indv.xpath('@datetime').extract()
#                     else :
#                         datetime = ''

#                     text = indv.xpath('text()').extract()
#                     # yield{
#                     #     # 'indivisible' : indv.extract(),
#                     #     # 'text' : [t.strip() for t in text],
#                     #     # 'image' : image,
#                     #     # 'href' : href,
#                     #     # 'datetime' : datetime,
#                     #     'urls' : imp_u
#                     #     # indv.xpath('text()').extract()
#                     # }
                
#         yield{
#             'original anchor links ': original_anchor_links,
#             'base anchor links ' : base_anchor_links,
#             'important url' : imp_urls,
#             'com list' : com_list,
#             'non com list' : non_com_list,
#             'pattern list' : pattern_list,
#             'l' : l,
#             'original helping url' : original_helping_url
#         }
           


#             # yield child_tags

#             # yield {
#             #     'children' : children,
#             #     # 'path' : path,
#             #     # 'result' : result,
#             #     # 'sub_child_result' : sub_child_result
#             # }



#                                                                               able to extract to some extend(indivisible tags information) to get all href data, image data, text data, date time data


# import scrapy
# import re
# from scrapy import Selector
# from collections import Counter

# class ExampleSpider(scrapy.Spider):
#     name = "example"
#     # allowed_domains = ["example.com"]
#     start_urls = [input('enter urls : ')]

#     def parse(self, response):
#         # getting urls
#         original_anchor_links = response.xpath("//a/@href").getall()

#         # get only unique urls
#         original_anchor_links = [value for i, value in enumerate(original_anchor_links) if value not in original_anchor_links[:i]]

#         # finding .com for .com domains
#         s = self.start_urls[0]
#         substring = s[:s.index('.com')+4]

#         # for base_anchor_links adding meaningful urls
#         base_anchor_links = []
#         for anchor in original_anchor_links:
#             if anchor.startswith('/'):
#                 base_anchor_links.append(substring + anchor)
#             else:
#                 base_anchor_links.append(anchor)

#         pattern = r'\.com\/(.*?)\/'
#         com_pattern = r'\.com\/(.*?)\/'
#         non_com_pattern = r'\/(.*?)\/'


#         # consolidation .com urls and non .com urls with finding pattern
#         com_list = []
#         non_com_list = []
#         pattern_list = []        
#         for link in original_anchor_links:
#             if '.com'  in link:
#                 com = re.findall(com_pattern, link)
#                 if len(com) >= 1 :
#                     com_list.append(com[0])
#                     pattern_list.append(com[0])
#             else:
#                 non_com = re.findall(non_com_pattern, link)
#                 if len(non_com) >= 1 :
#                     non_com_list.append(non_com[0])
#                     pattern_list.append(non_com[0])
        


#         counts = Counter(pattern_list)

#         max_value = counts.most_common(1)[0]

#         original_helping_url = []
#         for link in original_anchor_links:
#             if max_value[0] in link:
#                 original_helping_url.append(link)
# #---------------------------------------------------
# ## till here getting helping urls to extract data
        
#         l = []
#         for link in base_anchor_links:
#             result = re.findall(pattern, link)
#             if len(result) >=1:
#                 l.append(result[0])


#         # from collections import Counter

#         # Count the occurences of each value
#         counts = Counter(l)

#         # Get the value that has the highest count
#         max_value = counts.most_common(1)[0]


#         imp_urls = []
#         for i in base_anchor_links:
#             if max_value[0] in i:
#                 imp_urls.append(i)

# #-----------------------------------------
# # till here to get imp urls


#         # blogs lirqs
#         # passing achor links as they got  -----
#         # for imp_u in imp_urls:
#         for imp_u in original_helping_url:
#             selector = Selector(response)
#             node = selector.xpath('//a[@href=' + '\"' + imp_u + '\"' + ']')
#             parent = node.xpath('..')
#             # I want only child elements  -> so that in future if i want to add all sub elements to individual child
#             children = parent.xpath('*').extract()  # matches only child elements

#             # -----> dictionary to store child tags 
#             child_tags = dict()
#             for chi in children:
#                 child_tags[chi] = []

#             for ch in children:
#                 sel = Selector(text = ch)
#                 # all sub elements to join main child
#                 all_sub = sel.xpath('//*')  # matches all elements

#                 indivisible = sel.xpath('//*[not(*)]')

#                 indivisible.extract()

#                 for i in indivisible:
#                     i.extract()
#                 # text = indivisible.xpath('text()').extract()

#                 # removing tags which does not having image or href or datetime or text
#                 modified_indivisible = []
#                 for ind in indivisible:
#                     tag_info = ind.extract()

#                     if 'src' in tag_info or  'href' in tag_info or 'datetime' in tag_info or ind.xpath('text()').extract_first() != None:
#                         modified_indivisible.append(ind)



#                 for indv in modified_indivisible:
#                     tag_info = indv.extract()

#                     if 'src' in tag_info:                           # for finding images
#                         image = indv.xpath('@src').extract()        
#                     else:
#                         image = ''

#                     if 'href' in tag_info:                          # for finding href(anchor tag)
#                         href = indv.xpath('@href').extract()
#                     else:
#                         href = ''

#                     if 'datetime' in tag_info:                      # for finding datetime
#                         datetime = indv.xpath('@datetime').extract()
#                     else :
#                         datetime = ''

#                     text = indv.xpath('text()').extract_first()
#                     text = text.strip() if text != None else text

                    
#                     yield{
#                         'indivisible tag' : indv.extract(),
#                         'text' : text,
#                         'image' : image,
#                         'href' : href,
#                         'datetime' : datetime,
#                         # 'urls' : imp_u
#                     }
                
                
#         # yield{
#         #     'original anchor links ': original_anchor_links,
#             # 'base anchor links ' : base_anchor_links,
#             # 'important url' : imp_urls,
#             # 'com list' : com_list,
#             # 'non com list' : non_com_list,
#             # 'pattern list' : pattern_list,
#             # 'l' : l,
#             # 'original helping url' : original_helping_url
#         # }
           



#                                                                                                   able to extract all data in lists of href, image, text , datetime

# import scrapy
# import re
# from scrapy import Selector
# from collections import Counter

# class ExampleSpider(scrapy.Spider):
#     name = "example"
#     # allowed_domains = ["example.com"]
#     start_urls = [input('enter urls : ')]

#     def parse(self, response):

#         text_child = []
#         image_child = []
#         href_child = []
#         date_time_child = []

#         # getting urls
#         original_anchor_links = response.xpath("//a/@href").getall()

#         # get only unique urls
#         original_anchor_links = [value for i, value in enumerate(original_anchor_links) if value not in original_anchor_links[:i]]

#         # finding .com for .com domains
#         s = self.start_urls[0]
#         substring = s[:s.index('.com')+4]

#         # for base_anchor_links adding meaningful urls
#         base_anchor_links = []
#         for anchor in original_anchor_links:
#             if anchor.startswith('/'):
#                 base_anchor_links.append(substring + anchor)
#             else:
#                 base_anchor_links.append(anchor)

#         pattern = r'\.com\/(.*?)\/'
#         com_pattern = r'\.com\/(.*?)\/'
#         non_com_pattern = r'\/(.*?)\/'


#         # consolidation .com urls and non .com urls with finding pattern
#         com_list = []
#         non_com_list = []
#         pattern_list = []        
#         for link in original_anchor_links:
#             if '.com'  in link:
#                 com = re.findall(com_pattern, link)
#                 if len(com) >= 1 :
#                     com_list.append(com[0])
#                     pattern_list.append(com[0])
#             else:
#                 non_com = re.findall(non_com_pattern, link)
#                 if len(non_com) >= 1 :
#                     non_com_list.append(non_com[0])
#                     pattern_list.append(non_com[0])
        


#         counts = Counter(pattern_list)

#         max_value = counts.most_common(1)[0]

#         original_helping_url = []
#         for link in original_anchor_links:
#             if max_value[0] in link:
#                 original_helping_url.append(link)
# #---------------------------------------------------
# ## till here getting helping urls to extract data
        
#         l = []
#         for link in base_anchor_links:
#             result = re.findall(pattern, link)
#             if len(result) >=1:
#                 l.append(result[0])


#         # from collections import Counter

#         # Count the occurences of each value
#         counts = Counter(l)

#         # Get the value that has the highest count
#         max_value = counts.most_common(1)[0]


#         imp_urls = []
#         for i in base_anchor_links:
#             if max_value[0] in i:
#                 imp_urls.append(i)

# #-----------------------------------------
# # till here to get imp urls


#         # blogs lirqs
#         # passing achor links as they got  -----
#         # for imp_u in imp_urls:
#         for imp_u in original_helping_url:
#             selector = Selector(response)
#             node = selector.xpath('//a[@href=' + '\"' + imp_u + '\"' + ']')
#             parent = node.xpath('..')
#             # I want only child elements  -> so that in future if i want to add all sub elements to individual child
#             children = parent.xpath('*').extract()  # matches only child elements

#             # -----> dictionary to store child tags 
#             child_tags = dict()
#             for chi in children:
#                 child_tags[chi] = []

#             for ch in children:
#                 sel = Selector(text = ch)
#                 # all sub elements to join main child
#                 all_sub = sel.xpath('//*')  # matches all elements

#                 indivisible = sel.xpath('//*[not(*)]')

#                 indivisible.extract()

#                 for i in indivisible:
#                     i.extract()
#                 # text = indivisible.xpath('text()').extract()

#                 # removing tags which does not having image or href or datetime or text
#                 modified_indivisible = []
#                 for ind in indivisible:
#                     tag_info = ind.extract()

#                     if 'src' in tag_info or  'href' in tag_info or 'datetime' in tag_info or ind.xpath('text()').extract_first() != None:
#                         modified_indivisible.append(ind)


                
#                 for indv in modified_indivisible:
#                     tag_info = indv.extract()

#                     if 'src' in tag_info:                           # for finding images
#                         image = indv.xpath('@src').extract()        
#                     else:
#                         image = ''

#                     if 'href' in tag_info:                          # for finding href(anchor tag)
#                         href = indv.xpath('@href').extract()
#                     else:
#                         href = ''

#                     if 'datetime' in tag_info:                      # for finding datetime
#                         datetime = indv.xpath('@datetime').extract()
#                     else :
#                         datetime = ''

#                     text = indv.xpath('text()').extract_first()
#                     text = text.strip() if text != None else text

#                     # to return indivisible data
#                     # yield{
#                     #     'indivisible tag' : indv.extract(),
#                     #     'text' : text,
#                     #     'image' : image,
#                     #     'href' : href,
#                     #     'datetime' : datetime,
#                     #     # 'urls' : imp_u
#                     # }

#                     # we are in indivisible child tags going back to main child where we are getting urls
                    

#                     # adding data
#                     text_child.append(text)
#                     image_child.append(image)
#                     href_child.append(href)
#                     date_time_child.append(datetime)

#                 # to return child data
#         yield {
#             'text_child' : text_child,
#             'image_child' : image_child,
#             'href_child' : href_child,
#             'date_time_child' : date_time_child
#         }
                
                
#         # yield{
#         #     'original anchor links ': original_anchor_links,
#             # 'base anchor links ' : base_anchor_links,
#             # 'important url' : imp_urls,
#             # 'com list' : com_list,
#             # 'non com list' : non_com_list,
#             # 'pattern list' : pattern_list,
#             # 'l' : l,
#             # 'original helping url' : original_helping_url
#         # }
        

#                                                                                   we are able to get the data for each direct child


# import scrapy
# import re
# from scrapy import Selector
# from collections import Counter

# class ExampleSpider(scrapy.Spider):
#     name = "example"
#     # allowed_domains = ["example.com"]
#     start_urls = [input('enter urls : ')]

#     def parse(self, response):

#         # text_child = []
#         # image_child = []
#         # href_child = []
#         # date_time_child = []

#         # getting urls
#         original_anchor_links = response.xpath("//a/@href").getall()

#         # get only unique urls
#         original_anchor_links = [value for i, value in enumerate(original_anchor_links) if value not in original_anchor_links[:i]]

#         # finding .com for .com domains
#         s = self.start_urls[0]
#         substring = s[:s.index('.com')+4]

#         # for base_anchor_links adding meaningful urls
#         base_anchor_links = []
#         for anchor in original_anchor_links:
#             if anchor.startswith('/'):
#                 base_anchor_links.append(substring + anchor)
#             else:
#                 base_anchor_links.append(anchor)

#         pattern = r'\.com\/(.*?)\/'
#         com_pattern = r'\.com\/(.*?)\/'
#         non_com_pattern = r'\/(.*?)\/'


#         # consolidation .com urls and non .com urls with finding pattern
#         com_list = []
#         non_com_list = []
#         pattern_list = []        
#         for link in original_anchor_links:
#             if '.com'  in link:
#                 com = re.findall(com_pattern, link)
#                 if len(com) >= 1 :
#                     com_list.append(com[0])
#                     pattern_list.append(com[0])
#             else:
#                 non_com = re.findall(non_com_pattern, link)
#                 if len(non_com) >= 1 :
#                     non_com_list.append(non_com[0])
#                     pattern_list.append(non_com[0])
        


#         counts = Counter(pattern_list)

#         max_value = counts.most_common(1)[0]

#         original_helping_url = []
#         for link in original_anchor_links:
#             if max_value[0] in link:
#                 original_helping_url.append(link)
# #---------------------------------------------------
# ## till here getting helping urls to extract data
        
#         l = []
#         for link in base_anchor_links:
#             result = re.findall(pattern, link)
#             if len(result) >=1:
#                 l.append(result[0])


#         # from collections import Counter

#         # Count the occurences of each value
#         counts = Counter(l)

#         # Get the value that has the highest count
#         max_value = counts.most_common(1)[0]


#         imp_urls = []
#         for i in base_anchor_links:
#             if max_value[0] in i:
#                 imp_urls.append(i)

# #-----------------------------------------
# # till here to get imp urls


#         # blogs lirqs
#         # passing achor links as they got  -----
#         # for imp_u in imp_urls:
#         for imp_u in original_helping_url:
#             selector = Selector(response)
#             node = selector.xpath('//a[@href=' + '\"' + imp_u + '\"' + ']')
#             parent = node.xpath('..')
#             # I want only child elements  -> so that in future if i want to add all sub elements to individual child
#             children = parent.xpath('*').extract()  # matches only child elements

#             # -----> dictionary to store child tags 
#             child_tags = dict()
#             for chi in children:
#                 child_tags[chi] = []


#             text_child = []
#             image_child = []
#             href_child = []
#             date_time_child = []
#             #dup
#             indv_tag = []
#             for ch in children:
                
#                 sel = Selector(text = ch)
#                 # all sub elements to join main child
#                 all_sub = sel.xpath('//*')  # matches all elements

#                 indivisible = sel.xpath('//*[not(*)]')

#                 indivisible.extract()

#                 for i in indivisible:
#                     i.extract()
#                 # text = indivisible.xpath('text()').extract()

#                 # removing tags which does not having image or href or datetime or text
#                 modified_indivisible = []
#                 for ind in indivisible:
#                     tag_info = ind.extract()

#                     if 'src' in tag_info or  'href' in tag_info or 'datetime' in tag_info or ind.xpath('text()').extract_first() != None:
#                         modified_indivisible.append(ind)


                
#                 for indv in modified_indivisible:
#                     tag_info = indv.extract()

#                     if 'src' in tag_info:                           # for finding images
#                         image = indv.xpath('@src').extract_first()        
#                     else:
#                         image = ''

#                     if 'href' in tag_info:                          # for finding href(anchor tag)
#                         href = indv.xpath('@href').extract_first()
#                     else:
#                         href = ''

#                     if 'datetime' in tag_info:                      # for finding datetime
#                         datetime = indv.xpath('@datetime').extract_first()
#                     else :
#                         datetime = ''

#                     text = indv.xpath('text()').extract_first()
#                     text = text.strip() if text != None else text

#                     # to return indivisible data
#                     # yield{
#                     #     'indivisible tag' : indv.extract(),
#                     #     'text' : text,
#                     #     'image' : image,
#                     #     'href' : href,
#                     #     'datetime' : datetime,
#                     #     # 'urls' : imp_u
#                     # }

#                     # we are in indivisible child tags going back to main child where we are getting urls
                    

#                     # adding data
#                     text_child.append(text)
#                     image_child.append(image)
#                     href_child.append(href)
#                     date_time_child.append(datetime)

#                     indv_tag.append(indv.extract())

#                 # to return child data
#             yield {
#                 'indivisible tag' : indv_tag,
#                 'text_child' : text_child,
#                 'image_child' : image_child,
#                 'href_child' : href_child,
#                 'date_time_child' : date_time_child
#             }
                
                
#         # yield{
#         #     'original anchor links ': original_anchor_links,
#             # 'base anchor links ' : base_anchor_links,
#             # 'important url' : imp_urls,
#             # 'com list' : com_list,
#             # 'non com list' : non_com_list,
#             # 'pattern list' : pattern_list,
#             # 'l' : l,
#             # 'original helping url' : original_helping_url
#         # }
        



