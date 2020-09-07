from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json

import pandas as pd
import smtplib
from email.message import EmailMessage


output_response = ""

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'
		
	def run(self, dispatcher, tracker, domain):
		config={"user_key":"3e34705c21d061b234a03b546694ec11"} # get this API Key from Zomato API site
		zomato = zomatopy.initialize_app(config)
		# Get all slot values
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine').lower()
		minbudget = tracker.get_slot('minbudget')
		maxbudget = tracker.get_slot('maxbudget')
		# Get Location latitude longitude
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'chinese':25,'mexican':73,'italian':55,'american':1,'south indian':85,'north indian':50,}
		# search for restaurants
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 200)
		d = json.loads(results)
		global output_response
		# Filter based on Budget
		output_response = [x for x in d['restaurants'] if x['restaurant']['average_cost_for_two'] in range(minbudget,maxbudget+1)]
		response=""
		if len(output_response) == 0:
			dispatcher.utter_message("No Results Found! Please try with different search criteria.")
			return[SlotSet("resultsfound", False)]
		else:
			i=1
			email_response = output_response
			for restaurant in output_response[:5]:
				response=response+ str(i)+". " + restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+" has been rated "+str(restaurant['restaurant']['user_rating']['aggregate_rating'])+"\n"
				i+=1
			dispatcher.utter_message("Showing you top rated restaurants:-\n")
			dispatcher.utter_message(response)
			return [SlotSet("resultsfound", True)]

class ActionCheckBudget(Action):

	def name(self):
		return "action_check_budget"

	def run(self, dispatcher, tracker, domain):
		price_range = ["Less than Rs.300", "Rs.300 to 700", "More than Rs.700"]
		error_msg = "Sorry! This Price range is not supported. Please re-enter your choice from the available price range."
		try:
			price = tracker.get_slot('price')
		except (RuntimeError, TypeError, NameError, AttributeError):
			dispatcher.utter_message(error_msg)
			return [SlotSet('minbudget', 0), SlotSet('maxbudget', 10000), SlotSet('valid_budget_range', False)]
		if price == price_range[0]:
			return [SlotSet('minbudget', 0), SlotSet('maxbudget', 300), SlotSet('valid_budget_range', True)]
		elif price == price_range[1]:
			return [SlotSet('minbudget', 300), SlotSet('maxbudget', 700), SlotSet('valid_budget_range', True)]
		elif price == price_range[2]:
			return [SlotSet('minbudget', 700), SlotSet('maxbudget', 10000), SlotSet('valid_budget_range', True)]
		else:
			dispatcher.utter_message(error_msg)
			return [SlotSet('minbudget', 0), SlotSet('maxbudget', 10000), SlotSet('valid_budget_range', False)]


class ActionVerifyLocation(Action):
	
	def name(self):
		return "action_verify_location"
	 
	def run(self, dispatcher, tracker, domain):
		tier_1_2_cities = ["delhi","mumbai","kolkata","chennai","bengaluru","hyderabad","pune","ahmedabad","agra","ajmer","aligarh","amravati","amritsar","asansol","aurangabad","bareilly","belgaum","bhavnagar","bhiwandi","bhopal","bhubaneswar","bikaner","bilaspur","bokaro steel city","chandigarh","coimbatore","cuttack","dehradun","dhanbad","bhilai","durgapur","erode","faridabad","firozabad","ghaziabad","gorakhpur","gulbarga","guntur","gwalior","gurgaon","guwahati","hamirpur","hubli–dharwad","indore","jabalpur","jaipur","jalandhar","jammu","jamnagar","jamshedpur","jhansi","jodhpur","kakinada","kannur","kanpur","kochi","kolhapur","kollam","kozhikode","kurnool","ludhiana","lucknow","madurai","malappuram","mathura","goa","mangalore","meerut","moradabad","mysore","nagpur","nanded","nashik","nellore","noida","patna","pondicherry","purulia","prayagraj","raipur","rajkot","rajahmundry","ranchi","rourkela","salem","sangli","shimla","siliguri","solapur","srinagar","surat","thiruvananthapuram","thrissur","tiruchirappalli","tiruppur","ujjain","bijapur","vadodara","varanasi","vasai-virar city","vijayawada","visakhapatnam","vellore","warangal"]
		loc = tracker.get_slot('location')
		try:
			loc = loc.lower()
		except (RuntimeError, TypeError, NameError, AttributeError):
			return [SlotSet('location',None), SlotSet('valid_location', False)]
		if not(loc in tier_1_2_cities):
			return [SlotSet('location',None), SlotSet('valid_location', False)]
		else:
			return [SlotSet('location',loc), SlotSet('valid_location', True)]


class ActionVerifyCuisine(Action):
	def name(self):
		return "action_verify_cuisine"
		
	def run(self, dispatcher, tracker, domain):
		cuisines = ['chinese','mexican','italian','american','south indian','north indian']
		cuisine = tracker.get_slot('cuisine')
		cuisine = cuisine.lower()
        # check if the cuisine slot value is in the valid cuisine list
		if (cuisine in cuisines):
			return [SlotSet('valid_cuisine', True)]
		else:
			dispatcher.utter_message("Sorry! This cuisine is not supported. Please re-enter your choice from the list specified.")
			return [SlotSet('valid_cuisine', False)]
		

class ActionSendEmail(Action):
	def name(self):
		return 'action_send_email'
		
	def run(self, dispatcher, tracker, domain):
		emailid = tracker.get_slot('emailid')
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		global output_response
		email_df = pd.DataFrame(columns=['S.No.','Restaurant Name', 'Restaurant Locality Address', 'Average Budget for two people','Zomato User Rating'],index=None)
		i=1
		for restaurant in output_response[:10]:
			email_df = email_df.append({'S.No.': i ,'Restaurant Name': restaurant['restaurant']['name'], 'Restaurant Locality Address': restaurant['restaurant']['location']['address'], 'Average Budget for two people': restaurant['restaurant']['average_cost_for_two'],'Zomato User Rating': restaurant['restaurant']['user_rating']['aggregate_rating']}, ignore_index=True)
			i+=1
		email_df = email_df.set_index('S.No.')
		
		#Sending Email
		mail_content = """<head><style text="type/css" rel="stylesheet">h4{font-weight:normal}h3{font-weight:normal;color:#000000} th{background-color: #bfdce0} table,thead,th,tr,tbody{border:1px solid black;border-collapse: collapse;text-align:center}</style></head>
		<h4>Hello!<br/><br/>
		Below are some of the top restaurants matching your search that you may want to explore. <br/>                                                                      
		<br/><br/>"""+email_df.to_html()+"""<br/><br/>
		<b>Bon Appetit!<br/>"""
		#The mail addresses and password
		sender_address = 'test123@gmail.com' #Sender email address
		sender_pass = '12345'                #Password of the Sender
		receiver_address = emailid
		#Setup the EmailMessage
		message = EmailMessage()
		message['From'] = sender_address
		message['To'] = receiver_address
		message['Subject'] = 'Top Rated '+cuisine.capitalize()+' Restaurants in '+loc.capitalize()   #The subject line
		#The body and the attachments for the mail
		message.set_content(mail_content, subtype='html')
		#Create SMTP session for sending the mail
		try:
			session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
			session.starttls() #enable security
			session.login(sender_address, sender_pass) #login with mail_id and password
			session.send_message(message)
			session.quit()
			dispatcher.utter_message("Email Sent. Bon Appetit!\n")
		except (RuntimeError, TypeError, NameError, AttributeError):
			dispatcher.utter_message("Unable to send mails right now. This is a temporary problem. Please try again later.\n")
		return []
