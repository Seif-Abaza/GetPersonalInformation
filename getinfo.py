#!/usr/bin/env python
from piplapis import search
import ColorText
import os
import getpass
import re
import phonenumbers
from phonenumbers import geocoder

autho = 'Seif Abaza <abazuos@gmail.com>'
lines = '====================================================================='
exit_msg = "\n[++] Shutting down ... Goodbye. ( ^_^)\n"

Color = ColorText.color
Functions = {
	1: 'Person Infromations',
	2: 'Phone Informations',
	0: 'Exit...'
}

Message = Color.PURPLE + Color.BOLD + Color.UNDERLINE + 'Do you see the number of options or are you blind ?' + Color.END


def Banar ():
	print '  ____      _'
	print ' / ___| ___| |_'
	print '| |  _ / _ \ __|'
	print '| |_| |  __/ |_'
	print ' \____|\___|\__|'

	print ' ___        __                            _   _'
	print '|_ _|_ __  / _| ___  _ __ _ __ ___   __ _| |_(_) ___  _ __  ___'
	print ' | ||  _ \| |_ / _ \|   _|  _ ` _ \ / _` | __| |/ _ \|  _ \/ __|'
	print ' | || | | |  _| (_) | |  | | | | | | (_| | |_| | (_) | | | \__ \\'
	print '|___|_| |_|_|  \___/|_|  |_| |_| |_|\__,_|\__|_|\___/|_| |_|___/'
	print lines
	print autho.center(len(autho) + (len(lines) - len(autho)), '=')
	print lines + '\n'


def PeoplesInfoBanar ():
	ClearScreen()
	print ' ____                  _'
	print '|  _ \ ___  ___  _ __ | | ___  ___  '
	print '| |_) / _ \/ _ \| V_ \| |/ _ \/ __| '
	print '|  __/  __/ (_) | |_) | |  __/\__ \ '
	print '|_|   \___|\___/| .__/|_|\___||___/ '
	print '                |_| '
	print ' ___        __                            _   _ '
	print '|_ _|_ __  / _| ___  _ __ _ __ ___   __ _| |_(_) ___  _ __  '
	print ' | || V_ \| |_ / _ \| V__|  _ ` _ \ / _` | __| |/ _ \|  _ \ '
	print ' | || | | |  _| (_) | |  | | | | | | (_| | |_| | (_) | | | |'
	print '|___|_| |_|_|  \___/|_|  |_| |_| |_|\__,_|\__|_|\___/|_| |_|'
	print lines
	print lines


def PhoneInformationBanar ():
	ClearScreen()
	print ' ____  _                                                    '
	print '|  _ \| |__   ___  _ __   ___                               '
	print '| |_) |  _ \ / _ \| v_ \ / _ \                              '
	print '|  __/| | | | (_) | | | |  __/                              '
	print '|_|   |_| |_|\___/|_| |_|\___|                              '
	print '                                                            '
	print ' ___        __                            _   _             '
	print '|_ _|_ __  / _| ___  _ __ _ __ ___   __ _| |_(_) ___  _ __  '
	print ' | || v_ \| |_ / _ \| v__| v_ ` _ \ / _` | __| |/ _ \| v_ \ '
	print ' | || | | |  _| (_) | |  | | | | | | (_| | |_| | (_) | | | |'
	print '|___|_| |_|_|  \___/|_|  |_| |_| |_|\__,_|\__|_|\___/|_| |_|'
	print lines
	print lines


# Basic Functions

def Start ():
	# Load Banar
	Banar()

	# Ask User what he want ?
	print Color.RED + Color.BOLD + "What do you want ?" + Color.END
	# Load All options form dictionary
	for OptionsKeys in Functions.keys():
		Options = Color.BOLD + Color.RED + '[' + str(OptionsKeys) + '] ' + Color.END
		Label = Color.YELLOW + Functions.get(OptionsKeys) + Color.END
		print Options + Label
	# End
	print lines
	# Waiting Input
	choois = raw_input(Color.BOLD + Color.RED + 'I want number : ' + Color.END)
	if choois.isdigit():  # Must Digital 0~9
		toint = int(choois)
		if toint >= len(Functions):
			fMessage = Color.RED + Color.BOLD + lines + Color.END + '\n'
			fMessage += Message + '\n'
			fMessage += Color.RED + Color.BOLD + lines + Color.END + '\n'
			raw_input(fMessage)
			ClearScreen()
			Start()
		else:
			for fun in choois:
				toint = int(fun)
				if toint == 1:
					PersonInfo()
					break
				elif toint == 2:
					PhoneInfo()
					break
				elif toint == 3:
					IPInfor()
					break
				elif toint == 0:
					EndScript()

	else:  # Joking with user :)
		ClearScreen()
		Qu = Color.BOLD + Color.RED + str(getpass.getuser()).capitalize() + ' Are You want to Joking ?\n' + Color.END
		ans = raw_input(Qu)
		if ans == 'y' or ans == 'yes' or ans == 'Y' or ans == 'YES':
			print Color.BOLD + Color.YELLOW + 'I not have time ... Bye'
			EndScript()
		elif ans == 'n' or ans == 'no' or ans == 'N' or ans == 'NO':
			ClearScreen()
			Start()
		else:
			EndScript()


