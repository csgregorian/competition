dictionary = {"CU": "see you",
":-)":	"I'm happy",
":-(":	"I'm unhappy",
";-)":	"wink",
":-P":	"stick out my tongue",
"(~.~)":	"sleepy",
"TA":	"totally awesome",
"CCC":	"Canadian Computing Competition",
"CUZ":	"because",
"TY": "thank-you",
"YW":	"you're welcome",
"TTYL":	"talk to you later"}

short = input()

while True:
	print(dictionary[short] if dictionary.get(short) else short)
	if short == "TTYL":
		break

	short = input()
