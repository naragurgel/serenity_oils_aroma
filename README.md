# Serenity Oils - Essential Oils Aroma
Am I Responsive image HERE!

Serenity Oils is a online page that offers natural essential oils aromas, candles and diffusers. You can explore the benefits of aromatherapy with essential oils for relaxation, mindfulness, harmonious atmosphere and much more. 

You can view the deployed website [here](https://serenity-oils-3beb26e98281.herokuapp.com/).

## Github
[Serenity Oils](https://github.com/naragurgel/serenity_oils_aroma)
## Author
Nara Gurgel

## Contents
CREATE TABLE

## User Experience

### Strategy
#### Project Goals
* Build an easy to use and information website inviting online platform dedicated to promoting well-being through aromatherapy.
* Showcase a variety of natural essential oils, candles, and diffusers to create a serene ambiance.
* Ensure user can build and edit profile and orders.
* Create a user friendly payment mechanism.
* Provide valuable insights into the benefits of aromatherapy, fostering relaxation, mindfulness, and harmony.

### Structure
#### User Stories
- There are 26 user's stories were generated using an agile approach in a *"As a [role], I can [action], so that [benefit]"* format with acceptance criteria in declarative gherkin syntax.
- They were recorded as GitHub issues and integrated into a project board within GitHub. [here](https://github.com/users/naragurgel/projects/7) 
- This approach was employed throughout the development journey to construct the project through gradual increments.
- The order of implementation was as follows:
    - Home page and navigation.
    - Registration, login and logout features.
    - Products page with filter and sections.
    - Blog, Add favourits post to the favourits page.
    - Contact us and Testimonials.  
    - My bag and checkout.
    - Payment and confirmation of the order.
    - My profile page.
    - Footer with contact and social links.

|    	| **USER STORY**                                                                                                                                                                                 	| **PRIORITY** 	|
|----	|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|--------------	|
|    	| **_VIEWING AND NAVIGATION_**                                                                                                                                                                   	|              	|
| 1  	| As a user I can easily navigate the website using both desktop and mobile devices, so that I can have a consistent experience regardless of device.                                            	| HIGH         	|
| 2  	| As a shopper I can use the search bar to find a specific essential oil by its name or properties so that I can locate what I'm looking for easily.                                             	| HIGH         	|
| 3  	| As a visitor I can browse the homepage to quickly discover the range of essential oils available so that I can explore my options                                                              	| MEDIUM       	|
| 4  	| As a new user, I can easily find the social and contact information, so that I can reach out to them for more information.                                                                     	| HIGH         	|
| 5  	| As a user I can filter products by price, rating or category so that I can easily find products that meet my preference and needs                                                              	| HIGH         	|
| 6  	| As a wellness enthusiast, I can access a blog section with articles about the benefits of using essential oils, so that I can expand my knowledge.                                             	| MEDIUM       	|
| 7  	| As a shopper I can use the search bar to find a specific essential oil by its name or properties so that I can locate what I'm looking for easily.                                             	| MEDIUM       	|
|    	| **REGISTRATION AND ACCOUNTS**                                                                                                                                                                  	|              	|
| 8  	| As a new user I can create an account in the website so that I can easily manage my profile                                                                                                    	| HIGH         	|
| 9  	| As a returning customer I can log in to my account to quickly access my saved information to use on the checkout process so that I can save time.                                              	| MEDIUM       	|
| 10 	| As a existing user I can login and logout of the website so that I can access my account securely and protect my information when I'm done using the site.                                     	| HIGH         	|
| 11 	| As a user I can recover my password so that access my account again                                                                                                                            	| HIGH         	|
| 12 	| As a new user I can receive an email to verify my account after registering so that I can ensure the security of my account and access all the features of the website                         	| HIGH         	|
| 13 	| As a existing user I can have a personalized user profile so that I can update my personal information and view my order history                                                               	| MEDIUM       	|
| 14 	| As a user I can sent any request through the contact us form so that ask specific queries                                                                                                      	| MEDIUM       	|
| 15 	| As a user, I can sign up to receive a newsletter from Serenity Oils, so that I can get updates about the company and its services.                                                             	| MEDIUM       	|
| 16 	| As an authenticated user, I can view my profile information when logged in, so that I can ensure it is complete and up-to-date.                                                                	| HIGH         	|
| 17 	| As an authenticated user, I can write an optional rating/testimonial so that I can provide feedback about my experience.                                                                       	| MEDIUM       	|
| 18 	| As a new or authenticated user, I can be notified once completing actions on the website, so I know what I was doing.                                                                          	| HIGH         	|
| 19 	| As a user, I can easily connect with the social media accounts, so that I can learn more about the Serenity Oils.                                                                              	| LOW          	|
| 20 	| As a logged reader of the Serenity Oils blog I can mark my favorite blog posts so that I can easily access and revisit them whenever I need to.                                                	| LOW          	|
| 21 	| As a logged reader of the Serenity Oils blog I can delete any post from the list of favorites so that I keep it updated                                                                        	| LOW          	|
|    	| **_PRODUCTS, BAG, CHECKOUT AND PAYMENT _**                                                                                                                                                     	|              	|
| 23 	| As a customer I can read detailed descriptions of each essential oil's benefits and uses so that I can make informed purchasing decisions.                                                     	| MEDIUM       	|
| 24 	| As a buyer I can view the total of my purchase on the website so that I can see the cost of all the item in my cart                                                                            	| HIGH         	|
| 25 	| As a potential buyer I can view customer reviews and testimonials so that I can gain confidence in the quality of the essential oils.                                                          	| LOW          	|
| 26 	| As a curious shopper I can explore a "New Arrivals" section to discover the latest additions to the product lineup so that I can stay up-to-date.                                              	| LOW          	|
| 27 	| As a shopper I can change quantity of individual items in my shopping bag so that I can easily make changes to my purchase before proceeding to checkout                                       	| HIGH         	|
| 28 	| As a shopper I can delete items from my shopping bag so that I can make changes to my purchase before proceeding to checkout                                                                   	| HIGH         	|
| 29 	| As a customer I can view the order summary, including the selected products, their quantities and grand total so that I can check that everything is right before procced with the transaction 	| HIGH         	|
|    	| **_ADMIN_**                                                                                                                                                                                    	|              	|
| 30 	| As a admin I can add new products to the website so that I can keep the product catalogue up-to-date                                                                                           	| HIGH         	|
| 31 	| As a Admin I can delete products or edit on the website, such as name, description, price, images and category so that I can maintain accurate and relevant product information                	| HIGH         	|
| 32 	| As a admin I can manage the reviews received on the website so that I can make sure they are real and appropriate for the page                                                                 	| MEDIUM       	|
| 33 	| As a Admin I can access customer orders, total of each order and product details so that I can create a efficient user experience and have a better control of product and stock.              	| HIGH         	|
| 34 	| As a admin I can create, update, edit and delete any post on the blog so that I can manage the content effectively                                                                             	| MEDIUM       	|