# Options

def PersonInfo ():
	PeoplesInfoBanar()
	if CheckInternetConnection():
		Label = 'Put the information available for you \n'
		Label += lines
		print Color.BOLD + Color.UNDERLINE + Color.CYAN + Label + Color.END

		data = ('Email', 'Phone', 'Back To Main Menu')
		index = 1
		for elem in data:
			print Color.BOLD + Color.RED + '[' + str(index) + '] ' + Color.END + Color.YELLOW + elem + Color.END
			index += 1
		try:
			options = raw_input(Color.BOLD + Color.RED + 'I Know : ' + Color.END)
			if len(options) > 0:
				if not options.isdigit():
					del options
					PersonInfo()
			else:
				ClearScreen()
				Start()

			if options is not None:
				if int(options) != 0:
					options = int(options) - 1
					if options < 0:
						PersonInfo()
				leng = len(data) - 1
				if leng < options:
					fMessage = Color.RED + Color.BOLD + lines + Color.END + '\n'
					fMessage += Message + '\n'
					fMessage += Color.RED + Color.BOLD + lines + Color.END + '\n'
					raw_input(fMessage)
					ClearScreen()
					Start()
				if options == leng:
					ClearScreen()
					Start()
					return
				else:
					titLabel = Color.BOLD + data[options] + ' : ' + Color.END
					inputdata = data[options] + ':' + raw_input(titLabel)
					response = piplSearching(inputdata)
					if response:
						print setLabel('Name') + setNormalValue(str(response.name))
						print setLabel('Education') + setNormalValue(str(response.education))
						print setLabel('Username') + setMiddelValue(str(response.username))
						print setLabel('Address') + setNormalValue(str(response.address))
						print setLabel('Email') + setGoodValue(str(response.email))
						print setLabel('Phone') + setGoodValue(str(response.phone))
						print setLabel('Language') + setNormalValue(str(response.language))
						print setLabel('Ethnicity') + setNormalValue(str(response.ethnicity))
						print setLabel('Origin Country') + setNormalValue(str(response.origin_country))
						print setLabel('Jobs') + setNormalValue(", ".join(map(str, response.person.jobs)))
						print setLabel('Relationship') + setNormalValue(
							", ".join(map(str, response.person.relationships)))
						print setLabel('URL') + setNormalValue(str(response.url))
						raw_input(lines + '\nEnter to Back...')
						ClearScreen()
						PersonInfo()
					else:
						raw_input(lines + '\nNothing Info\nEnter to Back...')
						ClearScreen()
						PersonInfo()
			else:
				ClearScreen()
				Start()
		except BaseException, e:
			raw_input('Error:' + e.message)
			del options
			ClearScreen()
			Start()

	else:
		EndScript()


