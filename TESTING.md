# Serenity Oils - Essential Oils Aroma

![image (6)](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/555b82f9-f9c6-4304-a70d-6e1ac8239e1a)

You can view the deployed website [here](https://serenity-oils-3beb26e98281.herokuapp.com/).

# Table of contents

- [Testing](#testing)
  - [Cross Browser and Cross Device Testing](#cross-browser-and-cross-device-testing)
  - [Manual Testing](#manual-testing)
  - [Accessibility Testing](#accessibility-testing)
  - [Validation Testing](#validation-testing)
  - [Defects](#defects)
    
# Testing
## Cross Browser and Cross Device Testing

- I've tested the compatibility and visual appeal of the website on different platforms, the appearance and the website functions are working normally on all this devices:

| Tool/Device    | Browser | OS            | Viewport       |
|----------------|---------|---------------|----------------|
| Iphone 14 Plus | Safari  | V16.0         | 1284 x 2778 px |
| Iphone 13      | Safari  | V16.3         |  390 x 664 px  |
| Iphone 12      | Safari  | V14.1         |  390 x 664 px  |
| Moto G9 v10.0  | Firefox | Android,v10.0 |  390 x 664 px  |
| OnePlus        | Chrome  | v9.0          |  412 x 757 px  |
| Samsung Galaxy | Firefox | v12.0         |  384 x 702 px  |
| Google Pixel   | Chrome  | v13.0         |  412 x 796 px  |
| Ipad Pro       | Safari  | v16.2         | 1024 x 1292 px |
| Windows PC     | Edge    | Windowns 11   | 1336 x 667 px  |
| Mac PC         | Safari  | Safari 15.6   | 1336 x 667 px  |
| Windows PC     | Chrome  | Chrome        | 1336 x 667 px  |

> **Most Popular browser & Operating System:**

| Browser         | Market Share (%) | Operating System | Market Share (%) |
|-----------------|------------------|------------------|------------------|
| Google Chrome   | 63.81            | Windows          | 70.89            |
| Apple Safari    | 18.85            | macOS            | 18.83            |
| Microsoft Edge  | 3.57             | iOS              | 10.82            |
| Mozilla Firefox | 3.16             | Android          | 0.71             |
| Samsung Internet| 2.71             | Linux            | 1.71             |
| Other           | 7.90             | Other            | 1.04             |

The selections in the table have been determined using statistics from (gs.statcounter.com)[https://gs.statcounter.com/], which reflects the distribution of web browser usage among users. Given that Chrome and Safari hold the largest market shares, they were prioritized for thorough testing across various devices and operating systems. Microsoft Edge, with a substantial user base, was also included for comprehensive assessment. Considering the relatively smaller market shares of Firefox, Samsung Internet, and Opera, they have been grouped together under the "Other" category. 

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

## Defensive programming testing

Defensive programming practices have been integrated into every page of the application, for all areas that store sensitive user information. In cases where unauthorized attempts are made to breach secure pathways housing personal data, a precautionary response is initiated. This results in the presentation of a cautionary page, illustrating the potential risks involved.

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/6b02e7e8-e2fe-47a5-bd1c-af9b18d83e18)

Flows with this protection that only the owner or the admin can have access:
- Order history
- Profile- Add  and update 
- Add testimonial
- Update testimonial
- Delete testimonial
- Add to Favorites posts list
- Like a post on the blog's page
- Add post on the blog- only admin

Other defensive stuff:
- A protective layer has been integrated through the utilization of Stripe's mechanisms for text fields. This strategic measure safeguards against the insertion of malicious scripts, thus enhancing the overall security of the system.
- Magic link for access the order sumary if the user doesn't have an account.
  
## Accessibility Testing

[Serenity Oils Homepage](https://github.com/naragurgel/serenity_oils_aroma/issues/49)

[Products](https://github.com/naragurgel/serenity_oils_aroma/issues/50)

[Products Details](https://github.com/naragurgel/serenity_oils_aroma/issues/57)

[User Profile Page- Authenticated User](https://github.com/naragurgel/serenity_oils_aroma/issues/58)

[Admin - Product Management](https://github.com/naragurgel/serenity_oils_aroma/issues/59)

[Blog page](https://github.com/naragurgel/serenity_oils_aroma/issues/51)

[Post Details](https://github.com/naragurgel/serenity_oils_aroma/issues/52)

[Favorite Post Page](https://github.com/naragurgel/serenity_oils_aroma/issues/56)

[Contact Us Page](https://github.com/naragurgel/serenity_oils_aroma/issues/53)

[Testimonials](https://github.com/naragurgel/serenity_oils_aroma/issues/54)

[Add Testimonial](https://github.com/naragurgel/serenity_oils_aroma/issues/55)

## Validation Testing

The following site were used to aid in validation testing:

- **[CSS Validator](https://jigsaw.w3.org/css-validator/)**

### [BASE.CSS](https://github.com/naragurgel/serenity_oils_aroma/blob/main/static/css/base.css)

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/57eee367-2a62-4065-a80e-650327b4b75c)

### [TESTIMONIALS.CSS](https://github.com/naragurgel/serenity_oils_aroma/blob/main/testimonials/static/testimonials/css/testimonials.css)

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/9c666e5b-6952-4d1a-b1c2-5382de36b1b9)

### [PROFILES.CSS](https://github.com/naragurgel/serenity_oils_aroma/blob/main/profiles/static/profiles/css/profile.css)

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/e3f79749-a23b-4edb-a912-b19526152988)

### [CONTACT_US.CSS](https://github.com/naragurgel/serenity_oils_aroma/blob/main/contact_us/static/contact_us/css/contact_us.css)

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/154b233b-0866-425a-a303-dd28874420ae)

### [CHECKOUT.CSS](https://github.com/naragurgel/serenity_oils_aroma/blob/main/checkout/static/checkout/css/checkout.css)

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/0b72b920-a8c5-4d5a-bd53-ab63a50091b8)

### [BLOG.CSS](https://github.com/naragurgel/serenity_oils_aroma/blob/main/blog/static/blog/css/blog.css)

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/be59d141-2bef-464f-b9f3-7dce147934c1)

The following site were used to aid in validation testing:

- **[HTML Validator](https://validator.w3.org/)**

### HOME PAGE:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/acfa56ca-200a-4060-906b-93dd937f1dac)

### PRODUCTS PAGE:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/5ecf6ae1-9385-4b78-a10b-bb3568257081)

### PRODUCTS DETAILS PAGE:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/8954e6df-d708-4b22-ab08-4ebb224fcc2b)

### BLOG PAGE:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/0f1cf68c-15dd-4715-9a15-c40c67076cd6)

### BLOG DETAILS PAGE:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/cf61d6b7-b0c5-4cf3-8cbd-2c104abbb1ea)

### BLOG POSTS FAVORITES PAGE:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/01797d0f-ac85-46fd-aed4-a6be4b94913c)

### CONTACT US PAGE:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/d5bddb25-21ba-4fdc-939a-65c89f06405c)

### TESTIMONIALS PAGE:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/c68e18d8-2fd9-4865-9ead-c046ff80d6c1)

### TESTIMONIALS DETAILS PAGE:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/ca6a8f67-d783-4e77-83c8-f7bcb02f82c4)

### LOGOUT PAGE:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/1330334e-a447-4186-9e18-6787435a43c9)

### LOGIN PAGE:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/3e3e8b0e-11c6-4170-be62-e3c10b65af63)

### REGISTER PAGE:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/85f8da7e-86e9-4a97-8e31-98cd911119e6)

### MY PROFILE PAGE:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/38f8a089-67ed-4cfa-bc95-b6ed31bde833)

### SHOPPING BAG PAGE:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/f14997b5-c165-45fa-8034-be1ac12759c8)

### CHECKOUT PAGE:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/3a7910a1-2976-42ee-9d60-fbf098aa8f1c)

### CHECKOUT SUCCESS PAGE:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/89111f20-df53-4425-aa8c-60863b44303c)

- **[JS validation](https://jshint.com)**

### [STRIPE_ELEMENT.JS](https://github.com/naragurgel/serenity_oils_aroma/blob/main/checkout/static/checkout/js/stripe_elements.js)

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/aef55e90-40b0-483e-a403-8712195ae708)

### [COUNTRYFIELD.JS](https://github.com/naragurgel/serenity_oils_aroma/blob/main/profiles/static/profiles/js/countryfield.js)

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/dcd1a21d-dbf1-485d-9056-c2a587f3801c)

### [QUANTITY_INPUT_SCRIPT](https://github.com/naragurgel/serenity_oils_aroma/blob/main/products/templates/products/includes/quantity_input_script.html)

The following site were used to aid in validation testing:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/ba41841a-1555-4cc2-9442-39f0c365ef0e)

- **[CI's pep8 tool](https://pep8ci.herokuapp.com/)** 

### BAG

- APPS.PY:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/b1436d8f-7dc1-4a49-a9f3-9e69a3685ae6)

- CONTEXTS.PY:
  
![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/a37b6bc5-9eb8-4fc2-ab7c-246b37da8df9)

- URLS.PY:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/7051ce30-cb13-4f2c-b426-5875ea4b1d6d)

- VIEWS.PY:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/f7cb8e29-e32e-47b7-ad06-a5058c1139af)

### BLOG

- ADMIN.PY:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/fe98dde8-e5bc-45da-a712-c86cd5f61efa)

- APPS.PY:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/9d82e3e5-3ebe-4053-a252-3211ff1951e9)

- FORMS.PY:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/c47612e6-8053-4f06-b218-9c5e46593ed2)

- MODELS.PY:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/c56f953c-ba6a-43cc-837c-21413e28ba2a)

- URLS.PY:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/da7d1339-0f89-4651-aa97-2fc7d67a9dfc)

- VIEWS.PY:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/ebdbddfd-264e-407e-a077-4a5b0981f13e)

### CHECKOUT

- ADMIN.PY:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/1d80fb38-1ca4-4d3b-80cd-724e8392674b)

- APPS.PY:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/726f3171-8b68-45d9-8368-282a3dc2e6c3)

- FORMS.PY:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/eaa61d3d-9b3a-4429-870c-59aa13a5b886)

- MODELS.PY:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/dfc330bb-878f-4de1-9f58-d8adcfcae5d5)

