from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import password_generator as pg
import random as r
from selenium.webdriver import ActionChains
import excel_data as ed

def runner(fname,lname,country,status,gender,blood_group,driving_license,expiry_date,birth_date,job_title,sub_unit,employment_status,doj):
    #openURL
    driver = webdriver.Chrome()
    driver.maximize_window()

    #Hit url
    try:
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)
        print("+++Url hit successful+++")
    except:
        print("---Url hit unsuccessful---")

    #Login page
    try:
        wait(driver, 90).until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/h5')))
        time.sleep(5)
        print("+++Login page loaded successfully+++")
    except:
        print("---Login page open unsuccessful---")

    #Give id & password
    try:
        driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("Admin")
        time.sleep(3)
        print("+++User id given successfully+++")
        driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys("admin123")
        time.sleep(3)
        print("+++Password given successfully+++")
    except:
        print("---Unable to insert Id & Password---")

    #Click login button
    try:
        wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'))).click()
        time.sleep(3)
        print("+++Login button click successfully+++")
    except:
        print("---Unable to click login button---")

    #check id password are correct or not
    try:
        wait(driver, 30).until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p')))
        print("Please give correct id & password")
        driver.quit()
    except:
        pass

    #Check dashboard is open or not
    try:
        wait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[1]/div[1]/span/h6')))
        print("+++Dashboard loaded successfully+++")
        time.sleep(1)
    except:
        print("---Unable to load dashboard page---")

    #Select PIM
    try:
        wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a'))).click()
        time.sleep(2)
        print("+++Click on PIM successful+++")    
    except:
        print("---Unable to select PIM---")

    # #Check all othe info
    # try:
    #     wait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[1]/div/div[1]/div/label/span'))).click()
    #     # print("+++Admin page loaded successfully+++")
    #     print("+++All details select successfully+++")
    #     time.sleep(3)
    # except:
    #     print("---Unable to select all info---")

    # #Delete all previous info
    # try:
    #     wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div/button'))).click()
    #     print("+++All previous INFO deleted successfully+++")
    #     time.sleep(3)
    # except:
    #     print("---Unable to delete previous INFOs---")

    # #Confirm to delete
    # try:
    #     wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]'))).click()
    #     print("+++Old records Delete confirm+++")
    #     time.sleep(5)
    # except:
    #     print("---Unable to confirm delete previous INFOs---")

    #Goto add employee
    try:
        wait(driver,30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/a'))).click()
        print("+++PIM page loaded successfully+++")
        print("+++Click on add employee successful+++")
        time.sleep(2)
    except:
        print("---Unable to click on add employee---")

    #upload img
    try:
        # driver.switch_to_frame()
        wait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[1]/div/div[2]/input'))).send_keys("D:\myProject\img\images.jpg")
        print("+++Upload picture successfully+++")
        time.sleep(3)
    except:
        print("---Unable to upload picture---")

    #provide add employee details
    try:
        # fname = "Naruto"
        # lname = "Uzumaki"
        emp_id = r.randint(111,999)
        wait(driver,30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input'))).send_keys(fname)
        print("+++First name given successfully+++")
        time.sleep(1)
        wait(driver,30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input'))).send_keys(lname)
        print("+++Last name given successfully+++")
        time.sleep(1)
        for i in range(4):
            wait(driver,30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input'))).send_keys(Keys.BACKSPACE)
        time.sleep(2)
        print("+++Employee id text box clear successfully+++")
        wait(driver,30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input'))).send_keys(emp_id)
        time.sleep(2)
        print("+++Employee id given successfully+++")
    except:
        print("---Unable to provide the 'Add Employee' INFO---")

    #Save add employee details
    try:
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]').click()
        time.sleep(7)
        print("+++Employee details saved successfully+++")
    except:
        print("---Unable to save employee details---")

    #Personal details page
    try:
        wait(driver,30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/h6')))
        print("+++Personal details page loaded successfully+++")
        time.sleep(2)
    except:
        print("---Personal details page not loaded---")

    #Personal details full up
    try:
        wait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input'))).send_keys(driving_license)
        print("+++Driver's License Number provided+++")
        time.sleep(1)
        wait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input'))).send_keys(expiry_date) #"2026-12-01"
        print("+++License Expiry Date provided+++")
        time.sleep(1)
        # wait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[1]/div/div[2]/input'))).send_keys("26648")
        # print("+++SSN Number provided+++")
        time.sleep(7)
        # wait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[2]/div/div[2]/input'))).send_keys("156487")
        # print("+++SIN Number provided+++")
        try:
            driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[2]/i').click()
            print("+++click on nation+++")
            time.sleep(2)
            nations = driver.find_elements(By.XPATH, '//div[@class = "oxd-select-option"]')
            for nation in nations:
                if nation.text.__contains__(country): #"India"
                    nation.click()
                    print("+++Successfully select nation+++")
                    break
        except:
            print("---Unable to select nation---")

        time.sleep(5)

        try:
            driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[2]/i').click()
            print("+++click on status+++")
            time.sleep(2)
            nations = driver.find_elements(By.XPATH, "//div[@class = 'oxd-select-option']")
            for nation in nations:
                if nation.text.__contains__(status): #"Single"
                    nation.click()
                    print("+++Successfully select status+++")
                    break
        except:
            print("---Unable to select status---")
                
        time.sleep(5)

        wait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input'))).send_keys(birth_date) #"1998-06-02"
        print("+++birth date provided successfully+++")
        time.sleep(3)

        try:
            # driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label/span').click()
            # print("+++Select male option successfully+++")
            genders = driver.find_elements(By.XPATH, "//div[@class = 'oxd-radio-wrapper']/label")
            # print(gender.text)
            for g in genders:
                print(g.text)
                # if g.text.__contains__(gender): #"Male"
                if gender == "Male":
                    if g.text.__contains__(gender):
                        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label/span').click()
                        print("+++Select male option successfully+++")
                        time.sleep(3)
                        break

                else:
                    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/label/span').click()
                    print("+++Select female option successfully+++")
                    time.sleep(3)
                    break
        except:
            print("---Unable to select gender---")

        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button').click()
        print("+++Click on 1st submit button successfully+++")
        time.sleep(3)

        try:
            driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div/div/div[2]/div/div/div[2]/i').click()
            time.sleep(5)
            blood_groups = driver.find_elements(By.XPATH, "//div[@class = 'oxd-select-option']")
            for type in blood_groups:
                # print(type.text)
                if(type.text == blood_group):
                    type.click()
                    print("+++Successfully select blood group+++")
                    time.sleep(3)
                    break
        except:
            print("---Unable to choose blood group---")

        wait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[2]/button'))).click()
        print("+++2nd submit option click successfully+++")
        time.sleep(7)
    except:
        print("---Unable to pass Details---")

    #Job section
    try:
        time.sleep(4)
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[10]/a').click()
        time.sleep(5)
        print("++++Clisk on qualifications successfully++++")
        wait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[6]/a'))).click()
        print("+++Job section clicked loaded successfully+++")
        time.sleep(5)
        wait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/h6')))
        print("+++Job details page loaded successfully+++")
        time.sleep(7)

        #inputs
        wait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div/input'))).send_keys(doj) #"2023-03-12"
        print("+++DOJ provided successfully+++")
        time.sleep(1)

        try:
            driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div/div[2]/i').click()
            print("+++Click on job title successfully+++")
            time.sleep(2)
            job_titles = driver.find_elements(By.XPATH, '//div[@class = "oxd-select-option"]')
            for title in job_titles:
                # print(title.text)
                if(title.text.__contains__(job_title)): #"QA Engineer"
                    title.click()
                    print("+++Successfully select job title+++")
                    time.sleep(5)
                    break
        except:
            print("---Unable to select job title---")

        try:
            driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/div/div/div[2]/i').click()
            print("+++Click on sub unit successfully+++")
            time.sleep(2)
            subunits = driver.find_elements(By.XPATH, '//div[@class = "oxd-select-option --indent-2"]')
            for title in subunits:
                # print(title.text)
                if(title.text.__contains__(sub_unit)): #"Quality Assurance"
                    title.click()
                    print("+++Successfully select sub unit+++")
                    time.sleep(5)
                    break
        except:
            print("---Unable to select sub unit---")

        try:
            wait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[7]/div/div[2]/div/div/div[2]/i'))).click()
            print("+++Successfully click on employment status+++")
            time.sleep(3)
            empstatus = driver.find_elements(By.XPATH, '//div[@class = "oxd-select-option"]')
            for emp in empstatus:
                # print(emp.text)
                if(emp.text == employment_status): #"Full-Time Contract"
                    emp.click()
                    print("+++Select employment status successfully+++")
                    time.sleep(5)
                    break
        except:
            print("---Unable to select employment status---")

        try:
            wait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button'))).click()
            print("+++Successfully submit job details+++")
            time.sleep(5)
        except:
            print("---Unable to submit---")

    except:
        print("---Unable to goto job section---")

    try:
        wait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a'))).click()
        print("+++Successfully click on Employee List+++")
        time.sleep(7)

    except:
        print("---Unable to click on---")

    try:
        act=ActionChains(driver)
        names = driver.find_elements(By.XPATH, "//div[@class = 'oxd-table-cell oxd-padding-cell']")
        for name in names:
            if(name.text.__contains__(fname)):
                act.move_to_element(name).perform()
                print("+++Successfully hover on latest employee details+++")
                time.sleep(18)
                break
        
    except:
        print("---Unable to hover on current employee record---")

excel_data_list = ed.excel_datas()
# print(excel_data_list[0][0])
for row_num in range(len(excel_data_list)):
    fname = excel_data_list[row_num][0]
    lname = excel_data_list[row_num][1]
    country = excel_data_list[row_num][2]
    status = excel_data_list[row_num][3]
    gender = excel_data_list[row_num][4]
    blood_group = excel_data_list[row_num][5]
    driving_license = excel_data_list[row_num][6]
    expiry_date = excel_data_list[row_num][7]
    birth_date = excel_data_list[row_num][8]
    job_title = excel_data_list[row_num][9]
    sub_unit = excel_data_list[row_num][10]
    employment_status = excel_data_list[row_num][11]
    doj = excel_data_list[row_num][12]
    time.sleep(7)
    runner(fname,lname,country,status,gender,blood_group,driving_license,str(expiry_date).split()[0],str(birth_date).split()[0],job_title,sub_unit,employment_status,str(doj).split()[0])


# print(fname)
# print(lname)
# print(country)
# print(status)
# print(gender)
# print(blood_group)
# print(driving_license)
# print(str(expiry_date).split()[0])
# print(str(birth_date).split()[0])
# print(job_title)
# print(sub_unit)
# print(employment_status)
# print(str(doj).split()[0])