def PhoneInfo ():
	PhoneInformationBanar()
	if CheckInternetConnection():
		Label = 'Choose What kind of infromation you know ?\n'
		Label += lines
		print Color.BOLD + Color.UNDERLINE + Color.CYAN + Label + Color.END

		data = ('Information Phone Number', 'Back to Main Menu')
		index = 1
		for ele in data:
			print Color.BOLD + Color.RED + '[' + str(index) + '] ' + Color.END + Color.YELLOW + ele + Color.END
			index += 1
		try:
			options = raw_input(Color.BOLD + Color.RED + 'What did you know : ' + Color.END)
			if len(options) > 0 and not options.isdigit():
				del options
				PhoneInfo()
			else:
				options = int(options) - 1
				if options == (len(data) - 1):
					ClearScreen()
					Start()

				if options > (len(data) - 1):
					fMessage = Color.RED + Color.BOLD + lines + Color.END + '\n'
					fMessage += Message + '\n'
					fMessage += Color.RED + Color.BOLD + lines + Color.END + '\n'
					raw_input(fMessage)
					ClearScreen()
					Start()
				else:
					if (int(options) == 0):
						print Color.UNDERLINE + 'For get information about phone number please set phone like this : +XXXXXXXXXXX\n' + Color.END
						tmp1 = raw_input(Color.BLUE + Color.BOLD + data[options] + ' : ' + Color.END)
						tmp2 = re.sub(r'\D', "", tmp1)
						PhoneNumber = '+' + phone_format(tmp2)
						ClearScreen()
						PhoneInformationBanar()
						fMessage = Color.RED + Color.BOLD + lines + Color.END + '\n'
						fMessage += Color.GREEN + Color.BOLD + 'Get Information about ' + PhoneNumber + ' ... ' + Color.END + '\n'
						fMessage += Color.GREEN + Color.BOLD + 'Please Wait... ' + Color.END + '\n'
						fMessage += Color.RED + Color.BOLD + lines + Color.END + '\n'
						print fMessage
						pn = phonenumbers.parse(PhoneNumber, None)
						response = piplSearching('Phone:' + PhoneNumber)
						if response:
							print setLabel('Name') + setNormalValue(str(response.name))
							print setLabel('Education') + setNormalValue(str(response.education))
							print setLabel('Username') + setMiddelValue(str(response.username))
							print setLabel('City') + setNormalValue(repr(geocoder.description_for_number(pn, "en")))
							print setLabel('Address') + setMiddelValue(str(response.address))
							print setLabel('Email') + setGoodValue(str(response.email))
							print setLabel('Phone') + setNormalValue(str(response.phone))
							print setLabel('Language') + setNormalValue(str(response.language))
							print setLabel('Ethnicity') + setNormalValue(str(response.ethnicity))
							print setLabel('Origin Country') + setGoodValue(str(response.origin_country))
							print setLabel('Jobs') + setNormalValue(", ".join(map(str, response.person.jobs)))
							print setLabel('Relationship') + setNormalValue(
								", ".join(map(str, response.person.relationships)))
							print setLabel('URL') + setNormalValue(str(response.url))
							print lines
							# callerpy.country = str(response.ethnicity)
							# callerpy.CallerPy.truecaller(callerpy.country,PhoneNumber)
							raw_input(lines + '\nEnter to Back...')
							ClearScreen()
							PhoneInfo()
						else:
							raw_input(lines + '\nNothing Info\nEnter to Back...')
							ClearScreen()
							PhoneInfo()
		except:
			print '\n' + lines
			raw_input(Color.RED + Color.BOLD + '\n' + 'Not Find this person..' + Color.END)
			ClearScreen()
			PhoneInfo()

	else:
		EndScript()


def piplSearching (data):
	value = str(data).split(':')
	if 'Name' in value[0]:
		lName = value[1].split(' ')
		request = search.SearchAPIRequest(first_name = lName[0], last_name = lName[1]).default_api_key
	if 'Username' in value[0]:
		request = search.SearchAPIRequest(username = unicode(value[1]))
	if 'Email' in value[0]:
		request = search.SearchAPIRequest(email = unicode(value[1]))
	if 'Phone' in value[0]:
		request = search.SearchAPIRequest(raw_phone = unicode(value[1]))

	if request is not None:
		if CheckInternetConnection():
			# try:
			response = request.send()
			if response is not None:
				return response
			else:
				return None
		else:
			ClearScreen()
			PersonInfo()


def CheckInternetConnection ():
	import httplib
	try:
		con = httplib.HTTPConnection('www.google.com')
		con.request('HEAD', '/')
		return True
	except:
		print Color.RED + Color.BOLD + 'No Internet Connection' + Color.END
		return False


def EndScript ():
	print exit_msg;
	os._exit(0)


def ClearScreen ():
	os.system('cls' if os.name == 'nt' else 'clear')


def phone_format (n):
	return format(int(n[:-1]), ",").replace(",", "-") + n[-1]


def setLabel (Label):
	return Color.BOLD + Color.GREEN + Label + ' : ' + Color.END


def setNormalValue (Value):
	return Color.GREEN + Value + '.' + Color.END


def setMiddelValue (Value):
	return Color.YELLOW + Value + '.' + Color.END


def setGoodValue (Value):
	return Color.RED + Value + '.' + Color.END


Start()
