from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import prettytable


driver = webdriver.Chrome('C:\/chromedriver.exe')
driver.get("https://ossc.ca/player-home-and-dashboard/day-to-day-info/schedules/4597")

actions = ActionChains(driver)

element = driver.find_elements_by_id("user_email")[1]
actions.move_to_element(element).click().send_keys("<user_email>" + Keys.TAB + "<user_password>" + Keys.ENTER).perform()

go_to_league_page = driver.get("https://ossc.ca/player-home-and-dashboard/day-to-day-info/schedules/4597")

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, 'moduleid-sports_schedules-index')))

get_table_elements = driver.find_elements_by_xpath("//*[@id=\"moduleid-sports_schedules-index\"]/table[2]/tbody")

table = []
table = prettytable.PrettyTable(
["Date", "Team", "Time", "Place", "Diamond Location"])

for elem in get_table_elements:
	matchingString = [s for s in elem.text.split("\n") if "PLAYOFFS" not in s]
	if len(matchingString) >1:
		splitMatchingString = matchingString[2].split("PM")
		matchedObjectTime = re.search("([0-9]:[0-9]*\w+)", matchingString[2], flags=0)
		matchedObjectPlace=re.search("([a-zA-Z]+\s+[a-zA-Z]+\s)-", matchingString[2],flags=0)
		matchedObjectDiamond = re.search("-((\s\w+)*)", matchingString[2],flags=0)
	empList= []
	if elem.text and matchingString :
		empList.append(elem.text.split("\n")[0])
		empList.append(elem.text.split("\n")[1])
		empList.append(matchedObjectTime.group(1))
		if "Public"  in matchedObjectPlace.group(1):
			empList.append("Regina "+matchedObjectPlace.group(1))
		elif "Wood" in matchedObjectPlace.group(1):
			empList.append("Elizabeth "+matchedObjectPlace.group(1))
		else:
			empList.append(matchedObjectPlace.group(1))
		empList.append(matchedObjectDiamond.group(1))
		table.add_row(empList)

print("PrettyTable: \n",table)
