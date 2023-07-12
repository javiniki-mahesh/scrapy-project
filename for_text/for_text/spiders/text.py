import scrapy
import re
from scrapy import Selector
from collections import Counter
# Counter used to count the occurrences of elements in an iterable or a sequence.
import pandas


# user defined modules
from all_domains import Domain
from data_extraction import Data

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
        # print("All links : \n",\
        #       original_anchor_links, len(original_anchor_links),sep = '\n\n')

        # getting body urls
        # original_anchor_links = response.xpath("//body//a/@href").getall()

        # get only unique urls
        original_anchor_links = [value for i, value in enumerate(original_anchor_links) if value not in original_anchor_links[:i]]

        # print("\n\nAfter modification unique links : \n\n",\
        #       original_anchor_links, len(original_anchor_links),sep = '\n\n')

        # finding .com for .com domains
        # s = self.start_urls[0]
        # base_url = s[:s.index('.com')+4]

        # finding base_url using OOP classes
        domain_obj = Domain(self.start_urls[0])
        base_url = domain_obj.logic_for_domains()

        print(f'printing the base url after traveling though OOPs: {base_url}')

        # for base_anchor_links adding meaningful urls
        # some links may not start with https://domain the following logic will fix that
        base_anchor_links = [] # anchor links with base or domain
        for anchor in original_anchor_links:
            if anchor.startswith('/'):
                base_anchor_links.append(base_url + anchor)
            else:
                base_anchor_links.append(anchor)

        # print("Base anchor links : \n", base_anchor_links,'\n\n')

        pattern = r'\.com\/(.*?)\/'
        com_pattern = r'\.com\/(.*?)\/'
        # the regular expression r'\.com\/(.*?)\/' is designed to match a string that starts with ".com/" and captures the substring between the first and second forward slashes after ".com/".
        non_com_pattern = r'\/(.*?)\/'
        # we have removed the specific requirement of ".com" at the beginning of the string.


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
        
        # print('com patterns : \n\n', com_list)
        # print('\n\nnon com :\n\n',non_com_list)
        # print('\n\npattern: \n\n', pattern_list)


        counts = Counter(pattern_list)
        
        # the below is by taking the single pattern
        max_value = counts.most_common(1)[0]
        max_occur_patten = max_value[0]
        # for this time we are going with many as below logic

        # print('counts:\n\n', counts)
        # print('max value:\n\n', max_value)
        # print(max_value[0])                           
        # here max_value[0] we are getting the max value which is used further
        

        # single may not be able to cover many things for that reason we will go with by following logic to include as many as meaningful
        sorted_dict_patterns = dict(sorted(counts.items(), key = lambda value: value[1], reverse = True)) # sorting data by value

        url_pattern_to_extract = [] # pattern list which we need to extract
        for key, value in sorted_dict_patterns.items(): # iterating through key, value
            if value >= 5: # setting the threshold to select the pattern
                url_pattern_to_extract.append(key)

        # the following is the soul of whole

        # through maximum occurred pattern we are creating a list of links by which we are moving forward
        # if any content is missing while scrapping the following plays major role 
        # till now focusing only one pattern
        # we can modify the following code for better scraping in the next level

        # def absolute_data(original_anchor_links, url_pattern_to_extract):
        #     """This function will return all possible combinations from given website"""
        #     original_helping_url = []
        #     for link in original_anchor_links:  # I think base_anchor_links should present instead original_anchor_links  -----> changed ---> rechanged to original_anchor_links for XPath we need only part of url not complete
        #         for patt in url_pattern_to_extract:
        #             if '/' + patt in link:          # checking only '/category' values            # better to keep an eye
        #                 if link.startswith('/' + patt) or link.startswith(base_url + '/' + patt):
        #                     # above line is very important for segregating the urls by first category
        #                     original_helping_url.append(link)
        #     return original_helping_url

        # def relative_data(original_anchor_links, max_occur_patten):
        #     """This function will return maximum repeated combination from given website"""
        #     original_helping_url = []
        #     for link in original_anchor_links:  # I think base_anchor_links should present instead original_anchor_links  -----> changed ---> rechanged to original_anchor_links for XPath we need only part of url not complete
        #         if '/' + max_occur_patten in link:          # checking only '/category' values            # better to keep an eye
        #             if link.startswith('/' + max_occur_patten) or link.startswith(base_url + '/' + max_occur_patten):
        #                 # above line is very important for segregating the urls by first category
        #                 original_helping_url.append(link)
        #     return original_helping_url
        
        extraction_choice_of_user = input("Enter abs if you want extract absolute data\n \
                                          Enter rel if you want to extract relative data : ")
        data_obj = Data(original_anchor_links, base_url)
        if extraction_choice_of_user == 'abs':
            original_helping_url = data_obj.absolute_data(url_pattern_to_extract)
        else:
            original_helping_url = data_obj.relative_data(max_occur_patten)

        # print("original helping urls : \n\n", original_helping_url)

        
        # original_helping_url = []
        # for link in original_anchor_links:  # I think base_anchor_links should present instead original_anchor_links  -----> changed ---> rechanged to original_anchor_links for XPath we need only part of url not complete
        #     for patt in url_pattern_to_extract:
        #         if '/' + patt in link:          # checking only '/category' values            # better to keep an eye
        #             if link.startswith('/' + patt) or link.startswith(base_url + '/' + patt):
        #                 # above line is very important for segregating the urls by first category
        #                 original_helping_url.append(link)

        # made above logic modular


        # Edge cases (from above logic)
        # if we haven't find the pattern which contains in many urls in links ---> doesn't do good job
        # the patten should present only beginning of url or immediately after base url
        
        
        # if there are significant number of patterns present we can add more patterns/categories to it
                    # ----> in the above case we can expect good result
        # print('Helping urls: \n\n\n',original_helping_url)

        # original helping_urls does not cover base_url edge case
