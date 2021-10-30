#	log file probleml
'''
file gererated at (09:09 PM | 30/10/2021)
[warnings]
Exception error ln(32) 09:10
This script has not found ln(40) 09:10

[alerts]
add a class ln(20) 09:09

[total]
w 2
a 1
'''

import datetime, time
from os import error

class Probleml:
	SEC_WARNINGS = "Warnings"
	SEC_INFOS = "Infos"
	SEC_DEBUGS = "Debugs"
	SEC_ERRORS = "Errors"
	SEC_CRITICALS = "Criticals"
	SEC_TOTAL = "Total"

	def __init__(self) -> None:
		self.log_sections = []
		self.log_values = []

		self.logs = {
			self.SEC_WARNINGS: [],
			self.SEC_ERRORS: [],
			self.SEC_DEBUGS: [],
			self.SEC_CRITICALS: [],
			self.SEC_INFOS: [],
			self.SEC_TOTAL: {
				self.SEC_WARNINGS: 0,
				self.SEC_ERRORS: 0,
				self.SEC_DEBUGS: 0,
				self.SEC_INFOS: 0,
				self.SEC_CRITICALS: 0
			}
		}
		pass

	def write(self, section = SEC_WARNINGS, message = "-message-"):
		data = []
		data.append(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
		data.append(section)
		data.append(message)
		self.logs[section].append(data)
		pass

	def generate(self, custom_filename = "problem.lg"):
		#	create log file with sctions
		for key_names in self.logs[self.SEC_TOTAL]:
			self.logs[self.SEC_TOTAL][key_names] = len(self.logs[key_names]) #	count sections and reports

		with open(custom_filename, "a") as file:
			file.writelines("@{}\n".format(datetime.datetime.now().strftime("%d/%m/%Y & %H:%M:%S")))
			for sec_names in self.logs.keys():
				file.writelines("\n[{}]\n".format(sec_names))#	make section name

				if sec_names != self.SEC_TOTAL:
					sec_values_arr = self.logs[sec_names]
					if len(sec_values_arr) > 0:
						for i in range(len(sec_values_arr)):
							line_str = "{} -> {} -> {}\n".format(
								sec_values_arr[i][0],
								sec_values_arr[i][1],
								sec_values_arr[i][2]
							)
							file.writelines(line_str)
					else:
						file.writelines("#nothing to report!\n")
				else:
					for key_n in self.logs[sec_names].keys():
						file.writelines("{}: {}\n".format(key_n, self.logs[sec_names][key_n]))
		
		print("log created at {}".format(custom_filename))
		pass
"""
log = Probleml()
log.write(section=log.SEC_DEBUGS, message="log debug message")
log.write(section=log.SEC_DEBUGS, message="log debug message")
log.write(section=log.SEC_WARNINGS, message="log warning message")
log.write(section=log.SEC_CRITICALS, message="log critical message")
log.generate()
"""