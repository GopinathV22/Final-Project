from behave import when
from selenium import webdriver
 
@when('I press the "{button_name}" button')
def step_impl(context, button_name):
    button = context.browser.find_element_by_name(button_name)
button.click()

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
 
# Task 7b: Step Definition for verifying a specific name or text to be present
@then('I should see "{text}" in the page')
def step_impl(context, text):
    assert text in context.browser.page_source, f'Expected text "{text}" not found in the page.'
 
# Task 7c: Step Definition for verifying a specific name or text NOT to be present
@then('I should not see "{text}" in the page')
def step_impl(context, text):
    assert text not in context.browser.page_source, f'Unexpected text "{text}" found in the page.'
    

 #Task 7d : Step Definition for verifying a specific message is present
@given('I am on the homepage')
def step_given_i_am_on_the_homepage(context):
    context.browser = webdriver.Chrome()
    context.browser.get('http://example.com')
 
@when('I look for a message containing "{message}"')
def step_when_i_look_for_a_message(context, message):
    context.message = message
    context.page_source = context.browser.page_source
 
@then('I should see the message "{message}"')
def step_then_i_should_see_the_message(context, message):
    assert message in context.page_source, f"Expected message '{message}' not found."
    context.browser.quit()
 