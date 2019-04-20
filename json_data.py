 json_data_ product=  
 [    {
               "product_id":"edf4a46d-6679-4fb8-bc00-fb352e59d918",
            	"variant_id":"41",
                "quantity":"7"
            },
            {
               "product_id":"edf4a46d-6679-4fb8-bc00-fb352e59d918",
                "variant_id":"72",
                "quantity":"7"
            }
       ]
 json_data_variant=  [    {
               "product_id":"edf4a46d-6679-4fb8-bc00-fb352e59d918",
            	"variant_id":"11",
                "quantity":"7"
            },
            {
               "product_id":"edf4a46d-6679-4fb8-bc00-fb352e59d918",
                "variant_id":"12",
                "quantity":"7"
            }
       ]
        
 json_data = json_data_product + json_data_variant # add two list 

 #json_data = sorted(json_data,key=itemgetter('variant_id'),reverse=True) 
 json_data = sorted(json_data, key=lambda k: k['variant_id'])
 print(json_data)
