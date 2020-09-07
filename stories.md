## complete path 
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "agra"}
    - slot{"location": "agra"}
    - action_verify_location
    - slot{"location": "agra"}
    - slot{"valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - utter_ask_budget
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - action_check_budget
    - slot{"minbudget": 0}
    - slot{"maxbudget":300} 
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* affirm
    - utter_ask_emailid
* send_email{"emailid": "qwerty.123@yahoo.co.in"}
    - slot{"emailid": "qwerty.123@yahoo.co.in"}
    - action_send_email
* affirm
    - utter_goodbye
    - export
    - action_restart

## complete path with email
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "agra"}
    - slot{"location": "agra"}
    - action_verify_location
    - slot{"location": "agra"}
    - slot{"valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - utter_ask_budget
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - action_check_budget
    - slot{"minbudget": 0}
    - slot{"maxbudget":300} 
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* send_email{"emailid": "hellobot@gmail.com"}
    - slot{"emailid": "hellobot@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye
    - export
    - action_restart
    
    
## complete path wrong location
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "moga"}
    - slot{"location": "moga"}
    - action_verify_location
    - slot{"location": null}
    - slot{"valid_location": false}
    - utter_city_not_found
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_verify_location
    - slot{"location": "delhi"}
    - slot{"valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - utter_ask_budget
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - action_check_budget
    - slot{"minbudget": 0}
    - slot{"maxbudget":300} 
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* affirm
    - utter_ask_emailid
* send_email{"emailid": "hellobot@gmail.com"}
    - slot{"emailid": "hellobot@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye
    - export
    - action_restart


## complete path wrong cuisine
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "amritsar"}
    - slot{"location": "amritsar"}
    - action_verify_location
    - slot{"location": "amritsar"}
    - slot{"valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "british"}
    - slot{"cuisine": "british"}
    - action_verify_cuisine
    - slot{"valid_cuisine": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - utter_ask_budget
* restaurant_search{"price": "Rs.300 to 700"}
    - slot{"price": "Rs.300 to 700"}
    - action_check_budget
    - slot{"minbudget": 0}
    - slot{"maxbudget":300} 
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* affirm
    - utter_ask_emailid
* send_email{"emailid": "lkjhgst_asdf@yebh.com"}
    - slot{"emailid": "lkjhgst_asdf@yebh.com"}
    - action_send_email
* affirm
    - utter_goodbye
    - export
    - action_restart


## complete path wrong price range
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - action_verify_location
    - slot{"location": "bengaluru"}
    - slot{"valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - utter_ask_budget
* restaurant_search{"price": "Less than Rs.500"}
    - slot{"price": "Less than Rs.500"}
    - action_check_budget
    - slot{"minbudget": 0}
    - slot{"maxbudget":10000} 
    - slot{"valid_budget_range": false}
    - utter_ask_budget
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - action_check_budget
    - slot{"minbudget":0}
    - slot{"maxbudget":300}
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* affirm
    - utter_ask_emailid
* send_email{"emailid": "hellobot@gmail.com"}
    - slot{"emailid": "hellobot@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye
    - export
    - action_restart


## complete path no resultsfound
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_verify_location
    - slot{"location": "pune"}
    - slot{"valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - utter_ask_budget
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - action_check_budget
    - slot{"minbudget": 0}
    - slot{"maxbudget":300} 
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": false}
* affirm
    - utter_goodbye
    - export
    - action_restart


## complete path deny email
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bokaro"}
    - slot{"location": "bokaro"}
    - action_verify_location
    - slot{"location": "bokaro"}
    - slot{"valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - utter_ask_budget
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - action_check_budget
    - slot{"minbudget": 0}
    - slot{"maxbudget":300} 
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* deny
    - utter_goodbye
    - export
    - action_restart


## happy_path
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian", "location": "kolkata", "price":"More than Rs.700"}
    - slot{"cuisine": "south indian"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - slot{"location": "kolkata"}
    - action_verify_location
    - slot{"location": "kolkata"}
    - slot{"valid_location": true}  
    - slot{"price":"More than Rs.700"}
    - action_check_budget
    - slot{"minbudget":700}
    - slot{"maxbudget":10000} 
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* affirm
    - utter_ask_emailid
* send_email{"emailid": "jeena.89@gmail.com"}
    - slot{"emailid": "jeena.89@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye
    - export
    - action_restart
## happy_path no resultsfound
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian", "location": "kolkata", "price":"More than Rs.700"}
    - slot{"cuisine": "south indian"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - slot{"location": "kolkata"}
    - action_verify_location
    - slot{"location": "kolkata"}
    - slot{"valid_location": true}  
    - slot{"price":"More than Rs.700"}
    - action_check_budget
    - slot{"minbudget":700}
    - slot{"maxbudget":10000} 
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": false}
* affirm
    - utter_goodbye
    - export
    - action_restart

## happy_path deny email
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian", "location": "goa", "price":"Rs.300 to 700"}
    - slot{"cuisine": "south indian"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - slot{"location": "goa"}
    - action_verify_location
    - slot{"location": "goa"}
    - slot{"valid_location": true}  
    - slot{"price":"Rs.300 to 700"}
    - action_check_budget
    - slot{"minbudget":300}
    - slot{"maxbudget":700} 
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* deny
    - utter_goodbye
    - export
    - action_restart

## location specified correct location
* greet
    - utter_greet
* restaurant_search{"location": "durgapur"}
    - slot{"location": "durgapur"}
    - action_verify_location
    - slot{"location": "durgapur"}
    - slot{"valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - utter_ask_budget
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - action_check_budget
    - slot{"minbudget": 0}
    - slot{"maxbudget":300} 
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* affirm
    - utter_ask_emailid
* send_email{"emailid": "hellobot@gmail.com"}
    - slot{"emailid": "hellobot@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye
    - export
    - action_restart


## location specified wrong location
* greet
    - utter_greet
* restaurant_search{"location": "firozpur"}
    - slot{"location": "firozpur"}
    - action_verify_location
    - slot{"location": null}
    - slot{"valid_location": false}
    - utter_city_not_found
* restaurant_search{"location": "dhanbad"}
    - slot{"location": "dhanbad"}
    - action_verify_location
    - slot{"location": "dhanbad"}
    - slot{"valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - action_check_budget
    - slot{"minbudget":700}
    - slot{"maxbudget":10000} 
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* affirm
    - utter_ask_emailid
* send_email{"emailid": "hellobot@gmail.com"}
    - slot{"emailid": "hellobot@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye
    - export
    - action_restart

## location specified wrong cuisine
* greet
    - utter_greet
* restaurant_search{"location": "durgapur"}
    - slot{"location": "durgapur"}
    - action_verify_location
    - slot{"location": "durgapur"}
    - slot{"valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "continental"}
    - slot{"cuisine": "continental"}
    - action_verify_cuisine
    - slot{"valid_cuisine": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - utter_ask_budget
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - action_check_budget
    - slot{"minbudget": 0}
    - slot{"maxbudget":300} 
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* affirm
    - utter_ask_emailid
* send_email{"emailid": "hellobot@gmail.com"}
    - slot{"emailid": "hellobot@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye
    - export
    - action_restart

## location specified wrong price range
* greet
    - utter_greet
* restaurant_search{"location": "chandigarh"}
    - slot{"location": "chandigarh"}
    - action_verify_location
    - slot{"location": "chandigarh"}
    - slot{"valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - utter_ask_budget
* restaurant_search{"price": "300 to 900"}
    - slot{"price": "300 to 900"}
    - action_check_budget
    - slot{"minbudget":0}
    - slot{"maxbudget":10000} 
    - slot{"valid_budget_range": false}
    - utter_ask_budget
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - action_check_budget
    - slot{"minbudget": 0}
    - slot{"maxbudget":300} 
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* affirm
    - utter_ask_emailid
* send_email{"emailid": "hellobot@gmail.com"}
    - slot{"emailid": "hellobot@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye
    - export
    - action_restart


## location specified no resultsfound
* greet
    - utter_greet
* restaurant_search{"location": "durgapur"}
    - slot{"location": "durgapur"}
    - action_verify_location
    - slot{"location": "durgapur"}
    - slot{"valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - utter_ask_budget
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - action_check_budget
    - slot{"minbudget": 0}
    - slot{"maxbudget":300} 
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": false}
* affirm
    - utter_goodbye
    - export
    - action_restart


## location specified deny email
* greet
    - utter_greet
* restaurant_search{"location": "durgapur"}
    - slot{"location": "durgapur"}
    - action_verify_location
    - slot{"location": "durgapur"}
    - slot{"valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - utter_ask_budget
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - action_check_budget
    - slot{"minbudget": 0}
    - slot{"maxbudget":300} 
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* deny
    - utter_goodbye
    - export
    - action_restart


## cuisine specified
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - utter_ask_location
* restaurant_search{"location": "faridabad"}
    - slot{"location": "faridabad"}
    - action_verify_location
    - slot{"location": "faridabad"}
    - slot{"valid_location": true}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - action_check_budget
    - slot{"minbudget":700}
    - slot{"maxbudget":10000} 
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* affirm
    - utter_ask_emailid
* send_email{"emailid": "hellobot@gmail.com"}
    - slot{"emailid": "hellobot@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye
    - export
    - action_restart


## cuisine specified wrong cuisine
* greet
    - utter_greet
* restaurant_search{"cuisine": "japanese"}
    - slot{"cuisine": "japanese"}
    - action_verify_cuisine
    - slot{"valid_cuisine": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - utter_ask_location
* restaurant_search{"location": "ghaziabad"}
    - slot{"location": "ghaziabad"}
    - action_verify_location
    - slot{"location": "ghaziabad"}
    - slot{"valid_location": true}
    - utter_ask_budget
* restaurant_search{"price": "Rs.300 to 700"}
    - slot{"price": "Rs.300 to 700"}
    - action_check_budget
    - slot{"minbudget":300}
    - slot{"maxbudget":700} 
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* affirm
    - utter_ask_emailid
* send_email{"emailid": "hellobot@gmail.com"}
    - slot{"emailid": "hellobot@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye
    - export
    - action_restart



## cuisine specified wrong location
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - utter_ask_location
* restaurant_search{"location": "tezpur"}
    - slot{"location": "tezpur"}
    - action_verify_location
    - slot{"location": null}
    - slot{"valid_location": false}
    - utter_city_not_found
* restaurant_search{"location": "cuttack"}
    - slot{"location": "cuttack"}
    - action_verify_location
    - slot{"location": "cuttack"}
    - slot{"valid_location": true}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - action_check_budget
    - slot{"minbudget":700}
    - slot{"maxbudget":10000} 
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* affirm
    - utter_ask_emailid
* send_email{"emailid": "hellobot@gmail.com"}
    - slot{"emailid": "hellobot@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye
    - export
    - action_restart


## cuisine specified wrong price range
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - utter_ask_location
* restaurant_search{"location": "faridabad"}
    - slot{"location": "faridabad"}
    - action_verify_location
    - slot{"location": "faridabad"}
    - slot{"valid_location": true}
    - utter_ask_budget
* restaurant_search{"price": "500 to 1000"}
    - slot{"price": "300 to 900"}
    - action_check_budget
    - slot{"minbudget":0}
    - slot{"maxbudget":10000} 
    - slot{"valid_budget_range": false}
    - utter_ask_budget
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - action_check_budget
    - slot{"minbudget": 0}
    - slot{"maxbudget":300} 
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* affirm
    - utter_ask_emailid
* send_email{"emailid": "hellobot@gmail.com"}
    - slot{"emailid": "hellobot@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye
    - export
    - action_restart

## cuisine specified no resultsfound
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - utter_ask_location
* restaurant_search{"location": "jhansi"}
    - slot{"location": "jhansi"}
    - action_verify_location
    - slot{"location": "jhansi"}
    - slot{"valid_location": true}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - action_check_budget
    - slot{"minbudget":700}
    - slot{"maxbudget":10000} 
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": false}
* affirm
    - utter_goodbye
    - export
    - action_restart
    

## cuisine specified deny email
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - utter_ask_location
* restaurant_search{"location": "faridabad"}
    - slot{"location": "faridabad"}
    - action_verify_location
    - slot{"location": "faridabad"}
    - slot{"valid_location": true}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - action_check_budget
    - slot{"minbudget":700}
    - slot{"maxbudget":10000} 
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* deny
    - utter_goodbye
    - export
    - action_restart
    

## price specified 
* greet
    - utter_greet
* restaurant_search{"price": "Rs.300 to 700"}
    - slot{"price": "Rs.300 to 700"}
    - action_check_budget
    - slot{"minbudget":300}
    - slot{"maxbudget":700} 
    - slot{"valid_budget_range": true}
    - utter_ask_location
* restaurant_search{"location": "mathura"}
    - slot{"location": "mathura"}
    - action_verify_location
    - slot{"location": "mathura"}
    - slot{"valid_location": true}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* affirm
    - utter_ask_emailid
* send_email{"emailid": "hellobot@gmail.com"}
    - slot{"emailid": "hellobot@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye
    - export
    - action_restart
    
    
## price specified wrong price range
* greet
    - utter_greet
* restaurant_search{"price": "800 to 2000"}
    - slot{"price": "800 to 2000"}
    - action_check_budget
    - slot{"minbudget":0}
    - slot{"maxbudget":10000} 
    - slot{"valid_budget_range": false}
    - utter_ask_budget
* restaurant_search{"price": "Rs.300 to 700"}
    - slot{"price": "Rs.300 to 700"}
    - action_check_budget
    - slot{"minbudget":300}
    - slot{"maxbudget":700} 
    - slot{"valid_budget_range": true}
    - utter_ask_location
* restaurant_search{"location": "malappuram"}
    - slot{"location": "malappuram"}
    - action_verify_location
    - slot{"location": "malappuram"}
    - slot{"valid_location": true}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* affirm
    - utter_ask_emailid
* send_email{"emailid": "hellobot@gmail.com"}
    - slot{"emailid": "hellobot@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye
    - export
    - action_restart

    

## price specified wrong location
* greet
    - utter_greet
* restaurant_search{"price": "Rs.300 to 700"}
    - slot{"price": "Rs.300 to 700"}
    - action_check_budget
    - slot{"minbudget":300}
    - slot{"maxbudget":700} 
    - slot{"valid_budget_range": true}
    - utter_ask_location
* restaurant_search{"location": "alwar"}
    - slot{"location": "alwar"}
    - action_verify_location
    - slot{"location": null}
    - slot{"valid_location": false}
    - utter_city_not_found
* restaurant_search{"location": "kanpur"}
    - slot{"location": "kanpur"}
    - action_verify_location
    - slot{"location": "kanpur"}
    - slot{"valid_location": true}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* affirm
    - utter_ask_emailid
* send_email{"emailid": "hellobot@gmail.com"}
    - slot{"emailid": "hellobot@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye
    - export
    - action_restart
    
    
## price specified wrong cuisine
* greet
    - utter_greet
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - action_check_budget
    - slot{"minbudget":700}
    - slot{"maxbudget":10000} 
    - slot{"valid_budget_range": true}
    - utter_ask_location
* restaurant_search{"location": "lucknow"}
    - slot{"location": "lucknow"}
    - action_verify_location
    - slot{"location": "lucknow"}
    - slot{"valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "vegetarian"}
    - slot{"cuisine": "vegetarian"}
    - action_verify_cuisine
    - slot{"valid_cuisine": false}
    - utter_ask_cuisine 
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* affirm
    - utter_ask_emailid
* send_email{"emailid": "hellobot@gmail.com"}
    - slot{"emailid": "hellobot@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye
    - export
    - action_restart

## price specified no resultsfound
* greet
    - utter_greet
* restaurant_search{"price": "Rs.300 to 700"}
    - slot{"price": "Rs.300 to 700"}
    - action_check_budget
    - slot{"minbudget":300}
    - slot{"maxbudget":700} 
    - slot{"valid_budget_range": true}
    - utter_ask_location
* restaurant_search{"location": "mathura"}
    - slot{"location": "mathura"}
    - action_verify_location
    - slot{"location": "mathura"}
    - slot{"valid_location": true}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - action_search_restaurants
    - slot{"resultsfound": false}
* affirm
    - utter_goodbye
    - export
    - action_restart


## price specified deny email
* greet
    - utter_greet
* restaurant_search{"price": "Rs.300 to 700"}
    - slot{"price": "Rs.300 to 700"}
    - action_check_budget
    - slot{"minbudget":300}
    - slot{"maxbudget":700} 
    - slot{"valid_budget_range": true}
    - utter_ask_location
* restaurant_search{"location": "mathura"}
    - slot{"location": "mathura"}
    - action_verify_location
    - slot{"location": "mathura"}
    - slot{"valid_location": true}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* deny
    - utter_goodbye
    - export
    - action_restart


## location and cuisine specified
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian", "location": "erode"}
    - slot{"cuisine": "south indian"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - slot{"location": "erode"}
    - action_verify_location
    - slot{"location": "erode"}
    - slot{"valid_location": true}
    - utter_ask_budget
* restaurant_search{"price": "Rs.300 to 700"}
    - slot{"price": "Rs.300 to 700"}
    - action_check_budget
    - slot{"minbudget":300}
    - slot{"maxbudget":700} 
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* affirm
    - utter_ask_emailid
* send_email{"emailid": "qwerty.123@yahoo.co.in"}
    - slot{"emailid": "qwerty.123@yahoo.co.in"}
    - action_send_email
* affirm
    - utter_goodbye
    - export
    - action_restart
    
## location and cuisine specified wrong location
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian", "location": "rishikesh"}
    - slot{"cuisine": "south indian"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - slot{"location": "rishikesh"}
    - action_verify_location
    - slot{"location": "null"}
    - slot{"valid_location": false}
* restaurant_search{"location": "jaipur"}
    - slot{"location": "jaipur"}
    - action_verify_location
    - slot{"location": "jaipur"}
    - slot{"valid_location": true}
    - utter_ask_budget
* restaurant_search{"price": "Rs.300 to 700"}
    - slot{"price": "Rs.300 to 700"}
    - action_check_budget
    - slot{"minbudget":300}
    - slot{"maxbudget":700} 
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* affirm
    - utter_ask_emailid
* send_email{"emailid": "qwerty.123@yahoo.co.in"}
    - slot{"emailid": "qwerty.123@yahoo.co.in"}
    - action_send_email
* affirm
    - utter_goodbye
    - export
    - action_restart

## location and cuisine specified no resultsfound
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian", "location": "erode"}
    - slot{"cuisine": "south indian"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - slot{"location": "erode"}
    - action_verify_location
    - slot{"location": "erode"}
    - slot{"valid_location": true}
    - utter_ask_budget
* restaurant_search{"price": "Rs.300 to 700"}
    - slot{"price": "Rs.300 to 700"}
    - action_check_budget
    - slot{"minbudget":300}
    - slot{"maxbudget":700} 
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": false}
* affirm
    - utter_goodbye
    - export
    - action_restart

## location and cuisine specified deny email
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian", "location": "erode"}
    - slot{"cuisine": "south indian"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - slot{"location": "erode"}
    - action_verify_location
    - slot{"location": "erode"}
    - slot{"valid_location": true}
    - utter_ask_budget
* restaurant_search{"price": "Rs.300 to 700"}
    - slot{"price": "Rs.300 to 700"}
    - action_check_budget
    - slot{"minbudget":300}
    - slot{"maxbudget":700} 
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* deny
    - utter_goodbye
    - export
    - action_restart

## location and cuisine specified wrong cuisine
* greet
    - utter_greet
* restaurant_search{"cuisine": "mughlai", "location": "erode"}
    - slot{"cuisine": "mughlai"}
    - slot{"location": "erode"}
    - action_verify_cuisine
    - slot{"valid_cuisine": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - action_verify_location
    - slot{"location": "erode"}
    - slot{"valid_location": true}
    - utter_ask_budget
* restaurant_search{"price": "Rs.300 to 700"}
    - slot{"price": "Rs.300 to 700"}
    - action_check_budget
    - slot{"minbudget":300}
    - slot{"maxbudget":700} 
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* affirm
    - utter_ask_emailid
* send_email{"emailid": "qwerty.123@yahoo.co.in"}
    - slot{"emailid": "qwerty.123@yahoo.co.in"}
    - action_send_email
* affirm
    - utter_goodbye
    - export
    - action_restart


## location and cuisine specified wrong cuisine wrong location
* greet
    - utter_greet
* restaurant_search{"cuisine": "mughlai", "location": "kota"}
    - slot{"cuisine": "mughlai"}
    - slot{"location": "kota"}
    - action_verify_cuisine
    - slot{"valid_cuisine": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - action_verify_location
    - slot{"location": "null"}
    - slot{"valid_location": false}
    - utter_city_not_found
* restaurant_search{"location": "jabalpur"}
    - utter_ask_location
    - slot{"location": "jabalpur"}
    - action_verify_location
    - slot{"location": "jabalpur"}
    - slot{"valid_location": true}  
    - utter_ask_budget
* restaurant_search{"price": "Rs.300 to 700"}
    - slot{"price": "Rs.300 to 700"}
    - action_check_budget
    - slot{"minbudget":300}
    - slot{"maxbudget":700} 
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* affirm
    - utter_ask_emailid
* send_email{"emailid": "qwerty.123@yahoo.co.in"}
    - slot{"emailid": "qwerty.123@yahoo.co.in"}
    - action_send_email
* affirm
    - utter_goodbye
    - export
    - action_restart

## location and cuisine specified wrong cuisine wrong location no resultsfound
* greet
    - utter_greet
* restaurant_search{"cuisine": "mughlai", "location": "kota"}
    - slot{"cuisine": "mughlai"}
    - slot{"location": "kota"}
    - action_verify_cuisine
    - slot{"valid_cuisine": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - action_verify_location
    - slot{"location": "null"}
    - slot{"valid_location": false}
    - utter_city_not_found
* restaurant_search{"location": "jabalpur"}
    - utter_ask_location
    - slot{"location": "jabalpur"}
    - action_verify_location
    - slot{"location": "jabalpur"}
    - slot{"valid_location": true}  
    - utter_ask_budget
* restaurant_search{"price": "Rs.300 to 700"}
    - slot{"price": "Rs.300 to 700"}
    - action_check_budget
    - slot{"minbudget":300}
    - slot{"maxbudget":700} 
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": false}
* affirm
    - utter_goodbye
    - export
    - action_restart


## location and cuisine specified wrong cuisine wrong location deny email
* greet
    - utter_greet
* restaurant_search{"cuisine": "mughlai", "location": "kota"}
    - slot{"cuisine": "mughlai"}
    - slot{"location": "kota"}
    - action_verify_cuisine
    - slot{"valid_cuisine": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - action_verify_location
    - slot{"location": "null"}
    - slot{"valid_location": false}
    - utter_city_not_found
* restaurant_search{"location": "jodhpur"}
    - utter_ask_location
    - slot{"location": "jodhpur"}
    - action_verify_location
    - slot{"location": "jodhpur"}
    - slot{"valid_location": true}  
    - utter_ask_budget
* restaurant_search{"price": "Rs.300 to 700"}
    - slot{"price": "Rs.300 to 700"}
    - action_check_budget
    - slot{"minbudget":300}
    - slot{"maxbudget":700} 
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* deny
    - utter_goodbye
    - export
    - action_restart
    
    
## location and cuisine specified wrong cuisine wrong location wrong price
* greet
    - utter_greet
* restaurant_search{"cuisine": "mughlai", "location": "kota"}
    - slot{"cuisine": "mughlai"}
    - slot{"location": "kota"}
    - action_verify_cuisine
    - slot{"valid_cuisine": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - action_verify_location
    - slot{"location": "null"}
    - slot{"valid_location": false}
    - utter_city_not_found
* restaurant_search{"location": "jabalpur"}
    - utter_ask_location
    - slot{"location": "jabalpur"}
    - action_verify_location
    - slot{"location": "jabalpur"}
    - slot{"valid_location": true}  
    - utter_ask_budget
* restaurant_search{"price": "300 to 900"}
    - slot{"price": "300 to 900"}
    - action_check_budget
    - slot{"minbudget":0}
    - slot{"maxbudget":10000} 
    - slot{"valid_budget_range": false}
    - utter_ask_budget
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - action_check_budget
    - slot{"minbudget": 0}
    - slot{"maxbudget":300} 
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* affirm
    - utter_ask_emailid
* send_email{"emailid": "qwerty.123@yahoo.co.in"}
    - slot{"emailid": "qwerty.123@yahoo.co.in"}
    - action_send_email
* affirm
    - utter_goodbye
    - export
    - action_restart
    
## location and cuisine specified wrong cuisine wrong location wrong price no resultsfound
* greet
    - utter_greet
* restaurant_search{"cuisine": "mughlai", "location": "kota"}
    - slot{"cuisine": "mughlai"}
    - slot{"location": "kota"}
    - action_verify_cuisine
    - slot{"valid_cuisine": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - action_verify_location
    - slot{"location": "null"}
    - slot{"valid_location": false}
    - utter_city_not_found
* restaurant_search{"location": "jabalpur"}
    - utter_ask_location
    - slot{"location": "jabalpur"}
    - action_verify_location
    - slot{"location": "jabalpur"}
    - slot{"valid_location": true}  
    - utter_ask_budget
* restaurant_search{"price": "300 to 900"}
    - slot{"price": "300 to 900"}
    - action_check_budget
    - slot{"minbudget":0}
    - slot{"maxbudget":10000} 
    - slot{"valid_budget_range": false}
    - utter_ask_budget
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - action_check_budget
    - slot{"minbudget": 0}
    - slot{"maxbudget":300} 
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": false}
* affirm
    - utter_goodbye
    - export
    - action_restart
    
    
## location and cuisine specified wrong cuisine wrong location wrong price deny email
* greet
    - utter_greet
* restaurant_search{"cuisine": "mughlai", "location": "gujrat"}
    - slot{"cuisine": "mughlai"}
    - slot{"location": "gujrat"}
    - action_verify_cuisine
    - slot{"valid_cuisine": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - action_verify_location
    - slot{"location": "null"}
    - slot{"valid_location": false}
    - utter_city_not_found
* restaurant_search{"location": "jabalpur"}
    - slot{"location": "jabalpur"}
    - action_verify_location
    - slot{"location": "jabalpur"}
    - slot{"valid_location": true}  
    - utter_ask_budget
* restaurant_search{"price": "300 to 900"}
    - slot{"price": "300 to 900"}
    - action_check_budget
    - slot{"minbudget":0}
    - slot{"maxbudget":10000} 
    - slot{"valid_budget_range": false}
    - utter_ask_budget
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - action_check_budget
    - slot{"minbudget": 0}
    - slot{"maxbudget":300} 
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* deny
    - utter_goodbye
    - export
    - action_restart
    
## price range and cuisine specified
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "price":"Less than Rs.300"}
    - slot{"cuisine": "american"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - slot{"price": "Less than Rs.300"}
    - action_check_budget
    - slot{"minbudget":0}
    - slot{"maxbudget":300} 
    - slot{"valid_budget_range": true}
    - utter_ask_location
* restaurant_search{"location": "jalandhar"}
    - slot{"location": "jalandhar"}
    - action_verify_location
    - slot{"location": "jalandhar"}
    - slot{"valid_location": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* affirm
    - utter_ask_emailid
* send_email{"emailid": "qwerty.123@yahoo.co.in"}
    - slot{"emailid": "qwerty.123@yahoo.co.in"}
    - action_send_email
* affirm
    - utter_goodbye
    - export
    - action_restart    


## price range and cuisine specified no resultsfound
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "price":"Less than Rs.300"}
    - slot{"cuisine": "american"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - slot{"price": "Less than Rs.300"}
    - action_check_budget
    - slot{"minbudget":0}
    - slot{"maxbudget":300} 
    - slot{"valid_budget_range": true}
    - utter_ask_location
* restaurant_search{"location": "jalandhar"}
    - slot{"location": "jalandhar"}
    - action_verify_location
    - slot{"location": "jalandhar"}
    - slot{"valid_location": true}
    - action_search_restaurants
    - slot{"resultsfound": false}
* affirm
    - utter_goodbye
    - export
    - action_restart    

## price range and cuisine specified deny email
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "price":"Less than Rs.300"}
    - slot{"cuisine": "american"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - slot{"price": "Less than Rs.300"}
    - action_check_budget
    - slot{"minbudget":0}
    - slot{"maxbudget":300} 
    - slot{"valid_budget_range": true}
    - utter_ask_location
* restaurant_search{"location": "jalandhar"}
    - slot{"location": "jalandhar"}
    - action_verify_location
    - slot{"location": "jalandhar"}
    - slot{"valid_location": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* deny
    - utter_goodbye
    - export
    - action_restart
    
    
## price range and cuisine specified wrong cuisine
* greet
    - utter_greet
* restaurant_search{"cuisine": "british", "price":"Less than Rs.300"}
    - slot{"cuisine": "british"}
    - slot{"price": "Less than Rs.300"}
    - action_verify_cuisine
    - slot{"valid_cuisine": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - slot{"valid_cuisine": true}
    - action_check_budget
    - slot{"minbudget":0}
    - slot{"maxbudget":300} 
    - slot{"valid_budget_range": true}
    - utter_ask_location
* restaurant_search{"location": "kozhikode"}
    - slot{"location": "kozhikode"}
    - action_verify_location
    - slot{"location": "kozhikode"}
    - slot{"valid_location": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* affirm
    - utter_ask_emailid
* send_email{"emailid": "qwerty.123@yahoo.co.in"}
    - slot{"emailid": "qwerty.123@yahoo.co.in"}
    - action_send_email
* affirm
    - utter_goodbye
    - export
    - action_restart    

## price range and cuisine specified wrong cuisine wrong location
* greet
    - utter_greet
* restaurant_search{"cuisine": "british", "price":"Less than Rs.300"}
    - slot{"cuisine": "british"}
    - slot{"price": "Less than Rs.300"}
    - action_verify_cuisine
    - slot{"valid_cuisine": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - slot{"valid_cuisine": true}
    - action_check_budget
    - slot{"minbudget":0}
    - slot{"maxbudget":300} 
    - slot{"valid_budget_range": true}
    - utter_ask_location
* restaurant_search{"location": "karnal"}
    - slot{"location": "karnal"}
    - action_verify_location
    - slot{"location": "null"}
    - slot{"valid_location": false}
    - utter_city_not_found
* restaurant_search{"location": "dhanbad"}
    - slot{"location": "dhanbad"}
    - action_verify_location
    - slot{"location": "dhanbad"}
    - slot{"valid_location": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* affirm
    - utter_ask_emailid
* send_email{"emailid": "qwerty.123@yahoo.co.in"}
    - slot{"emailid": "qwerty.123@yahoo.co.in"}
    - action_send_email
* affirm
    - utter_goodbye
    - export
    - action_restart

    
## price range and cuisine specified wrong cuisine wrong location no resultsfound
* greet
    - utter_greet
* restaurant_search{"cuisine": "british", "price":"Less than Rs.300"}
    - slot{"cuisine": "british"}
    - slot{"price": "Less than Rs.300"}
    - action_verify_cuisine
    - slot{"valid_cuisine": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - slot{"valid_cuisine": true}
    - action_check_budget
    - slot{"minbudget":0}
    - slot{"maxbudget":300} 
    - slot{"valid_budget_range": true}
    - utter_ask_location
* restaurant_search{"location": "karnal"}
    - slot{"location": "karnal"}
    - action_verify_location
    - slot{"location": "null"}
    - slot{"valid_location": false}
    - utter_city_not_found
* restaurant_search{"location": "dhanbad"}
    - slot{"location": "dhanbad"}
    - action_verify_location
    - slot{"location": "dhanbad"}
    - slot{"valid_location": true}
    - action_search_restaurants
    - slot{"resultsfound": false}
* affirm
    - utter_goodbye
    - export
    - action_restart

## price range and cuisine specified wrong cuisine wrong location deny email
* greet
    - utter_greet
* restaurant_search{"cuisine": "british", "price":"Less than Rs.300"}
    - slot{"cuisine": "british"}
    - slot{"price": "Less than Rs.300"}
    - action_verify_cuisine
    - slot{"valid_cuisine": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - slot{"valid_cuisine": true}
    - action_check_budget
    - slot{"minbudget":0}
    - slot{"maxbudget":300} 
    - slot{"valid_budget_range": true}
    - utter_ask_location
* restaurant_search{"location": "karnal"}
    - slot{"location": "karnal"}
    - action_verify_location
    - slot{"location": "null"}
    - slot{"valid_location": false}
    - utter_city_not_found
* restaurant_search{"location": "dhanbad"}
    - slot{"location": "dhanbad"}
    - action_verify_location
    - slot{"location": "dhanbad"}
    - slot{"valid_location": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* deny
    - utter_goodbye
    - export
    - action_restart

    
## price range and cuisine specified wrong price
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "price":"More than Rs.300"}
    - slot{"cuisine": "american"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - slot{"price": "More than Rs.300"}
    - action_check_budget
    - slot{"minbudget":0}
    - slot{"maxbudget":10000} 
    - slot{"valid_budget_range": false}
    - utter_ask_budget
* restaurant_search{"price":"Less than Rs.300"}
    - slot{"price":"Less than Rs.300"}
    - action_check_budget
    - slot{"minbudget":0}
    - slot{"maxbudget":300} 
    - slot{"valid_budget_range": true}
    - utter_ask_location
* restaurant_search{"location": "ludhiana"}
    - slot{"location": "ludhiana"}
    - action_verify_location
    - slot{"location": "ludhiana"}
    - slot{"valid_location": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* affirm
    - utter_ask_emailid
* send_email{"emailid": "qwerty.123@yahoo.co.in"}
    - slot{"emailid": "qwerty.123@yahoo.co.in"}
    - action_send_email
* affirm
    - utter_goodbye
    - export
    - action_restart    


## price range and cuisine specified wrong price no resultsfound
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "price":"More than Rs.300"}
    - slot{"cuisine": "american"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - slot{"price": "More than Rs.300"}
    - action_check_budget
    - slot{"minbudget":0}
    - slot{"maxbudget":10000} 
    - slot{"valid_budget_range": false}
    - utter_ask_budget
* restaurant_search{"price":"Less than Rs.300"}
    - slot{"price":"Less than Rs.300"}
    - action_check_budget
    - slot{"minbudget":0}
    - slot{"maxbudget":300} 
    - slot{"valid_budget_range": true}
    - utter_ask_location
* restaurant_search{"location": "ludhiana"}
    - slot{"location": "ludhiana"}
    - action_verify_location
    - slot{"location": "ludhiana"}
    - slot{"valid_location": true}
    - action_search_restaurants
    - slot{"resultsfound": false}
* affirm
    - utter_goodbye
    - export
    - action_restart    
    
## price range and cuisine specified wrong price deny email
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "price":"More than Rs.300"}
    - slot{"cuisine": "american"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - slot{"price": "More than Rs.300"}
    - action_check_budget
    - slot{"minbudget":0}
    - slot{"maxbudget":10000} 
    - slot{"valid_budget_range": false}
    - utter_ask_budget
* restaurant_search{"price":"Less than Rs.300"}
    - slot{"price":"Less than Rs.300"}
    - action_check_budget
    - slot{"minbudget":0}
    - slot{"maxbudget":300} 
    - slot{"valid_budget_range": true}
    - utter_ask_location
* restaurant_search{"location": "ludhiana"}
    - slot{"location": "ludhiana"}
    - action_verify_location
    - slot{"location": "ludhiana"}
    - slot{"valid_location": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* deny
    - utter_goodbye
    - export
    - action_restart

## price range and cuisine specified wrong price wrong location
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "price":"More than Rs.300"}
    - slot{"cuisine": "american"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - slot{"price": "More than Rs.300"}
    - action_check_budget
    - slot{"minbudget":0}
    - slot{"maxbudget":10000} 
    - slot{"valid_budget_range": false}
    - utter_ask_budget
* restaurant_search{"price":"Less than Rs.300"}
    - slot{"price":"Less than Rs.300"}
    - action_check_budget
    - slot{"minbudget":0}
    - slot{"maxbudget":300} 
    - slot{"valid_budget_range": true}
    - utter_ask_location
* restaurant_search{"location": "kullu"}
    - slot{"location": "kullu"}
    - action_verify_location
    - slot{"location": "null"}
    - slot{"valid_location": false}
    - utter_city_not_found
* restaurant_search{"location": "jamshedpur"}
    - slot{"location": "jamshedpur"}
    - action_verify_location
    - slot{"location": "jamshedpur"}
    - slot{"valid_location": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* affirm
    - utter_ask_emailid
* send_email{"emailid": "qwerty.123@yahoo.co.in"}
    - slot{"emailid": "qwerty.123@yahoo.co.in"}
    - action_send_email
* affirm
    - utter_goodbye
    - export
    - action_restart    
    
    
## price range and cuisine specified wrong price wrong location deny email
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "price":"More than Rs.300"}
    - slot{"cuisine": "american"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - slot{"price": "More than Rs.300"}
    - action_check_budget
    - slot{"minbudget":0}
    - slot{"maxbudget":10000} 
    - slot{"valid_budget_range": false}
    - utter_ask_budget
* restaurant_search{"price":"Less than Rs.300"}
    - slot{"price":"Less than Rs.300"}
    - action_check_budget
    - slot{"minbudget":0}
    - slot{"maxbudget":300} 
    - slot{"valid_budget_range": true}
    - utter_ask_location
* restaurant_search{"location": "kullu"}
    - slot{"location": "kullu"}
    - action_verify_location
    - slot{"location": "null"}
    - slot{"valid_location": false}
    - utter_city_not_found
* restaurant_search{"location": "jamshedpur"}
    - slot{"location": "jamshedpur"}
    - action_verify_location
    - slot{"location": "jamshedpur"}
    - slot{"valid_location": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* deny
    - utter_goodbye
    - export
    - action_restart


## complete path wrong location with email
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "moga"}
    - slot{"location": "moga"}
    - action_verify_location
    - slot{"location": null}
    - slot{"valid_location": false}
    - utter_city_not_found
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_verify_location
    - slot{"location": "delhi"}
    - slot{"valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - utter_ask_budget
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - action_check_budget
    - slot{"minbudget": 0}
    - slot{"maxbudget":300} 
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* send_email{"emailid": "hellobot@gmail.com"}
    - slot{"emailid": "hellobot@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye
    - export
    - action_restart

## complete path wrong cuisine with email
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "amritsar"}
    - slot{"location": "amritsar"}
    - action_verify_location
    - slot{"location": "amritsar"}
    - slot{"valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "british"}
    - slot{"cuisine": "british"}
    - action_verify_cuisine
    - slot{"valid_cuisine": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - utter_ask_budget
* restaurant_search{"price": "Rs.300 to 700"}
    - slot{"price": "Rs.300 to 700"}
    - action_check_budget
    - slot{"minbudget": 0}
    - slot{"maxbudget":300} 
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* send_email{"emailid": "hellobot@gmail.com"}
    - slot{"emailid": "hellobot@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye
    - export
    - action_restart
## complete path wrong price range with email
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - action_verify_location
    - slot{"location": "bengaluru"}
    - slot{"valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - utter_ask_budget
* restaurant_search{"price": "Less than Rs.500"}
    - slot{"price": "Less than Rs.500"}
    - action_check_budget
    - slot{"minbudget": 0}
    - slot{"maxbudget":10000} 
    - slot{"valid_budget_range": false}
    - utter_ask_budget
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - action_check_budget
    - slot{"minbudget":0}
    - slot{"maxbudget":300}
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* send_email{"emailid": "hellobot@gmail.com"}
    - slot{"emailid": "hellobot@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye
    - export
    - action_restart
## happy_path with email
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian", "location": "kolkata", "price":"More than Rs.700"}
    - slot{"cuisine": "south indian"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - slot{"location": "kolkata"}
    - action_verify_location
    - slot{"location": "kolkata"}
    - slot{"valid_location": true}  
    - slot{"price":"More than Rs.700"}
    - action_check_budget
    - slot{"minbudget":700}
    - slot{"maxbudget":10000} 
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* send_email{"emailid": "hello123@gmail.com"}
    - slot{"emailid": "hello123@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye
    - export
    - action_restart
## location specified correct location with email
* greet
    - utter_greet
* restaurant_search{"location": "durgapur"}
    - slot{"location": "durgapur"}
    - action_verify_location
    - slot{"location": "durgapur"}
    - slot{"valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - utter_ask_budget
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - action_check_budget
    - slot{"minbudget": 0}
    - slot{"maxbudget":300} 
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* send_email{"emailid": "hello123@gmail.com"}
    - slot{"emailid": "hello123@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye
    - export
    - action_restart
## location specified wrong location with email
* greet
    - utter_greet
* restaurant_search{"location": "firozpur"}
    - slot{"location": "firozpur"}
    - action_verify_location
    - slot{"location": null}
    - slot{"valid_location": false}
    - utter_city_not_found
* restaurant_search{"location": "dhanbad"}
    - slot{"location": "dhanbad"}
    - action_verify_location
    - slot{"location": "dhanbad"}
    - slot{"valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - action_check_budget
    - slot{"minbudget":700}
    - slot{"maxbudget":10000} 
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* send_email{"emailid": "hello123@gmail.com"}
    - slot{"emailid": "hello123@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye
    - export
    - action_restart

## location specified wrong cuisine with email
* greet
    - utter_greet
* restaurant_search{"location": "durgapur"}
    - slot{"location": "durgapur"}
    - action_verify_location
    - slot{"location": "durgapur"}
    - slot{"valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "continental"}
    - slot{"cuisine": "continental"}
    - action_verify_cuisine
    - slot{"valid_cuisine": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - utter_ask_budget
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - action_check_budget
    - slot{"minbudget": 0}
    - slot{"maxbudget":300} 
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* send_email{"emailid": "hello123@gmail.com"}
    - slot{"emailid": "hello123@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye
    - export
    - action_restart
## location specified wrong price range with email
* greet
    - utter_greet
* restaurant_search{"location": "chandigarh"}
    - slot{"location": "chandigarh"}
    - action_verify_location
    - slot{"location": "chandigarh"}
    - slot{"valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - utter_ask_budget
* restaurant_search{"price": "300 to 900"}
    - slot{"price": "300 to 900"}
    - action_check_budget
    - slot{"minbudget":0}
    - slot{"maxbudget":10000} 
    - slot{"valid_budget_range": false}
    - utter_ask_budget
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - action_check_budget
    - slot{"minbudget": 0}
    - slot{"maxbudget":300} 
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* send_email{"emailid": "hello123@gmail.com"}
    - slot{"emailid": "hello123@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye
    - export
    - action_restart

## cuisine specified with email
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - utter_ask_location
* restaurant_search{"location": "faridabad"}
    - slot{"location": "faridabad"}
    - action_verify_location
    - slot{"location": "faridabad"}
    - slot{"valid_location": true}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - action_check_budget
    - slot{"minbudget":700}
    - slot{"maxbudget":10000} 
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* send_email{"emailid": "hello123@gmail.com"}
    - slot{"emailid": "hello123@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye
    - export
    - action_restart

## cuisine specified wrong cuisine with email
* greet
    - utter_greet
* restaurant_search{"cuisine": "japanese"}
    - slot{"cuisine": "japanese"}
    - action_verify_cuisine
    - slot{"valid_cuisine": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - utter_ask_location
* restaurant_search{"location": "ghaziabad"}
    - slot{"location": "ghaziabad"}
    - action_verify_location
    - slot{"location": "ghaziabad"}
    - slot{"valid_location": true}
    - utter_ask_budget
* restaurant_search{"price": "Rs.300 to 700"}
    - slot{"price": "Rs.300 to 700"}
    - action_check_budget
    - slot{"minbudget":300}
    - slot{"maxbudget":700} 
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* send_email{"emailid": "hello123@gmail.com"}
    - slot{"emailid": "hello123@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye
    - export
    - action_restart

## cuisine specified wrong location with email
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - utter_ask_location
* restaurant_search{"location": "tezpur"}
    - slot{"location": "tezpur"}
    - action_verify_location
    - slot{"location": null}
    - slot{"valid_location": false}
    - utter_city_not_found
* restaurant_search{"location": "cuttack"}
    - slot{"location": "cuttack"}
    - action_verify_location
    - slot{"location": "cuttack"}
    - slot{"valid_location": true}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - action_check_budget
    - slot{"minbudget":700}
    - slot{"maxbudget":10000} 
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* send_email{"emailid": "hello123@gmail.com"}
    - slot{"emailid": "hello123@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye
    - export
    - action_restart

## cuisine specified wrong price range with email
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - utter_ask_location
* restaurant_search{"location": "faridabad"}
    - slot{"location": "faridabad"}
    - action_verify_location
    - slot{"location": "faridabad"}
    - slot{"valid_location": true}
    - utter_ask_budget
* restaurant_search{"price": "500 to 1000"}
    - slot{"price": "300 to 900"}
    - action_check_budget
    - slot{"minbudget":0}
    - slot{"maxbudget":10000} 
    - slot{"valid_budget_range": false}
    - utter_ask_budget
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - action_check_budget
    - slot{"minbudget": 0}
    - slot{"maxbudget":300} 
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* send_email{"emailid": "hello123@gmail.com"}
    - slot{"emailid": "hello123@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye
    - export
    - action_restart

## price specified with email
* greet
    - utter_greet
* restaurant_search{"price": "Rs.300 to 700"}
    - slot{"price": "Rs.300 to 700"}
    - action_check_budget
    - slot{"minbudget":300}
    - slot{"maxbudget":700} 
    - slot{"valid_budget_range": true}
    - utter_ask_location
* restaurant_search{"location": "mathura"}
    - slot{"location": "mathura"}
    - action_verify_location
    - slot{"location": "mathura"}
    - slot{"valid_location": true}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* send_email{"emailid": "hello123@gmail.com"}
    - slot{"emailid": "hello123@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye
    - export
    - action_restart

## price specified wrong price range with email
* greet
    - utter_greet
* restaurant_search{"price": "800 to 2000"}
    - slot{"price": "800 to 2000"}
    - action_check_budget
    - slot{"minbudget":0}
    - slot{"maxbudget":10000} 
    - slot{"valid_budget_range": false}
    - utter_ask_budget
* restaurant_search{"price": "Rs.300 to 700"}
    - slot{"price": "Rs.300 to 700"}
    - action_check_budget
    - slot{"minbudget":300}
    - slot{"maxbudget":700} 
    - slot{"valid_budget_range": true}
    - utter_ask_location
* restaurant_search{"location": "malappuram"}
    - slot{"location": "malappuram"}
    - action_verify_location
    - slot{"location": "malappuram"}
    - slot{"valid_location": true}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* send_email{"emailid": "hello_123@yahoo.com"}
    - slot{"emailid": "hello_123@yahoo.com"}
    - action_send_email
* affirm
    - utter_goodbye
    - export
    - action_restart

## price specified wrong location with email
* greet
    - utter_greet
* restaurant_search{"price": "Rs.300 to 700"}
    - slot{"price": "Rs.300 to 700"}
    - action_check_budget
    - slot{"minbudget":300}
    - slot{"maxbudget":700} 
    - slot{"valid_budget_range": true}
    - utter_ask_location
* restaurant_search{"location": "alwar"}
    - slot{"location": "alwar"}
    - action_verify_location
    - slot{"location": null}
    - slot{"valid_location": false}
    - utter_city_not_found
* restaurant_search{"location": "kanpur"}
    - slot{"location": "kanpur"}
    - action_verify_location
    - slot{"location": "kanpur"}
    - slot{"valid_location": true}
    - utter_ask_cuisine    
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* send_email{"emailid": "hello_123@yahoo.com"}
    - slot{"emailid": "hello_123@yahoo.com"}
    - action_send_email
* affirm
    - utter_goodbye
    - export
    - action_restart

## price specified wrong cuisine with email
* greet
    - utter_greet
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - action_check_budget
    - slot{"minbudget":700}
    - slot{"maxbudget":10000} 
    - slot{"valid_budget_range": true}
    - utter_ask_location
* restaurant_search{"location": "lucknow"}
    - slot{"location": "lucknow"}
    - action_verify_location
    - slot{"location": "lucknow"}
    - slot{"valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "vegetarian"}
    - slot{"cuisine": "vegetarian"}
    - action_verify_cuisine
    - slot{"valid_cuisine": false}
    - utter_ask_cuisine 
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* send_email{"emailid": "hello.123@yahoo.com"}
    - slot{"emailid": "hello.123@yahoo.com"}
    - action_send_email
* affirm
    - utter_goodbye
    - export
    - action_restart

## location and cuisine specified with email
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian", "location": "erode"}
    - slot{"cuisine": "south indian"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - slot{"location": "erode"}
    - action_verify_location
    - slot{"location": "erode"}
    - slot{"valid_location": true}
    - utter_ask_budget
* restaurant_search{"price": "Rs.300 to 700"}
    - slot{"price": "Rs.300 to 700"}
    - action_check_budget
    - slot{"minbudget":300}
    - slot{"maxbudget":700} 
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* send_email{"emailid": "hello_123@yahoo.com"}
    - slot{"emailid": "hello_123@yahoo.com"}
    - action_send_email
* affirm
    - utter_goodbye
    - export
    - action_restart

## location and cuisine specified wrong location with email
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian", "location": "rishikesh"}
    - slot{"cuisine": "south indian"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - slot{"location": "rishikesh"}
    - action_verify_location
    - slot{"location": "null"}
    - slot{"valid_location": false}
* restaurant_search{"location": "jaipur"}
    - slot{"location": "jaipur"}
    - action_verify_location
    - slot{"location": "jaipur"}
    - slot{"valid_location": true}
    - utter_ask_budget
* restaurant_search{"price": "Rs.300 to 700"}
    - slot{"price": "Rs.300 to 700"}
    - action_check_budget
    - slot{"minbudget":300}
    - slot{"maxbudget":700} 
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* send_email{"emailid": "hello_123@yahoo.co.in"}
    - slot{"emailid": "hello_123@yahoo.co.in"}
    - action_send_email
* affirm
    - utter_goodbye
    - export
    - action_restart

## location and cuisine specified wrong cuisine with email
* greet
    - utter_greet
* restaurant_search{"cuisine": "mughlai", "location": "erode"}
    - slot{"cuisine": "mughlai"}
    - slot{"location": "erode"}
    - action_verify_cuisine
    - slot{"valid_cuisine": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - action_verify_location
    - slot{"location": "erode"}
    - slot{"valid_location": true}
    - utter_ask_budget
* restaurant_search{"price": "Rs.300 to 700"}
    - slot{"price": "Rs.300 to 700"}
    - action_check_budget
    - slot{"minbudget":300}
    - slot{"maxbudget":700} 
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* send_email{"emailid": "qwerty.123@yahoo.co.in"}
    - slot{"emailid": "qwerty.123@yahoo.co.in"}
    - action_send_email
* affirm
    - utter_goodbye
    - export
    - action_restart

## location and cuisine specified wrong cuisine wrong location with email
* greet
    - utter_greet
* restaurant_search{"cuisine": "mughlai", "location": "kota"}
    - slot{"cuisine": "mughlai"}
    - slot{"location": "kota"}
    - action_verify_cuisine
    - slot{"valid_cuisine": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - action_verify_location
    - slot{"location": "null"}
    - slot{"valid_location": false}
    - utter_city_not_found
* restaurant_search{"location": "jabalpur"}
    - utter_ask_location
    - slot{"location": "jabalpur"}
    - action_verify_location
    - slot{"location": "jabalpur"}
    - slot{"valid_location": true}  
    - utter_ask_budget
* restaurant_search{"price": "Rs.300 to 700"}
    - slot{"price": "Rs.300 to 700"}
    - action_check_budget
    - slot{"minbudget":300}
    - slot{"maxbudget":700} 
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* send_email{"emailid": "qwerty.123@yahoo.co.in"}
    - slot{"emailid": "qwerty.123@yahoo.co.in"}
    - action_send_email
* affirm
    - utter_goodbye
    - export
    - action_restart

## location and cuisine specified wrong cuisine wrong location wrong price with email
* greet
    - utter_greet
* restaurant_search{"cuisine": "mughlai", "location": "kota"}
    - slot{"cuisine": "mughlai"}
    - slot{"location": "kota"}
    - action_verify_cuisine
    - slot{"valid_cuisine": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - action_verify_location
    - slot{"location": "null"}
    - slot{"valid_location": false}
    - utter_city_not_found
* restaurant_search{"location": "jabalpur"}
    - utter_ask_location
    - slot{"location": "jabalpur"}
    - action_verify_location
    - slot{"location": "jabalpur"}
    - slot{"valid_location": true}  
    - utter_ask_budget
* restaurant_search{"price": "300 to 900"}
    - slot{"price": "300 to 900"}
    - action_check_budget
    - slot{"minbudget":0}
    - slot{"maxbudget":10000} 
    - slot{"valid_budget_range": false}
    - utter_ask_budget
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - action_check_budget
    - slot{"minbudget": 0}
    - slot{"maxbudget":300} 
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* send_email{"emailid": "qwerty.123@yahoo.co.in"}
    - slot{"emailid": "qwerty.123@yahoo.co.in"}
    - action_send_email
* affirm
    - utter_goodbye
    - export
    - action_restart

## price range and cuisine specified with email
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "price":"Less than Rs.300"}
    - slot{"cuisine": "american"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - slot{"price": "Less than Rs.300"}
    - action_check_budget
    - slot{"minbudget":0}
    - slot{"maxbudget":300} 
    - slot{"valid_budget_range": true}
    - utter_ask_location
* restaurant_search{"location": "jalandhar"}
    - slot{"location": "jalandhar"}
    - action_verify_location
    - slot{"location": "jalandhar"}
    - slot{"valid_location": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* send_email{"emailid": "qwerty.123@yahoo.co.in"}
    - slot{"emailid": "qwerty.123@yahoo.co.in"}
    - action_send_email
* affirm
    - utter_goodbye
    - export
    - action_restart    

## price range and cuisine specified wrong cuisine with email
* greet
    - utter_greet
* restaurant_search{"cuisine": "british", "price":"Less than Rs.300"}
    - slot{"cuisine": "british"}
    - slot{"price": "Less than Rs.300"}
    - action_verify_cuisine
    - slot{"valid_cuisine": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - slot{"valid_cuisine": true}
    - action_check_budget
    - slot{"minbudget":0}
    - slot{"maxbudget":300} 
    - slot{"valid_budget_range": true}
    - utter_ask_location
* restaurant_search{"location": "kozhikode"}
    - slot{"location": "kozhikode"}
    - action_verify_location
    - slot{"location": "kozhikode"}
    - slot{"valid_location": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* send_email{"emailid": "qwerty.123@yahoo.co.in"}
    - slot{"emailid": "qwerty.123@yahoo.co.in"}
    - action_send_email
* affirm
    - utter_goodbye
    - export
    - action_restart    

## price range and cuisine specified wrong cuisine wrong location with email
* greet
    - utter_greet
* restaurant_search{"cuisine": "british", "price":"Less than Rs.300"}
    - slot{"cuisine": "british"}
    - slot{"price": "Less than Rs.300"}
    - action_verify_cuisine
    - slot{"valid_cuisine": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - slot{"valid_cuisine": true}
    - action_check_budget
    - slot{"minbudget":0}
    - slot{"maxbudget":300} 
    - slot{"valid_budget_range": true}
    - utter_ask_location
* restaurant_search{"location": "karnal"}
    - slot{"location": "karnal"}
    - action_verify_location
    - slot{"location": "null"}
    - slot{"valid_location": false}
    - utter_city_not_found
* restaurant_search{"location": "dhanbad"}
    - slot{"location": "dhanbad"}
    - action_verify_location
    - slot{"location": "dhanbad"}
    - slot{"valid_location": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* send_email{"emailid": "qwerty.123@yahoo.co.in"}
    - slot{"emailid": "qwerty.123@yahoo.co.in"}
    - action_send_email
* affirm
    - utter_goodbye
    - export
    - action_restart

## price range and cuisine specified wrong price with email
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "price":"More than Rs.300"}
    - slot{"cuisine": "american"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - slot{"price": "More than Rs.300"}
    - action_check_budget
    - slot{"minbudget":0}
    - slot{"maxbudget":10000} 
    - slot{"valid_budget_range": false}
    - utter_ask_budget
* restaurant_search{"price":"Less than Rs.300"}
    - slot{"price":"Less than Rs.300"}
    - action_check_budget
    - slot{"minbudget":0}
    - slot{"maxbudget":300} 
    - slot{"valid_budget_range": true}
    - utter_ask_location
* restaurant_search{"location": "ludhiana"}
    - slot{"location": "ludhiana"}
    - action_verify_location
    - slot{"location": "ludhiana"}
    - slot{"valid_location": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* send_email{"emailid": "qwerty.123@yahoo.co.in"}
    - slot{"emailid": "qwerty.123@yahoo.co.in"}
    - action_send_email
* affirm
    - utter_goodbye
    - export
    - action_restart    

## price range and cuisine specified wrong price wrong location with email
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "price":"More than Rs.300"}
    - slot{"cuisine": "american"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - slot{"price": "More than Rs.300"}
    - action_check_budget
    - slot{"minbudget":0}
    - slot{"maxbudget":10000} 
    - slot{"valid_budget_range": false}
    - utter_ask_budget
* restaurant_search{"price":"Less than Rs.300"}
    - slot{"price":"Less than Rs.300"}
    - action_check_budget
    - slot{"minbudget":0}
    - slot{"maxbudget":300} 
    - slot{"valid_budget_range": true}
    - utter_ask_location
* restaurant_search{"location": "kullu"}
    - slot{"location": "kullu"}
    - action_verify_location
    - slot{"location": "null"}
    - slot{"valid_location": false}
    - utter_city_not_found
* restaurant_search{"location": "jamshedpur"}
    - slot{"location": "jamshedpur"}
    - action_verify_location
    - slot{"location": "jamshedpur"}
    - slot{"valid_location": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* send_email{"emailid": "qwerty.123@yahoo.co.in"}
    - slot{"emailid": "qwerty.123@yahoo.co.in"}
    - action_send_email
* affirm
    - utter_goodbye
    - export
    - action_restart    

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "goa"}
    - slot{"location": "goa"}
    - action_verify_location
    - slot{"location": "goa"}
    - slot{"valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - action_check_budget
    - slot{"minbudget": 700}
    - slot{"maxbudget": 10000}
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* send_email{"emailid": "jeena.pandit@gmail.com"}
    - slot{"emailid": "jeena.pandit@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye

## interactive_story_2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "ludhiana"}
    - slot{"location": "ludhiana"}
    - action_verify_location
    - slot{"location": "ludhiana"}
    - slot{"valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - utter_ask_budget
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - action_check_budget
    - slot{"minbudget": 0}
    - slot{"maxbudget": 300}
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* send_email{"emailid": "jeena.pandit.89@gmail.com"}
    - slot{"emailid": "jeena.pandit.89@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye

## interactive_story_3
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Nagpur", "price": "Less than Rs.300"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Nagpur"}
    - slot{"price": "Less than Rs.300"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - action_verify_location
    - slot{"location": "nagpur"}
    - slot{"valid_location": true}
    - action_check_budget
    - slot{"minbudget": 0}
    - slot{"maxbudget": 300}
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* send_email{"emailid": "dewesh.giet@gmail.com"}
    - slot{"emailid": "dewesh.giet@gmail.com"}
    - action_send_email
* goodbye
    - utter_goodbye

## interactive_story_4
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "rishikesh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "rishikesh"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - action_verify_location
    - slot{"location": null}
    - slot{"valid_location": false}
    - utter_city_not_found
* restaurant_search{"location": "Chandigarh"}
    - slot{"location": "Chandigarh"}
    - action_verify_location
    - slot{"location": "chandigarh"}
    - slot{"valid_location": true}
    - utter_ask_budget
* restaurant_search{"price": "Rs.300 to 700"}
    - slot{"price": "Rs.300 to 700"}
    - action_check_budget
    - slot{"minbudget": 300}
    - slot{"maxbudget": 700}
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* send_email{"emailid": "dewesh.giet@gmail.com"}
    - slot{"emailid": "dewesh.giet@gmail.com"}
    - action_send_email
* goodbye
    - utter_goodbye

## interactive_story_5
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh", "price": "More than Rs.700"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - slot{"price": "More than Rs.700"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - action_verify_location
    - slot{"location": "chandigarh"}
    - slot{"valid_location": true}
    - action_check_budget
    - slot{"minbudget": 700}
    - slot{"maxbudget": 10000}
    - slot{"valid_budget_range": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* deny
    - utter_goodbye

## interactive_story_6
* greet
    - utter_greet
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - action_check_budget
    - slot{"minbudget": 700}
    - slot{"maxbudget": 10000}
    - slot{"valid_budget_range": true}
    - utter_ask_location
* affirm{"location": "panji"}
    - slot{"location": "panji"}
    - action_verify_location
    - slot{"location": null}
    - slot{"valid_location": false}
    - utter_city_not_found
* restaurant_search{"location": "goa"}
    - slot{"location": "goa"}
    - action_verify_location
    - slot{"location": "goa"}
    - slot{"valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* deny
    - utter_goodbye

## interactive_story_7
* greet
    - utter_greet
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - action_check_budget
    - slot{"minbudget": 0}
    - slot{"maxbudget": 300}
    - slot{"valid_budget_range": true}
    - utter_ask_location
* restaurant_search{"location": "Rajahmundry"}
    - slot{"location": "Rajahmundry"}
    - action_verify_location
    - slot{"location": "rajahmundry"}
    - slot{"valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_verify_cuisine
    - slot{"valid_cuisine": true}
    - action_search_restaurants
    - slot{"resultsfound": true}
    - utter_ask_sendemail
* deny
    - utter_goodbye
