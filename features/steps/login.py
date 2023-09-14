from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@given('I launch chrome browser')
def open_browser(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


@when('I got navigated to login page')
def open_login_page(context):
    context.driver.get("https://www.beerwulf.com/en-nl/my-account/Login?ReturnUrl=/en-NL/AccountInformation/OrderHistory")


@when('I enter in Email with "{email}"')
def enter_email(context, email):
    username_locator = context.driver.find_element(By.CSS_SELECTOR, "[name='Email']")
    username_locator.send_keys(email)


@when('I enter in Password with "{password}"')
def enter_password(context, password):
    password_locator = context.driver.find_element(By.CSS_SELECTOR, "[name='Password']")
    password_locator.send_keys(password)


@when('I press "Login"')
def press_log_in(context):
    submit_button_locator = context.driver.find_element(By.XPATH, "//button[text()='Log in']")
    submit_button_locator.click()
    time.sleep(2)


@then('I should be in loggen in url')
def step_impl(context):
    pass

@then('I should see logged in user icon')
def is_user_logged_in_icon_displayed(context):
    pass

@then('I should see "Logout" button')
def is_logout_button_displayed(context):
    pass
#
# @then('I should see error message')
# def step_impl(context):
#     pass