#---------------------------------------------------
## till here getting helping urls to extract data
        
        l = []
        for link in base_anchor_links:
            result = re.findall(pattern, link)
            if len(result) >=1:
                l.append(result[0])
        # print('l :\n\n', l)
        # from collections import Counter

        # Count the occurences of each value
        counts = Counter(l)

        # Get the value that has the highest count
        max_value = counts.most_common(1)[0]

        imp_urls = []
        for i in base_anchor_links:
            if max_value[0] in i:
                imp_urls.append(i)
        # print('imp urls: \n\n\n',imp_urls)
#----------------------------------------->these imp_urls haven't used anywhere once more analyze and remove if unnecessary
# till here to get imp urls

        # little summary feels like imp_urls and original_helping_url having same moto
        # print('length of original hilping urls :\n',len(original_helping_url))
        # print('\nlength of imp urls : \n',len(imp_urls))


        # blogs lirqs
        # passing anchor links as they got  -----
        # for imp_u in imp_urls:

                                               # based on no.of elements in helping urls we decide which urls list is used to extract data
                                               # defining unwanted urls
        defined_urls_to_remove = ['facebook.com', 'twitter.com', '/privacy/', '/contact/', '/contribute/', '/about/', '/getting-started/']
                                                # removing unwanted urls
        after_removing_unwanted_urls = [x for x in original_anchor_links if not any(y in x for y in defined_urls_to_remove)]  # ok (statement is good)
        if len(original_helping_url) < 11:
            # the above condition can be changes based on the counter pattern by some specific pattern
            url_to_extract = after_removing_unwanted_urls           # instead of original_anchor_links go with after_removing_unwanted_urls
        else:
            url_to_extract = original_helping_url

        # print('urls to extract : \n\n', url_to_extract)
        
        for imp_u in url_to_extract:
            selector = Selector(response)
            # Selector(response) creates a Selector object that allows you to extract data from the web page using CSS or XPath selectors.

            node = selector.xpath('//a[@href=' + '\"' + imp_u + '\"' + ']')
            # + '\"' + imp_u + '\"' + ']'): This part of the expression concatenates the value of the imp_u variable into the XPath query.

            parent = node.xpath('..')
            # The '..' expression in XPath refers to the parent node of the current node. It selects the direct parent node of the current node.

            # I want only child elements  -> so that in future if i want to add all sub elements to individual child
            children = parent.xpath('*').extract()  # matches only child elements
            # children = parent.xpath('*').extract() is used to extract the HTML or text content of all child elements of the parent element using XPath.
            
            # -----> dictionary to store child tags 
            child_tags = dict()
            for chi in children:
                child_tags[chi] = []
            
            # I think above peace of code hasn't used anywhere


            text_child = []
            image_child = []
            href_child = []
            date_time_child = []
            # indv_tag is just to identify the tag
            indv_tag = []
            for ch in children:
                
                sel = Selector(text = ch)
                # text=ch: This is a keyword argument passed to the Selector constructor. It specifies the ch string as the input content for the selector object.

                # all sub elements to join main child
                all_sub = sel.xpath('//*')  # matches all elements
                # After creating the Selector object sel, the expression sel.xpath('//*') is used to select all elements in the HTML document.


                indivisible = sel.xpath('//*[not(*)]')
                # The //*[not(*)] expression selects all elements in the document that do not have any child elements.

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
                    # getting multiple repeated data because of the fact that it is insider of 3 loops

                    # we are in indivisible child tags going back to main child where we are getting urls
                    
                    # adding data
                    text_child.append(text)
                    image_child.append(image)
                    href_child.append(href)
                    date_time_child.append(datetime)
                    # the below is just to identify the tag
                    indv_tag.append(indv.extract())
            
                # to return direct child data        **json is prefered**                           (when require)             here is changing for child tags
                # I think the below one is might be the final as it can give the result for the individual data
                # final below
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
        
        # print(child_df)

                                        # saving the dataframe as csv file

        child_df.to_csv('E:\\scrapy project\\for_text\\for_text\\df.csv', index = True)
        # print(text_child)
            
                                        # total data as single lists 
                                        # json is prefered
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
        #     'base anchor links ' : base_anchor_links,
        #     'important url' : imp_urls,
        #     'com list' : com_list,
        #     'non com list' : non_com_list,
        #     'pattern list' : pattern_list,
        #     'l' : l,
        #     'original helping url' : original_helping_url
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