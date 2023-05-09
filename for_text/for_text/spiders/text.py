import scrapy
import re
from scrapy import Selector
from collections import Counter
import pandas

class TextSpider(scrapy.Spider):
    name = "text"
    # allowed_domains = ["text.com"]
    start_urls = [input('enter url to extract text : ')]

    def parse(self, response):
    
        all_text_child = []
        all_image_child = []
        all_href_child = []
        all_date_time_child = []
        all_indv_tag = []

        # getting all urls
        original_anchor_links = response.xpath("//a/@href").getall()

        # getting body urls
        # original_anchor_links = response.xpath("//body//a/@href").getall()

        # get only unique urls
        original_anchor_links = [value for i, value in enumerate(original_anchor_links) if value not in original_anchor_links[:i]]

        # finding .com for .com domains
        s = self.start_urls[0]
        base_url = s[:s.index('.com')+4]

        # for base_anchor_links adding meaningful urls
        base_anchor_links = [] # anchor links with base or domain
        for anchor in original_anchor_links:
            if anchor.startswith('/'):
                base_anchor_links.append(base_url + anchor)
            else:
                base_anchor_links.append(anchor)

        pattern = r'\.com\/(.*?)\/'
        com_pattern = r'\.com\/(.*?)\/'
        non_com_pattern = r'\/(.*?)\/'


        # consolidation .com urls and non .com urls with finding pattern
        com_list = []
        non_com_list = []
        pattern_list = []        
        for link in original_anchor_links:
            if '.com'  in link:
                com = re.findall(com_pattern, link)
                if len(com) >= 1 :
                    com_list.append(com[0])
                    pattern_list.append(com[0])
            else:
                non_com = re.findall(non_com_pattern, link)
                if len(non_com) >= 1 :
                    non_com_list.append(non_com[0])
                    pattern_list.append(non_com[0])
        


        counts = Counter(pattern_list)

        max_value = counts.most_common(1)[0]

        # print(max_value[0])                                                             # here printing
        original_helping_url = []
        for link in original_anchor_links:
            if '/' + max_value[0] in link:          # checking only '/category' values            # better to keep an eye
                if link.startswith('/' + max_value[0]) or link.startswith(base_url + '/' + max_value[0]):
                    # above line is very important for segregating the urls by first category
                    original_helping_url.append(link)
#---------------------------------------------------
## till here getting helping urls to extract data
        
        l = []
        for link in base_anchor_links:
            result = re.findall(pattern, link)
            if len(result) >=1:
                l.append(result[0])


        # from collections import Counter

        # Count the occurences of each value
        counts = Counter(l)

        # Get the value that has the highest count
        max_value = counts.most_common(1)[0]


        imp_urls = []
        for i in base_anchor_links:
            if max_value[0] in i:
                imp_urls.append(i)

