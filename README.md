# Navagetur
Navagetur: The Online Privacy Toolkit

## How to Install

- Click `Code -> Download ZIP` to download the application and open the zipped file.

### Setup Application

- Open your computer's terminal
- Ensure that running `python --version` in the terminal returns python version 3 or higher
    - If not, download at [https://www.python.org/downloads/](https://www.python.org/downloads/)
- Ensure that running `pip --version` in the terminal returns python version 3 or higher
    - If not, download at [https://pip.pypa.io/en/stable/installation/](https://pip.pypa.io/en/stable/installation/)
- Move to the project directory within the terminal
- Run `./setup.sh` from the terminal

### Run Application

- Open your computer's terminal
- Run `./run.sh` from the terminal
- If it doesn't automatically open, open `http://127.0.0.1:5000/`

### Possible Issues

- If the `./run.sh` script produces an error, run `python ./Flask\ App/run.py 5001` and open `http://127.0.0.1:5001/` (keep increasing 5001 until the error disappears)

## Widgets

### Password “Crackability” Widget

Most laypeople who use computers lack an adequate conception of why they are encouraged to use safe passwords. This widget aims to put the ease of cracking passwords into context with time estimates of how long it would take to crack a given password as well as some example passwords and times to crack. This widget provides users with a calculation for how long it would take to brute force crack their password based on a low-end estimate for how long it takes their computer to run basic C code. This allows users to input a string and check how good of a password it would make.

### Geographical Recording and Data Privacy Law Locator Widget

Many individuals are not aware of the privacy or recording consent laws that are applicable to them given their residence. We want to empower users to be knowledgeable by creating a widget that simply allows users to type in their zip code and will quickly explain the most pertinent privacy/recording consent laws within their specified region. The geographical recording and data privacy law locator is zip code powered and allows users to input their zip code and it then returns the consent laws that are applicable within that region. The user types in their zip code and on the back-end the zip code is matched with the corresponding state. The state is then searched within our internal categories which are roughly one-party, mixed-party and non-regulated state arrays which were sourced from Matthiesen, Wickert & Lehrer, Attorneys of Law Report . We increased the functionality to also display more relevant laws, specific to the state.
 
### Personal Account Security Information Widget

Many people have trouble keeping track of the security features they have enabled on each of their online accounts. This widget allows users to keep track of a variety of account safety features and see a representative score for how safe the account is. There are a variety of deterrents to increasing the safety of accounts that this widget aims to address. For example, if users have their phone added as a multi-factor authentication device and they are in the process of changing their number or have multiple phones, the user may not know which devices currently rely on each phone number. This application helps to reduce this deterrent by making it easy to add and check the current features of each account. This widget allows users to track website name, username, password, the date of last password change, whether multi-factor authentication is enabled, whether app passcodes have been generated, associated authenticator app devices, associated physical authentication keys, and associated phone numbers. All of these fields are entirely optional and are intended to make the user’s experience keeping track of their account information easier. Once account information is inputted, the program calculates the time it would take for the current device to brute force crack the password and calculates a safety score based on how many safety features are enabled for each account. This widget expands upon the current functionality of password managers to motivate users to further increase their online security by reducing their cognitive load when keeping track of and maintaining additional security measures.

### Personal Uniqueness Widget

It can be difficult for laypeople to understand how easy it can be to re-identify their data. This widget contextualizes how easy it is to randomly guess a person based on their inputted characteristics in comparison to how easy it would be to pick out a person from everyone in the United States. This widget determines how unique someone is by asking them for a list of possible demographic characteristics and comparing that person to U.S. Census data. 

###

##