- SIGNALS.PY:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/2e9505fc-05a1-4cd4-bb23-318b522f0781)

- URLS.PY:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/ac784940-b7cd-4311-8d9f-dfd3cfe85ab4)

- VIEWS.PY:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/411a5d9f-692b-4319-a10e-6dd142c033c1)

- WEBHOOK_HANDLER.PY:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/8d717d65-e636-4878-b071-c2931e31eb3c)

- WEBHOOKS.PY:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/0171ce33-7d97-43a4-8847-a5f8ca1c0996)

### CONTACT US

- APPS.PY:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/f253c328-132a-49d0-8a77-075df3651d16)

- ADMIM.PY:
  
  ![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/a3c799fd-abe1-4f52-b2fe-6e7dac12a69d)

- FORMS.PY:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/2bd182d4-a042-48ec-8197-0f971cf511dd)

- MODELS.PY:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/70c7de14-e785-4f8e-94ef-aafd758076cd)

- URLS.PY:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/5e64c24e-6b4b-431d-ab2b-afef31974ae1)

- VIEWS.PY:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/2257da55-a134-4d2a-a4bf-26ab6c826f9c)

### HOME

- APPS.PY:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/62771b80-b54a-4d0b-821b-7558498da77e)

- URLS.PY:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/c7b158b2-f725-49d3-abab-86ed5e08a49f)