#-----------------------------------------
# till here to get imp urls


        # blogs lirqs
        # passing achor links as they got  -----
        # for imp_u in imp_urls:

                                               # based on no.of elements in helping urls we decide which urls list is used to extract data
                                               # defining unwanted urls
        defined_urls_to_remove = ['facebook.com', 'twitter.com', '/privacy/', '/contact/', '/contribute/', '/about/', '/getting-started/']
                                                # removing unwanted urls
        after_removing_unwanted_urls = [x for x in original_anchor_links if not any(y in x for y in defined_urls_to_remove)]
        if len(original_helping_url) < 11:
            url_to_extract = after_removing_unwanted_urls           # instead of original_anchor_links go with after_removing_unwanted_urls
        else:
            url_to_extract = original_helping_url


        for imp_u in url_to_extract:
            selector = Selector(response)
            node = selector.xpath('//a[@href=' + '\"' + imp_u + '\"' + ']')
            parent = node.xpath('..')
            # I want only child elements  -> so that in future if i want to add all sub elements to individual child
            children = parent.xpath('*').extract()  # matches only child elements

            # -----> dictionary to store child tags 
            child_tags = dict()
            for chi in children:
                child_tags[chi] = []


            text_child = []
            image_child = []
            href_child = []
            date_time_child = []
            # indv_tag is just to identify the tag
            indv_tag = []
            for ch in children:
                
                sel = Selector(text = ch)
                # all sub elements to join main child
                all_sub = sel.xpath('//*')  # matches all elements

                indivisible = sel.xpath('//*[not(*)]')

                indivisible.extract()

                for i in indivisible:
                    i.extract()
                # text = indivisible.xpath('text()').extract()

                # removing tags which does not having image or href or datetime or text
                modified_indivisible = []
                for ind in indivisible:
                    tag_info = ind.extract()

                    if 'src' in tag_info or  'href' in tag_info or 'datetime' in tag_info or ind.xpath('text()').extract_first() != None:
                        modified_indivisible.append(ind)


                
                for indv in modified_indivisible:
                    tag_info = indv.extract()

                    if 'src' in tag_info:                           # for finding images
                        image = indv.xpath('@src').extract_first()        
                    else:
                        image = ''

                    if 'href' in tag_info:                          # for finding href(anchor tag)
                        href = indv.xpath('@href').extract_first()
                    else:
                        href = ''

                    if 'datetime' in tag_info:                      # for finding datetime
                        datetime = indv.xpath('@datetime').extract_first()
                    else :
                        datetime = ''

                    text = indv.xpath('text()').extract_first()
                    text = text.strip() if text != None else text

                    # to return indivisible data   **csv is prefered**                  (when require)          here is changing for individual tags
                    # yield{
                    #     'indivisible tag' : indv.extract(),
                    #     'text' : text,
                    #     'image' : image,
                    #     'href' : href,
                    #     'datetime' : datetime,
                    #     'urls' : imp_u
                    # }

                    # we are in indivisible child tags going back to main child where we are getting urls
                    

                    # adding data
                    text_child.append(text)
                    image_child.append(image)
                    href_child.append(href)
                    date_time_child.append(datetime)
                    # the below is just to identify the tag
                    indv_tag.append(indv.extract())
            
                # to return direct child data        **json is prefered**                           (when require)             here is changing for child tags
            
            # yield {
            #     'url' : imp_u,
            #     'indivisible tag' : indv_tag,
            #     'text_child' : text_child,
            #     'image_child' : image_child,
            #     'href_child' : href_child,
            #     'date_time_child' : date_time_child
            # }
            
            # removing duplicates
            text_child = [value for i, value in enumerate(text_child) if value not in text_child[:i]]
            image_child = [value for i, value in enumerate(image_child) if value not in image_child[:i]]
            href_child = [value for i, value in enumerate(href_child) if value not in href_child[:i]]
            date_time_child = [value for i, value in enumerate(date_time_child) if value not in date_time_child[:i]]
            indv_tag = [value for i, value in enumerate(indv_tag) if value not in indv_tag[:i]]

                                                # ---------making lists of same length ------------------------- #
            # max_child = max(len(text_child),
            #                 len(image_child),
            #                 len(href_child),
            #                 len(date_time_child),
            #                 len(indv_tag))
            
            # if len(text_child) == max_child:
            #     image_child.extend(['']*(max_child-len(image_child)))
            #     href_child.extend(['']*(max_child-len(href_child)))
            #     date_time_child.extend(['']*(max_child-len(date_time_child)))
            #     indv_tag.extend(['']*(max_child-len(indv_tag)))

            # if len(image_child) == max_child:
            #     text_child.extend(['']*(max_child-len(text_child)))
            #     href_child.extend(['']*(max_child-len(href_child)))
            #     date_time_child.extend(['']*(max_child-len(date_time_child)))
            #     indv_tag.extend(['']*(max_child-len(indv_tag)))
            
            # if len(href_child) == max_child:
            #     text_child.extend(['']*(max_child-len(text_child)))
            #     image_child.extend(['']*(max_child-len(image_child)))
            #     date_time_child.extend(['']*(max_child-len(date_time_child)))
            #     indv_tag.extend(['']*(max_child-len(indv_tag)))

            # if len(date_time_child) == max_child:
            #     text_child.extend(['']*(max_child-len(text_child)))
            #     image_child.extend(['']*(max_child-len(image_child)))
            #     href_child.extend(['']*(max_child-len(href_child)))
            #     indv_tag.extend(['']*(max_child-len(indv_tag)))

            # if len(indv_tag) == max_child:
            #     text_child.extend(['']*(max_child-len(text_child)))
            #     image_child.extend(['']*(max_child-len(image_child)))
            #     href_child.extend(['']*(max_child-len(href_child)))
            #     date_time_child.extend(['']*(max_child-len(date_time_child)))

                                                                # ---------making lists of same length ------------------------- #

                                    # ------------------- combining all child tags into single individual lists for text, image, href, etc ---------------------------------------
            all_text_child.append(text_child)
            all_image_child.append(image_child)
            all_href_child.append(href_child)
            all_date_time_child.append(date_time_child)
            all_indv_tag.append(indv_tag)

                                        # ----------------------making a dictionary from all single entities of text, image, href etc--------------------
        child_dict = {'text child': all_text_child,
                        'image child': all_image_child,
                        'href child': all_href_child,
                        'date_time child': all_date_time_child,
                        'indv_tag': all_indv_tag
                        }
                                        # converting the dict to pandas dataframe 
        
        child_df = pandas.DataFrame(child_dict)
        # child_df['url'] = url_to_extract          instead of directly giving it like this we can check elements having base url or not

        child_df['url'] = [base_url + url if url.startswith("/") else url for url in url_to_extract]
        print(child_df)
                                        # saving the dataframe as csv file

        # child_df.to_csv('E:\\scrapy project\\for_text\\for_text\\df.csv', index = True)
        # print(text_child)


            
                                        # total data as single lists 
        # yield{'text child': all_text_child,
        #     'image child': all_image_child,
        #     'href child': all_href_child,
        #     'date_time child': all_date_time_child,
        #     'indv_tag': all_indv_tag,
        #     'url': url_to_extract
        #     }
                                                # to understand the urls lists
        # yield{
        #     'original' : original_anchor_links,
        #     'urls list with pattern' : original_helping_url, # urls list with pattern
        #     'modified' : url_to_extract, # by using this we are extracting if pattern is not present
        #     'after removing unwanted urls' : after_removing_unwanted_urls
        # }
                
        # yield{
        #     'original anchor links ': original_anchor_links,
            # 'base anchor links ' : base_anchor_links,
            # 'important url' : imp_urls,
            # 'com list' : com_list,
            # 'non com list' : non_com_list,
            # 'pattern list' : pattern_list,
            # 'l' : l,
            # 'original helping url' : original_helping_url
        # }
        # for i in url_to_extract:
        #     yield response.follow(i, self.parse_url)

                                                            # with url going to next page and extracting the content
        # yield response.follow(child_df['url'][6], self.parse_url)
    def parse_url(self, response):
        t = response.xpath("//*[self::h1 or self::h2 or self::h3 or self::h4 or self::h5 or self::h6 or self::p or self::ul or self::ol or self::li or self::strong or self::em]/text()").extract()
        # need to be added 'strong', 'em'
        modified_t = [i for i in t if i.strip() != '']
        yield { 'url': response.url,
            'total text ' : modified_t}



# 2 major things keep in mind in this program 
# 1. extracting next page data
# 2. saving csv file          for that matter dataframe is also no need