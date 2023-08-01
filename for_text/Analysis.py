from pandas import DataFrame
class Make_data_frame:
    def create_data_frame(self, all_text_child, all_image_child, all_href_child, all_date_time_child, all_indv_tag, base_url, url_to_extract):
        child_dict = {'text child': all_text_child,
                            'image child': all_image_child,
                            'href child': all_href_child,
                            'date_time child': all_date_time_child,
                            'indv_tag': all_indv_tag
                            }
                # converting the dict to pandas dataframe 
            
        child_df = DataFrame(child_dict)
        # child_df['url'] = url_to_extract          instead of directly giving it like this we can check elements having base url or not

        child_df['url'] = [base_url + url if url.startswith("/") else url for url in url_to_extract]
        
        # print(child_df)

                                        # saving the dataframe as csv file

        child_df.to_csv('E:\\scrapy project\\for_text\\for_text\\df.csv', index = True)
        # print(text_child)