- VIEWS.PY:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/ffd9a55b-fd95-4caa-bd90-1cfbda2d39a1)

### PRODUCTS

- ADMIN.PY:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/7d843820-f667-4ab6-b610-3ba80e761e90)

- APPS.PY:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/4c20b632-f21d-48f1-9e0e-91ca5d569532)

- FORMS.PY:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/36f603d4-5e18-4e34-9c4d-b529356f5b84)

- MODELS.PY:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/9c00241f-a803-4ba5-981a-fbde6fd71768)

- URLS.PY:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/daf06aaa-7542-4573-ad08-1bffbc44ebf0)

- VIEWS.PY:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/309fddfb-6e9b-485f-9f42-f8fe0eb59a57)

- WIDGETS.PY:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/bf0c215f-26a6-4036-aaef-ffae84f20be5)

### PROFILE

- APPS.PY:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/1a41bcdb-7e63-4c79-9e78-35fa808ff281)

- FORMS.PY:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/c5a70103-8021-42e8-a2d8-dc8ad98b3870)

- MODELS.PY:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/408895a3-6ee3-4f8a-8c87-6b01d0d18907)

- URLS.PY:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/52844c27-aa70-44be-b85f-9843bb7ff299)

- VIEWS.PY:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/9b8c97ab-faec-4f89-95dd-198a9b340d8f)

### SERENITY OILS

- ASGI.PY:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/091a007f-debd-4bf6-a7f7-f701fdd23f59)

- SETTINGS.PY:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/55d93d67-4995-4207-aa34-ea6dc0fa1abc)

- URLS.PY:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/04322065-853d-4efa-8503-97585c23dd41)

- VIEWS.PY:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/dc5a3417-3cc2-4a1b-86d4-ede639a233a9)

- WSGI.PY:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/0f7ffd7b-43d1-430e-99d9-4bd103f30234)

### TESTIMONIALS

- ADMIN.PY:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/5328ebfa-6d84-4773-9d12-555d64c3bec9)

- APPS.PY:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/27f209dc-6ece-4793-b0c9-18393afbf641)

- FORMS.PY:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/deaaba2e-acb6-4d4e-b45a-d2d31729ce9f)

- MODELS.PY:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/007c3f18-9d58-47ae-a911-a165df4872f9)

- URLS.PY:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/f1784254-9ef2-4c43-9ca1-12ea8ddc4bbf)

- VIEWS.PY:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/c415ba06-f148-4f52-aa61-ed35fc9685e3)

### CUSTOM_STORAGES.PY:

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/1bde6ca9-69d2-493a-88f6-7ba2911081f5)

### MANAGE.PY

![image](https://github.com/naragurgel/serenity_oils_aroma/assets/112726044/aa718102-a4b0-4f83-9f41-a2e6c79863a9)

## Defects

I've made [miletones](https://github.com/naragurgel/serenity_oils_aroma/issues?q=is%3Aissue+is%3Aclosed) to group all the defects and make them easier to been found.

### Outstanding Defects

There are no known functional or visual outstanding defects at this time.

[Back to the TOP](https://github.com/naragurgel/serenity_oils_aroma/edit/main/TESTING.md#testing)

[Back to README.md](https://github.com/naragurgel/serenity_oils_aroma/tree/main#readme)https://github.com/naragurgel/serenity_oils_aroma/tree/main#readme)
