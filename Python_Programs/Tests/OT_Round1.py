[11:09 AM] Sushma Bandarupalli (Guest)
    select A.id, A.employee_name from a_employee A join on b_employee B where A.id = B.id
​[11:22 AM] Sushma Bandarupalli (Guest)
    
def fibo(n):


    if n == 0:
        return 0
    if n == 1:
        return 1
    if n < 0:
        return "Incorrect number"
    lst = [1]
    s = 1
    while s < n:
        lst.append(s)
        s += lst[-1]
    return lst


n = 10    
print(fibo(n))
    
1     
# 1 1 2 3 5 8
s = 1
i = 1
print(1)
s = i + s
s = 1+1
print(2)
s = 2 + 




​[11:47 AM] Sushma Bandarupalli (Guest)
    
# TC1 login with correct credentails
# TC2 login with incorrect credentials (login/password/both)
# TC3 password masking


from selenium import webdriver
#import By
#driver initialisation


Login ------
Password ------
Login button ------


def test_login():
    driver.get("url")
    # driver.title, assert can be done for title, to make sure we got into correct page
    # find login text box and enter data
    driver.find_by_element(By.XPATH,"xpath").sendkeys("testuser")
    # find password text box and enter data
    password = "password@test"
    driver.find_by_element(By.XPATH,"xpath").sendkeys("password")
    # to check masking
    password_text = driver.find_by_element(By.XPATH,"xpath").text
    assert password != password_text, "password in't masked"
    # click on login button
    driver.find_by_element(By.LINK_TEXT,"link_text").click
    # waits can be added, if page takes time to login
    # if Login text is visible, it's pass
    # return message for failure
    assert driver.switch_to.alert().text == 'Login successful',  'Login Failed'





​[11:47 AM] Sushma Bandarupalli (Guest)
    ps
​[11:47 AM] Sushma Bandarupalli (Guest)
    ps aux
