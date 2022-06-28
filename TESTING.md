# Table of Contents

- [Unit Testing](#unit-testing)
- [Manual Testing](#manual-testing)
    * [Feature 1 - Homepage and deals](#feature-1)
    * [Feature 2 - Navbar](#feature-2)
    * [Feature 3 - Footer](#feature-3)
    * [Feature 4 - Messages](#feature-4)
    * [Feature 5 - Bag](#feature-5)
    * [Feature 6 - Products](#feature-6)
    * [Feature 7 - Product categories](#feature-7)
    * [Feature 8 - Product details](#feature-8)
    * [Feature 9 - Product admin](#feature-9)
    * [Feature 10 - Newsletter](#feature-10)
    * [Feature 11 - Search bar](#feature-11)
    * [Feature 12 - Product sorting](#feature-12)
    * [Feature 13 - Profile info](#feature-13)
    * [Feature 14 - Order History](#feature-14)
    * [Feature 15 - User Sign in/up](#feature-15)
    * [Feature 16 - Checkout](#feature-16)
- [Validation](#validation)
    * [HTML](#html)
    * [CSS](#css)
    * [JavaScript](#javascript)
    * [Wave / Accessibility](#wave)
    * [Python](#python)

# Unit Testing
- I have written a total of 30 tests using the Django framework.
- They do not cover all files. I was about to test all core files (models, views, forms), yet I ran out of time.
- Those tests are structured based on the model/view structure, thus are named test_model/test_view.
- Coverage was used to check the total coverage of my tests.
- For the files I tested, I got 100% in all tests for the products.
- In the checkout app, I got 96% for the views, where I could not test some exceptions/errors and 71% for the models, where I ran out of time.

### Testing screenshots:
![Unit testing image](/docs/test.png)
<br>
![Unit testing coverage image](/docs/coverage_checkout_models.png)
<br>
![Unit testing coverage image](/docs/coverage_checkout_views.png)
<br>
![Unit testing coverage image](/docs/coverage_products_models.png)
<br>
![Unit testing coverage image](/docs/coverage_products_views.png)


# Manual Testing
### Feature 1 - Homepage and deals
#### User stories:
1) As a **potential customer** I can **see a home page** so that **I get information about the website/store**
3) As a **potential customer** I can **get to an offers page** so that **I can find deals on the products**

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Welcome text | Open page | See welcome text and image | Works as expected |
| Deals page | Open page > Look at second section | Find product deals and access them | Works as expected |

<details><summary>Screenshots</summary>

![Home page image](/docs/features/pages/home_top.png)
![Deals page image image](/docs/features/deals.png)

</details>

### Feature 2 - Navbar
#### User stories:
2. As a **potential customer** I can **get to the products page** so that **I find all available products**
5. As a **potential customer** I can **find a sign up button on the navigation** so that **I can sign up**
8. As a **potential customer** I can **find a sign in button on the navigation** so that **I can sign in easily**

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Navbar | Open page and look at top | See navbar | Works as expected |
| Navbar buttons | Press navbar buttons | Access menus | Works as expected |

<details><summary>Screenshots</summary>

![Navbar image](/docs/features/navbar.png)
![Products bar image](/docs/features/products_bar.png)
![User button image](/docs/features/user_button.png)

</details>

### Feature 3 - Footer
#### User stories:
2. As a **potential customer** I can **get to the products page** so that **I find all available products**
13. As a **potential customer** I can **find a social media link** so that **I can visit the store's social media account**

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Footer | Open page and scroll to bottom | See footer | Works as expected |
| Footer social links | Look at bottom of footer | See footer social links and access them | Works as expected |

<details><summary>Screenshots</summary>

![Footer image](/docs/features/footer.png)
![Footer image](/docs/features/social_links.png)

</details>

### Feature 4 - Messages
#### User stories:
16. As a **potential customer** I can **see confirmation or error messages** so that **I know whether an action was successful or failed**

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Django Messages | Make a POST action (add a product to bag, sign in, sign out, etc.) | See toast/message | Works as expected |

<details><summary>Screenshots</summary>

![Success message image](/docs/features/messages_success.png)

</details>

### Feature 5 - Bag
#### User stories:
9. As a **potential customer** I can **add items to my order without signing in** so that **I can make an order as a guest**
11. As a **potential customer** I can **add items to my order while signed in** so that **I can make an order as a user**
15. As a **potential customer** I can **see my bag** so that **products added in it are visible**

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Bag | Open page > Navigate to a product > Press add to bag | Product is added to visitor bag | Works as expected |

<details><summary>Screenshots</summary>

![Add to bag success image](/docs/features/proof/add_to_bag_success.png)
![Bag page image with product](/docs/features/proof/add_to_bag_success.png)

</details>

### Feature 6 - Products
#### User stories:
2. As a **potential customer** I can **get to the products page** so that **I find all available products**
9. As a **potential customer** I can **add items to my order without signing in** so that **I can make an order as a guest**
11. As a **potential customer** I can **add items to my order while signed in** so that **I can make an order as a user**

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| All products page | Open page > Click products hamburger menu > Press 'All products' | See all products page | Works as expected |

<details><summary>Screenshots</summary>

![Navbar products button image](/docs/features/navbar_products.png)
![Navbar products button image](/docs/features/products_bar.png)
![Products page image](/docs/features/pages/all_products.png)

</details>

### Feature 7 - Product categories
#### User stories:
2. As a **potential customer** I can **get to the products page** so that **I find all available products**
9. As a **potential customer** I can **add items to my order without signing in** so that **I can make an order as a guest**
11. As a **potential customer** I can **add items to my order while signed in** so that **I can make an order as a user**

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Products categories pages | Open page > Click products hamburger menu > Click on any category with any sorting | See the products in the category | Works as expected |

<details><summary>Screenshots</summary>

![Navbar products button image](/docs/features/navbar_products.png)
![Navbar products button image](/docs/features/products_bar.png)
![Example cases products image](/docs/features/pages/products_cases.png)

</details>

### Feature 8 - Product details
#### User stories:
14. As a **potential customer** I can **visit a product's details page** so that **I can learn more about it or add it to my bag**

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Product details page | Navigate to products and click on one or click on a deal | See the product's details page | Works as expected |

<details><summary>Screenshots</summary>

![Product details image](/docs/features/pages/product_details_top.png)
![Product details image](/docs/features/pages/product_details_bottom.png)

</details>

### Feature 9 - Product admin
#### User stories:
21. As a **website owner** I can **access an "add product" page** so that **I can easily add new products**
22. As a **website owner** I can **access an "edit product" page** so that **I can update its information**
23. As a **website owner** I can **delete a product** so that **it gets removed from the catalog**

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Add product | Sign in as admin > Press the User button > Press "Add product" > Choose category > Complete form | Product is added to catalog | Works as expected |
| Edit product | Sign in as admin > Navigate to a product's details > Press "Edit product" > Complete form | Product details are updated | Works as expected |
| Delete product | Sign in as admin > Navigate to a product's details > Press "Delete" > Confirm on model | Product is deleted | Works as expected |
| Add deal | Sign in as admin > Navigate to a product's details > Press "Add deal" > Complete form | Deal is added to deals page | Works as expected |

<details><summary>Screenshots</summary>

![Add product before image](/docs/features/proof/add_product_before.png)
![Add product after image](/docs/features/proof/add_product_after.png)
![Add product category picker image](/docs/features/proof/add_product_pick_case.png)
![Add product category picker image](/docs/features/proof/add_product_pick_mobo.png)
![Edit product before image](/docs/features/proof/edit_product_before.png)
![Edit product after image](/docs/features/proof/edit_product_after.png)
![Delete product before image](/docs/features/proof/delete_before.png)
![Delete product after image](/docs/features/proof/delete_after.png)
![Add deal before image](/docs/features/proof/add_deal_before.png)
![Add deal after image](/docs/features/proof/add_deal_after.png)

</details>

### Feature 10 - Newsletter
#### User stories:

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Newsletter signup form | Navigate to bottom of page | See newsletter sign up form > complete it and submit | Works as expected |

<details><summary>Screenshots</summary>

![Newsletter image](/docs/features/proof/newsletter_subscribe.png)

</details>

### Feature 11 - Search bar
#### User stories:
2. As a **potential customer** I can **get to the products page** so that **I find all available products**

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Search bar | On the navbar > Complete search query > Press the magnifying glass button to search | Products with the search query are displayed | Works as expected |

<details><summary>Screenshots</summary>

![Search before image](/docs/features/proof/search_before.png)
![Search after image](/docs/features/proof/search_after.png)

</details>

### Feature 12 - Product sorting
#### User stories:
2. As a **potential customer** I can **get to the products page** so that **I find all available products**

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Products sort by price | On products page > On the left of the page > Click on a price sorting method | Products are sorted by price | Works as expected |
| Products sort by rating | On products page > On the left of the page > Click on a rating sorting method | Products are sorted by rating | Works as expected |

<details><summary>Screenshots</summary>

![Price sorted products image](/docs/features/proof/sort_by_price.png)
![Rating sorted products image](/docs/features/proof/sort_by_rating.png)

</details>

### Feature 13 - Profile info
#### User stories:
18. As a **recurring customer** I can **use my profile information in an order** so that **I can complete my order faster**
20. As a **recurring customer** I can **edit my profile** so that **my information is up to date**

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Profile information | Sign in > Click on the user button > Press "My profile" > Edit information and submit | Information is saved | Works as expected |
| Profile information on checkout | Sign in > Add products to bag > Go to checkout | Checkout information is auto-completed with profile information | Works as expected |
| Profile information save on checkout | Sign in > Add products to bag > Go to checkout > Complete information > Tick "Save information to profile" | Information is saved to profile after checkout | Works as expected |

<details><summary>Screenshots</summary>

![Profile information on checkout image](/docs/features/proof/before_checkout.png)
![Profile information on profile image](/docs/features/proof/profile_update_before.png)
![Profile information after saving image](/docs/features/proof/profile_update_after1.png)
![Profile information on checkout after saving image](/docs/features/proof/profile_update_after2.png)

</details>

### Feature 14 - Order History
19. As a **recurring customer** I can **see my order history** so that **I know what I have ordered in the past**

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Profile order history | Sign in > Press user button > Press "My profile" | See order history on the right | Works as expected |

<details><summary>Screenshots</summary>

![Order history image](/docs/features/order_history.png)

</details>

### Feature 15 - User Sign in/up
7. As a **potential customer** I can **sign up for an account** so that **can access all that the website offers**

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Django Allauth sign up | Press the User button > Find "Register" button to sign up > Complete form | Have an account | Works as expected |
| Django Allauth sign in | Press the User button > Find "Log in" button to sign in > Complete form | Be logged in to the account | Works as expected |

<details><summary>Screenshots</summary>

![User button image](/docs/features/user_button.png)

</details>

### Feature 16 - Checkout
10. As a **potential customer** I can **complete an order without signing in** so that **I can make an order as a guest**
12. As a **potential customer** I can **complete an order while signed in** so that **I can make an order as a user**

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Checkout as user | Sign in > Add products to bag > Go to checkout > Complete form | Checkout is completed and order is successful | Works as expected |
| Checkout as visitor | Signed out > Add products to bag > Go to checkout > Complete form | Checkout is completed and order is successful | Works as expected |

<details><summary>Screenshots</summary>

![Checkout before image](/docs/features/proof/before_checkout.png)
![Checkout success image](/docs/features/proof/after_checkout.png)
![Guest Checkout before image](/docs/features/proof/guest_before_checkout.png)
![Guest Checkout success image](/docs/features/proof/guest_after_checkout.png)

</details>

# Validation

## HTML
- HTML was validated using the [Markup Validation Service](https://validator.w3.org/)
- The Validator unfortunately cannot validate pages that require signed in access


- The only errors are about list objects being inside the nav element, which should not be resolved as the nav elements were taken from Bootstrap

<details><summary>Screenshots</summary>

#### Home
![HTML homepage validation](/docs/validation/html/home.png)

#### Products
![HTML products validation](/docs/validation/html/all_products.png)

#### Product details
![HTML product details page validation](/docs/validation/html/product_details.png)

#### Bag
![HTML dashboard page validation](/docs/validation/html/bag.png)

#### Checkout
![HTML login page validation](/docs/validation/html/checkout.png)

#### Sign up
![HTML sign up page validation](/docs/validation/html/signup.png)

#### Sign in
![HTML sign in page validation](/docs/validation/html/login.png)

</details>

## CSS
- CSS was validated using the [CSS Validation Service](https://jigsaw.w3.org/css-validator/)
- No errors found

<details><summary>Screenshots</summary>

![CSS code validation](/docs/validation/base_css.png)
![CSS code validation](/docs/validation/checkout_css.png)

</details>

## JavaScript
- JavaScript was validated using the [JSHint](https://jshint.com/) page.
- JQuery and ES6 were enabled in the configuration.
- No errors found.

<details><summary>Screenshots</summary>

![JS code validation](/docs/validation/js/add_product.png)
![JS code validation](/docs/validation/js/bag_quantity_input.png)
![JS code validation](/docs/validation/js/base.png)
![JS code validation](/docs/validation/js/product_details.png)
![JS code validation](/docs/validation/js/products.png)
![JS code validation](/docs/validation/js/quantity_input.png)
![JS code validation](/docs/validation/js/stripe_elements.png)

</details>

## Wave / Accessibility
- Accessibility was tested with [Web Accessibility Evaluation Tool](https://wave.webaim.org/)
- There are 2 errors on the page and 3 contrast errors that were not fixed:
    * The 2 errors are about elements that don't have a value
    * An aria-label was added to both, but Wave seemed to ignore that code. Proof in screenshots
    * The contrast errors were left there on purpose, as they concerned 2 asterisks which were not meant to be read and the text-muted copyright statement, which is muted on purpose
- Wave cannot access pages that require signed in access
- Only 3 pages were able to be accessed

<details><summary>Screenshots</summary>

#### Validation
![WAVE home page validation](/docs/validation/wave/home.png)
![WAVE product details validation](/docs/validation/wave/product_details.png)
![WAVE products validation](/docs/validation/wave/products.png)

#### Proof
Error 1:<br>
![WAVE validation error 1](/docs/validation/wave_error1.png)
![WAVE validation proof 1](/docs/validation/wave_error1_proof.png)<br>
Error2:<br>
![WAVE validation error 2](/docs/validation/wave_error2.png)
![WAVE validation proof 2](/docs/validation/wave_error2_proof.png)

</details>

## Python
- For Python validation I used [PEP8 Online](http://pep8online.com/)
- I tested only files that I made changes to, not files that Django creates on its own and there was no input from me
- All files pass with no errors
- The noqa tag has been used only for errors in code that should not be altered

<details><summary>Screenshots</summary>

### Project level

#### settings.py
![PEP8 settings.py validation](/docs/validation/pep8/pep8_settings.png)

#### urls.py
![PEP8 urls.py validation](/docs/validation/pep8/pep8_urls.png)

### Bag

#### contexts.py
![PEP8 contexts.py validation](/docs/validation/pep8/pep8_bag_contexts.png)

#### urls.py
![PEP8 urls.py validation](/docs/validation/pep8/pep8_bag_urls.png)

#### views.py
![PEP8 views.py validation](/docs/validation/pep8/pep8_bag_views.png)

### Checkout

#### admin.py
![PEP8 admin.py validation](/docs/validation/pep8/pep8_checkout_admin.png)

#### forms.py
![PEP8 forms.py validation](/docs/validation/pep8/pep8_checkout_forms.png)

#### models.py
![PEP8 models.py validation](/docs/validation/pep8/pep8_checkout_models.png)

#### signals.py
![PEP8 signals.py validation](/docs/validation/pep8/pep8_checkout_signals.png)

#### test_models.py
![PEP8 test_models.py validation](/docs/validation/pep8/pep8_checkout_test_models.png)

#### test_views.py
![PEP8 test_views.py validation](/docs/validation/pep8/pep8_checkout_test_views.png)

#### urls.py
![PEP8 urls.py validation](/docs/validation/pep8/pep8_checkout_urls.png)

#### views.py
![PEP8 views.py validation](/docs/validation/pep8/pep8_checkout_views.png)

#### webhooks.py
![PEP8 webhooks.py validation](/docs/validation/pep8/pep8_checkout_webhooks.png)

#### webhook_handler.py
![PEP8 webhook_handler.py validation](/docs/validation/pep8/pep8_checkout_webhook_handler.png)

### Home

#### admin.py
![PEP8 admin.py validation](/docs/validation/pep8/pep8_home_admin.png)

#### forms.py
![PEP8 forms.py validation](/docs/validation/pep8/pep8_home_forms.png)

#### models.py
![PEP8 models.py validation](/docs/validation/pep8/pep8_home_models.png)

#### urls.py
![PEP8 urls.py validation](/docs/validation/pep8/pep8_home_urls.png)

#### views.py
![PEP8 views.py validation](/docs/validation/pep8/pep8_home_views.png)

### Products

#### admin.py
![PEP8 admin.py validation](/docs/validation/pep8/pep8_products_admin.png)

#### forms.py
![PEP8 forms.py validation](/docs/validation/pep8/pep8_products_forms.png)

#### models.py
![PEP8 models.py validation](/docs/validation/pep8/pep8_products_models.png)

#### test_models.py
![PEP8 test_models.py validation](/docs/validation/pep8/pep8_products_test_models.png)

#### test_views.py
![PEP8 test_views.py validation](/docs/validation/pep8/pep8_products_test_views.png)

#### urls.py
![PEP8 urls.py validation](/docs/validation/pep8/pep8_products_urls.png)

#### views.py
![PEP8 views.py validation](/docs/validation/pep8/pep8_products_views.png)

### Profiles

#### forms.py
![PEP8 forms.py validation](/docs/validation/pep8/pep8_profiles_forms.png)

#### models.py
![PEP8 models.py validation](/docs/validation/pep8/pep8_profiles_models.png)

#### urls.py
![PEP8 urls.py validation](/docs/validation/pep8/pep8_profiles_urls.png)

#### views.py
![PEP8 views.py validation](/docs/validation/pep8/pep8_profiles_views.png)

### Reviews

#### admin.py
![PEP8 admin.py validation](/docs/validation/pep8/pep8_reviews_admin.png)

#### forms.py
![PEP8 forms.py validation](/docs/validation/pep8/pep8_reviews_forms.png)

#### models.py
![PEP8 models.py validation](/docs/validation/pep8/pep8_reviews_models.png)

#### urls.py
![PEP8 urls.py validation](/docs/validation/pep8/pep8_reviews_urls.png)

#### views.py
![PEP8 views.py validation](/docs/validation/pep8/pep8_reviews_views.png)

</details>