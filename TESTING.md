# Serenity Oils - Essential Oils Aroma

![image (6)](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/555b82f9-f9c6-4304-a70d-6e1ac8239e1a)

You can view the deployed website [here](https://serenity-oils-3beb26e98281.herokuapp.com/).

## Manual Testing

I've create manual testing and added to the test [backlog](https://github.com/users/naragurgel/projects/8).

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/a6992f93-3baf-46db-9392-d98ac9d1f696)

[Here](https://github.com/naragurgel/serenity_oils_aroma/issues?q=is%3Aissue+is%3Aopen+label%3ATEST_CASE) is the list with all tests created. They are labelled as TEST_CASE and each one has the steps I've taken during the process and the conclusion. 
The template used was: 

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/58b08896-3996-4580-a3c9-36e0a9517172)

### Manual Testing: 

[Serenity Oils Homepage](https://github.com/naragurgel/serenity_oils_aroma/issues/35)

[Registration Process](https://github.com/naragurgel/serenity_oils_aroma/issues/37)

[Login](https://github.com/naragurgel/serenity_oils_aroma/issues/38)

[Serenity Oils Products Page- Products Details](https://github.com/naragurgel/serenity_oils_aroma/issues/39)

[Bag](https://github.com/naragurgel/serenity_oils_aroma/issues/40)

[Checkout Page](https://github.com/naragurgel/serenity_oils_aroma/issues/41)

[User Profile Page- Authenticated User](https://github.com/naragurgel/serenity_oils_aroma/issues/42)

[Admin - Product Management](https://github.com/naragurgel/serenity_oils_aroma/issues/43)

[Logout](https://github.com/naragurgel/serenity_oils_aroma/issues/44)

[Blog page, Post Details and Favorite Post Page](https://github.com/naragurgel/serenity_oils_aroma/issues/45)

[Contact Us Page](https://github.com/naragurgel/serenity_oils_aroma/issues/46)

[Testimonials](https://github.com/naragurgel/serenity_oils_aroma/issues/47)

[Nav bar non-authenticated and authenticated user](https://github.com/naragurgel/serenity_oils_aroma/issues/48)

## Accessibility Testing

[Serenity Oils Homepage]()

[Registration Process]()

[Login]()

[Serenity Oils Products Page- Products Details]()

[Bag]()

[Checkout Page]()

[User Profile Page- Authenticated User]()

[Admin - Product Management]()

[Logout]()

[Blog page, Post Details and Favorite Post Page]()

[Contact Us Page]()

[Testimonials]()

[Nav bar non-authenticated and authenticated user]()

## Validation Testing
🚨**Required**

You should try to ensure you code is valid and follows proper indentation. In this section you should write up any
websites you used to validate your code so there is credit given to those sites. Then add links to the test cases you
put into GitHub for the validation. You can copy your validation success to those tests.

The following site were used to aid in validation testing:

- **[CSS Validator](https://jigsaw.w3.org/css-validator/)**

> If you only have one CSS file, you can just run the validator through one deployed page URL, if you have custom CSS for diffent pages, make sure you hit those different URLS

- **[HTML Validator](https://validator.w3.org/)**

> For each view you wrote, you should validate the HTML and have a test case for it linked to from here
> NOTE: You may need to right-click to view the source of each page and paste that into the validator if you need to go through authentication to get to the page.

- **[JS validation](https://jshint.com)**

> for each .js file, copy the code and paste it into this site, and have a test case for it linked to from here. You can have warnings, but no errors.
> if using ES6, add this before pasting in your file: `/*jshint esversion: 6 */ `, similarily you can update it to 7 if you see warnings about ES7 syntax `/*jshint esversion: 7 */ `

- **[CI's pep8 tool](https://pep8ci.herokuapp.com/)** 

> for each .py file you created, copy the source code and paste it into this site, and have a test case for it linked to from here.
> include a screenshot of results in the test case showing NO ERRORS. (you should do this for all .py files in your repo)
> 
> **run.py**
> 
> ![image](https://user-images.githubusercontent.com/23039742/212106175-36b2f18a-7c75-458d-94dd-9886e81c71f3.png)

> Ideally you would have no errors remaining outside of line too long which you can fix by 
> 
> adding
> ```$python 
> # noqa
> ```
> There is a space before the # and after it to skip the quality assurance for that line.
> 
> Note any errors or warnings you are ignoring and why.

- **[JSON validation](https://jsonlint.com/)**

> for each .json file, you should copy the code and paste it into this site, and have a test case for it linked to from here.

## Automated Testing
🚀 **merit & beyhond**

**NOTE: If you want MERIT or Higher, you MUST have some automated testing**
If you managed to write jasmine tests or some django tests, note those files out here and how to run them.

https://github.com/maliahavlicek/ms4_challenger/blob/master/documentation/TESTING.md is my write up about my automated testing and how I ran them, but a simple test I'd recommend is a views test that tests authentication and any views you limit to superusers or logged in users.

https://github.com/maliahavlicek/ms4_challenger/blob/master/challenges/tests/test_views.py

## Defects
🚨**Required**

At this point you really should be using GITHUB's Issues to track these as it helps you with the AGILE process
requirement as it's really easy to copy/paste screenshots in and then write up how you closed them.

[Here's a brief overview](https://docs.google.com/document/d/1nDS5tZeMO77Dfq85IZGMSV6C41XaPm9FwcpR3k-UTVc/edit#heading=h.542xzc8ufx4x)
I put together on how to do this.

is what my custom tempalte looks like in the UX
![image](https://user-images.githubusercontent.com/23039742/165650359-a352d64e-b128-473d-ab60-7df0568a44df.png)

## Defects of Note
🚀 **merit & beyhond**

Some defects are more pesky than others. Highlight 3-5 of the bugs that drove you the most nuts and how you finally
ended up resolving them. Just create a link to the issues/defect of note.

### Outstanding Defects

It's ok to not resolve all the defects you found. If you know of something that isn't quite right, list it out and
explain why you chose not to resolve it. Again, do this in gitHub and provide a link to the defects you are not closing
and ensure they have a comment in them.