![Supported Python versions](https://img.shields.io/badge/python-2.7-blue.svg)
# PhoneHunter
PhoneHunter is a small sample script to extract personal data from a phone number. It utilizes [Twilio](https://www.twilio.com) and [NextCaller](https://nextcaller.com/) to lookup a phone number and return data. As far as I know NextCaller is primarily designed for fraud prevention and sales lead information, however anyone can request this data with no verification. It took me a grand total of 5 minutes and $20 to create an account that allows me to lookup 200 phone numbers. 

This information should **NOT** be treated as 100% valid. From my simple testing the validity of the information appears to be between 70-85% across a sample size of ~10 numbers. 

Additionally this script could malfunction at any time and is provided as is with no warranty. 

## Setup:
1. Create a [Twilio](https://www.twilio.com) account and fund it
2. Install [Advanced Caller ID by Next Caller](https://www.twilio.com/marketplace/add-ons/nextcaller-advanced-caller-id)
3. Insert your Account SID and Auth Token into phunter.py
4. ??????
5. **PROFIT**

###Usage:
**./phunter *[Phone Number]***

###Example: 
**./phunter 5555551234**
 

## To be added:
- Error handling/bounds checking
- Number formatting capabilities
- Output to file
- Documentation
- Enhanced argument support
- --help output


## Questions:
*Why didn't you use the python API?* - Either the current API documentation is broken or I didn't drink enough coffee. Either way the documentation is lacking a solid example of this

*How can I hide my information from this?* -  ¯\\_(ツ)_/¯ Your info is aggregated everywhere so hiding from this is plugging a hole in a screen boat

*Look up this number for me!* - No

