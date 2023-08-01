import scrapy
import re
from scrapy import Selector
from collections import Counter
# Counter used to count the occurrences of elements in an iterable or a sequence.
import pandas


# user defined modules
from all_domains import Domain
from data_extraction import Data
from delivery import Structure_images_urls
from user_interest import User_interest
from single_page import Single, Element_wise, All_in_one, Get_indivisible
from Analysis import Make_data_frame

class TextSpider(scrapy.Spider):
    name = "text"
    # allowed_domains = ["text.com"]
    start_urls = [input('enter url to extract text : ')]

    def parse(self, response):
        
        user_interest_for_single_multiple = User_interest()
        single_or_multiple_response = user_interest_for_single_multiple.single_or_multiple()

        print('\n\nuser interest is : ', single_or_multiple_response)
        if single_or_multiple_response == 1:
            single_obj = Single(response, self.start_urls[0])
            yield single_obj.extract_from_single_page()
            return 0
        elif single_or_multiple_response == 2:
            print('\n\n user wants multiple\n\n')

            # The below is to take input of user on multiple data getting
            user_on_multiple_obj = User_interest()
            user_response_on_multiple = user_on_multiple_obj.what_on_multiple_data()
            print(user_response_on_multiple)


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

            # getting the user interest of wanting absolute data or relative data
            user_interest_obj = User_interest()
            extraction_choice_of_user = user_interest_obj.get_absolute_or_relative()
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
            # defined_urls_to_remove = ['facebook.com', 'twitter.com', '/privacy/', '/contact/', '/contribute/', '/about/', '/getting-started/']
            # the below logic is to achieve the above thing
            with open('E:\\scrapy project\\for_text\\for_text\\config_text_files\\unnecessary_links.txt', 'r') as unnecessary_links_file:
                read_unnecessary_file = unnecessary_links_file.read()
                defined_urls_to_remove = read_unnecessary_file.split(', ')

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

                        indivisible_tag = indv.extract()

                        # to return indivisible data   **csv is prefered**                  (when require)          here is changing for individual tags


                        # The below is to get indivisible tags which are containing mostly of tags of unstructured
                        if user_response_on_multiple == 2:
                            get_indivisible_obj = Get_indivisible()
                            yield get_indivisible_obj.get_indivisible(indivisible_tag, text, image, href, datetime, imp_u)

                        
                        # getting multiple repeated data because of the fact that it is insider of 3 loops

                        # we are in indivisible child tags going back to main child where we are getting urls
                        
                        # adding data
                        text_child.append(text)
                        image_child.append(image)
                        href_child.append(href)
                        date_time_child.append(datetime)
                        # the below is just to identify the tag
                        indv_tag.append(indv.extract())

                        # to make urls and images workable we will make them structure by adding base url
                        # for that class Structure_image_url will help

                        image_url_obj = Structure_images_urls(base_url)
                        image_url_obj.make_images_structured(image_child)
                        image_url_obj.make_urls_structured(href_child)


                
                    # to return direct child data        **json is prefered**                           (when require)             here is changing for child tags
                    # I think the below one is might be the final as it can give the result for the individual data
                    # final below
                if user_response_on_multiple == 1:
                    all_data_obj = Element_wise()
                    yield all_data_obj.all_data_element_wise(imp_u, indv_tag, text_child, image_child, href_child, date_time_child)
                
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
                    # creating data frame by following calls
            create_data_frame = Make_data_frame()
            create_data_frame.create_data_frame(all_text_child, all_image_child, all_href_child, all_date_time_child, all_indv_tag, base_url, url_to_extract)
            
                
                                            # total data as single lists 
                                            # json is prefered

            # The below calls for all in one data
            if user_response_on_multiple == 3:
                all_in_one_obj = All_in_one()
                yield all_in_one_obj.get_all_in_one(all_text_child, all_image_child, all_href_child, all_date_time_child, all_indv_tag, url_to_extract)
            
            
        
            # function to extract complete text
            # def complete_text_fun(response, url_to_extract):
            #     for i in url_to_extract:
            #         yield response.follow(i, self.parse_url)
            # return complete_text_fun(response, url_to_extract)
                
            # The below one only working
            if user_response_on_multiple == 4:
                for i in url_to_extract:
                    yield response.follow(i, self.parse_url)

            # calls for getting text from multiple urls
            # traveling_each_url_for_text = Travel_on_each_url(response, url_to_extract)
            # from_mul_text =  traveling_each_url_for_text.multiple_url_text_extraction(response)
            # yield from_mul_text

    def parse_url(self, response):
        t = response.xpath("//*[self::h1 or self::h2 or self::h3 or self::h4 or self::h5 or self::h6 or self::p or self::ul or self::ol or self::li or self::strong or self::em]/text()").extract()
        # # need to be added 'strong', 'em'
        modified_t = [i for i in t if i.strip() != '']
        yield { 'url': response.url,
            'total text ' : modified_t}
