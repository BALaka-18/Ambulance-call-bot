import os
from twilio.rest import Client
from selenium import webdriver
# from twilio.twiml.voice_response import Dial, VoiceResponse, Say

class AmbulanceBot:
    def __init__(self, client = None, server_no = None, account_sid = None, 
                    auth_token = None, record = True, has_account = True, driver_path = r'C:\Users\BIPLAB\TopCareer\selenium\common\geckodriver.exe'):
        self.client = client
        self.server_no = server_no
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.record = record
        self.has_account = has_account
        self.driver_path = driver_path

    # Main function that initiates the bot
    def callClient(self,hosted_url):
        # Details
        account_SID,AUTH_TOKEN = self.account_sid,self.auth_token
        recording = self.record
        CLIENT,SERVER = self.client,self.server_no

        # Initializing calling client
        client = Client(account_SID, AUTH_TOKEN)
        initiate_call = client.calls.create(
                                record = recording,
                                url = hosted_url,   # website hosting the XML
                                # The website must be up and running at the time the bot runs.
                                to = CLIENT,
                                from_= SERVER
        )
        
        return initiate_call.sid      # Print out the unique call SID per call.

    # If the server/calling number is not registered, automatically open the Registration page.
    # If the user has no account, automatically open the Sign Up page.
    def Register(self):
        # Get details
        HAS_ACCOUNT,driver_path = self.has_account,self.driver_path

        # Initialize the driver
        driver = webdriver.Firefox(executable_path = driver_path)
        driver.get("https://www.twilio.com/")
        if HAS_ACCOUNT:
            login = driver.find_element_by_xpath('/html/body/nav/div/header/ul/li[2]/a')
            login.click()
        else:
            signup = driver.find_element_by_xpath('/html/body/nav/div/ul[2]/li[2]/a')
            signup.click()

# Driver code
if __name__ == "__main__":
    # Calling number
    number_server = input("Enter Calling number : ")
    number_server_with_code = str('+91' + str(number_server))
    # Client's number
    number_client = input("Enter Client number : ")
    number_client_with_code = str('+91' + str(number_client))
    # Get account details
    get_account_sid = input("Enter account SID : ")
    get_auth_token = input("Enter auth token : ")

    # Check status of calling number
    is_registered = input("Is your number registered on Twilio ?(Y/N)")
    if is_registered == 'Y':
        # Initiate the bot class
        ambulance_help_registered = AmbulanceBot(client=number_client_with_code,server_no=number_server_with_code,
                                        account_sid=get_account_sid,auth_token=get_auth_token,has_account=True)
        # Fire up the bot and print the call SID
        call_details = ambulance_help_registered.callClient(hosted_url='https://kinematic-ejection.000webhostapp.com/')
        print(call_details)
    elif is_registered == 'N':
        choice = input("Kindly register the calling number on Twilio first. Have account on Twilio ?(Y/N) ")
        if choice == 'Y':
            ambulance_help_with_account = AmbulanceBot(client=number_client_with_code,server_no=number_server_with_code,
                                        account_sid=get_account_sid,auth_token=get_auth_token,has_account=True)
            ambulance_help_with_account.Register()
        else:
            ambulance_help_without_account = AmbulanceBot(client=number_client_with_code,server_no=number_server_with_code,
                                        account_sid=get_account_sid,auth_token=get_auth_token,has_account=False)
            ambulance_help_without_account.Register()
    else:
        print("Wrong input. Terminating process...")
        exit(-1)