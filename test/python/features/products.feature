Feature: Product Management
 
  Scenario: Reading a Product
    Given the following products exist:
      | id | name          | category     | price | available |
      | 1  | Product A     | Category 1   | 10.00 | true      |
      | 2  | Product B     | Category 2   | 20.00 | true      |
    When I request to read the product with id "1"
    Then the response should contain:
      | id   | 1            |
      | name | Product A    |
      | category | Category 1 |
      | price | 10.00       |
      | available | true    |
 
  Scenario: Updating a Product
    Given the following products exist:
      | id | name          | category     | price | available |
      | 1  | Product A     | Category 1   | 10.00 | true      |
      | 2  | Product B     | Category 2   | 20.00 | true      |
    When I search for the product with name "Product A"
    Then I should see the message "Success"
    And the field "price" should have the value "10.00"
    When I change the "price" field to "15.00" and press the Update button
    Then I should see the message "Success"
    When I copy the "id" field, clear the form, paste the "id" field, and press the Retrieve button
    Then I should see the message "Success"
    And the field "price" should have the value "15.00"
    
  Scenario: Deleting a Product
    Given the following products exist:
      | id | name          | category     | price | available |
      | 1  | Product A     | Category 1   | 10.00 | true      |
      | 2  | Product B     | Category 2   | 20.00 | true      |
    When I search for the product with name "Product A"
    Then I should see the message "Success"
    And the field "price" should have the value "10.00"
    When I copy the "id" field, clear the form, paste the "id" field, and press the Delete button
    Then I should see the message "Product has been Deleted!"
    When I press the Clear button followed by the Search button
    Then the product should not be in the results
    
  Scenario: Listing All Products
    Given the following products exist:
      | id | name    | category     | price | available |
      | 1  | Hat     | Accessories  | 15.00 | true      |
      | 2  | Shoes   | Footwear     | 50.00 | true      |
      | 3  | Big Mac | Food         | 5.00  | true      |
      | 4  | Sheets  | Home Goods   | 20.00 | true      |
    When I press the Clear button
    And I press the Search button
    Then I should see the message "Success"
    And I should see all the products listed:
      | name    |
      | Hat     |
      | Shoes   |
      | Big Mac |
      | Sheets  |
      
  Scenario: Searching a Product Based on Category
    Given the following products exist:
      | id | name    | category     | price | available |
      | 1  | Hat     | Accessories  | 15.00 | true      |
      | 2  | Shoes   | Footwear     | 50.00 | true      |
      | 3  | Big Mac | Food         | 5.00  | true      |
      | 4  | Sheets  | Home Goods   | 20.00 | true      |
    When I press the Clear button
    And I select the category "Food"
    And I press the Search button
    Then I should see the message "Success"
    And I should see the following product in the results:
      | name    |
      | Big Mac |
    And I should not see the following products in the results:
      | name   |
      | Hat    |
      | Shoes  |
      | Sheets |
      
  Scenario: Searching a Product Based on Availability
    Given the following products exist:
      | id | name    | category     | price | available |
      | 1  | Hat     | Accessories  | 15.00 | true      |
      | 2  | Shoes   | Footwear     | 50.00 | true      |
      | 3  | Big Mac | Food         | 5.00  | false     |
      | 4  | Sheets  | Home Goods   | 20.00 | true      |
    When I set the availability dropdown to "True"
    And I press the Search button
    Then I should see the message "Success"
    And I should see the following available products in the results:
      | name   |
      | Hat    |
      | Shoes  |
      | Sheets |
    And I should not see the following unavailable product in the results:
      | name    |
      | Big Mac |
      
  Scenario: Searching a Product Based on Name
    Given the following products exist:
      | id | name    | category     | price | available |
      | 1  | Hat     | Accessories  | 15.00 | true      |
      | 2  | Shoes   | Footwear     | 50.00 | true      |
      | 3  | Big Mac | Food         | 5.00  | false     |
      | 4  | Sheets  | Home Goods   | 20.00 | true      |
    When I set the product name field to "Hat"
    And I press the Search button
    Then I should see the message "Success"
    And I should see the following product in the results:
      | name |
      | Hat  |
    And I should not see the following products in the results:
      | name    |
      | Shoes   |
      | Big Mac |
      | Sheets  |
      
  
