import datetime

def date_convert(s_date):
	month_dict = {'Jan':'01','Feb':'02','Mar':'03', 'Apr':'04', 'May':'05',
                  'Jun':'06', 'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10',
                  'Nov':'11', 'Dec':'12'}

	month = month_dict[s_date[:3]]
	day = s_date[4:6]
	hour_min = s_date[7:12]

	return  str(datetime.datetime.now().year) + '-' +month+ '-' +day+ 'T' +hour_min+ ':00'

print date_convert('Jul 25 16:20')
