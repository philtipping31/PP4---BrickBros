# Documented Manual Testing for | BrickBros

This project was tested throughout the duration of the project creation. This was done with ensuring the user story / feature was designed and working as intended when being coded.
The project was also tested frequently via Google Chrome Dev Tools for display issues. 


## Validation Testing

### HTML Checks

All Html files were tested using [W3C Schools validator](https://validator.w3.org/) in logged in and logged out state.

All issues were resolved and files now pass checks.

![HTML Checks](readmedocs/screenshots/html-checker.png)



### CSS Checks

CCS Files were tested using [W3C Schools CCS Validator](https://jigsaw.w3.org/css-validator/)

File passed checks first time.

![CSS Checks](readmedocs/screenshots/css-checks.png)



### Python Checks

Python files were checked using the [CI PEP8 Linter](https://pep8ci.herokuapp.com/)

Issues were resolved and files now pass checks.

![PEP8 Tests](readmedocs/screenshots/pep8-validation.png)

#### Outstanding.
I had a few lines too long in the settings.py as shown below:


![PEP8 Setting.py](readmedocs/screenshots/pep8-settingpy.png)

## User Stories

 Outer pipes  Cell padding 
No sorting
| User Story                                                                   | Test                                                                                                                            | Action                                                                                                                                                                              | Expected                                                                                                                          | Result (Pass/Fail) |
| ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| [User Story #2](https://github.com/philtipping31/PP4---BrickBros/issues/2)   | The site works as intended throughout in a deployed environment                                                                 | Perform all tests as documented below on the deployed site via Heroku                                                                                                               | All features, views, options work as intended                                                                                     | Pass               |
| [User Story #3](https://github.com/philtipping31/PP4---BrickBros/issues/3)   | Check nav bar and footer are on all pages from base.html                                                                        | View each page in deployed environement and clearly see the navbar and footer                                                                                                       | Features appear on all pages as stem from the base.html file                                                                      | Pass               |
| [User Story #6](https://github.com/philtipping31/PP4---BrickBros/issues/6)   | When logged in and logged out, click 'view more' on a build post to see more content about a specific post                      | Click 'Read More' on a build post when logged in and logged out of a profile                                                                                                        | An individual build post opens up and displays as intended                                                                        | Pass               |
| [User Story #11](https://github.com/philtipping31/PP4---BrickBros/issues/11) | Register button clearly shown in nav bar for users not logged in to an account                                                  | View all pages and check for Register link if not logged in                                                                                                                         | Register field appears in on all pages when user not logged in                                                                    | Pass               |
| [User Story #11](https://github.com/philtipping31/PP4---BrickBros/issues/11) | When register is clicked on, the register page is loaded correctly                                                              | View site on all pages and navigate to the Register (SignUp) page                                                                                                                   | Sign up page correctly loads and is visbile on all screensizes                                                                    | Pass               |
| [User Story #11](https://github.com/philtipping31/PP4---BrickBros/issues/11) | Fields work as intended, username is required, email address is not required, password needs to match criteria                  | Attempt to sign up without required fields - check prompt to complete shows. Try password variation that does not meet criteria and check prompt                                    | Prompts show as intended if criteria does not match. If all fields match then signup successful and logs user in to their account | Pass               |
| [User Story #12](https://github.com/philtipping31/PP4---BrickBros/issues/12) | User can not add a build when not logged in                                                                                     | Navigate to 'Add Build' when not logged in                                                                                                                                          | Check sign in page loads asking user to sign in to fully engage with the site                                                     | Pass               |
| [User Story #12](https://github.com/philtipping31/PP4---BrickBros/issues/12) | Once logged in 'Add Build' page is now accessible.                                                                              | Navigate to 'Add Build' when logged in to view the front end form to add a post.                                                                                                    | As the user is logged in the page displays as it should with all fields ready for the user to enter                               | Pass               |
| [User Story #12](https://github.com/philtipping31/PP4---BrickBros/issues/12) | Adding a post successfully                                                                                                      | Attempt to fill in the post form, missing items prompts user to fill in if required. If not image added, default placeholder is added, when post is added, user is notified of this | All features work as intended                                                                                                     | Pass               |
| [User Story #14](https://github.com/philtipping31/PP4---BrickBros/issues/14) | Appending /admin to the URL opens up Django Admin panel                                                                         | Add /admin to the URL to ensure admin access is available for the super user                                                                                                        | Admin page is accessed correctly for the super user. If non super user logged in and appends /admin, access denied                | Pass               |
| [User Story #16](https://github.com/philtipping31/PP4---BrickBros/issues/16) | If a user is logged in, they can view their own post and see the edit button                                                    | Log in as a user and view a post that the user has created to see the edit button                                                                                                   | Edit button displays for an owner of a post                                                                                       | Pass               |
| [User Story #16](https://github.com/philtipping31/PP4---BrickBros/issues/16) | If a user isn't logged in or doesn't own a post, edit will not be an option                                                     | View a post by a different user to the logged in user                                                                                                                               | Edit button is not visible                                                                                                        | Pass               |
| [User Story #16](https://github.com/philtipping31/PP4---BrickBros/issues/16) | If a user edits a post, they can see all previous fields to amend                                                               | Click edit and view the post form again with all fields in place                                                                                                                    | As expected, all items are populated and able to be edited                                                                        | Pass               |
| [User Story #16](https://github.com/philtipping31/PP4---BrickBros/issues/16) | If a user edits a post and submits the edit, they are notified of the confirmation of edit                                      | Edit a post and submit the edit - pop up confirms post edited                                                                                                                       | Edit is successful and pop up shown confirming edit                                                                               | Pass               |
| [User Story #17](https://github.com/philtipping31/PP4---BrickBros/issues/17) | If a user is logged in, they can view their own post and see the delete button                                                  | Log in as a user and view a post that the user has created to see the delete button                                                                                                 | Delete button displays for an owner of a post                                                                                     | Pass               |
| [User Story #17](https://github.com/philtipping31/PP4---BrickBros/issues/17) | If a user isn't logged in or doesn't own a post, delete will not be an option                                                   | View a post by a different user to the logged in user                                                                                                                               | Delete button is not visible                                                                                                      | Pass               |
| [User Story #17](https://github.com/philtipping31/PP4---BrickBros/issues/17) | If a user delete a post, they will be prompted to confirm the deletion of a post                                                | Click on the delete post option                                                                                                                                                     | Clicking delete, opens up the confirm delete page and allows the user to confirm deletion                                         | Pass               |
| [User Story #17](https://github.com/philtipping31/PP4---BrickBros/issues/17) | If a user deletes a post and submits the deletion, they are notified of the confirmation of edit                                | Confirm the deletion of a post                                                                                                                                                      | User is directed back to all builds, pop up shows that post was successfully deleted                                              | Pass               |
| [User Story #18](https://github.com/philtipping31/PP4---BrickBros/issues/18) | Once user has registered for account they can login                                                                             | Create a user and login                                                                                                                                                             | Login successful                                                                                                                  | Pass               |
| [User Story #19](https://github.com/philtipping31/PP4---BrickBros/issues/19) | Search bar shows on the 'All Builds' page                                                                                       | Go to all builds and search bar is available                                                                                                                                        | Search bar displays on all builds page                                                                                            | Pass               |
| [User Story #19](https://github.com/philtipping31/PP4---BrickBros/issues/19) | Search bar placeholder text shows just model numbers accepted                                                                   | Search bar clearly tells user to search for model numbers                                                                                                                           | Model number search feature works                                                                                                 | Pass               |
| [User Story #19](https://github.com/philtipping31/PP4---BrickBros/issues/19) | When a search is made, results show if match found                                                                              | Type in a model number that exists in the database                                                                                                                                  | Search clearly displays the correct results                                                                                       | Pass               |
| [User Story #19](https://github.com/philtipping31/PP4---BrickBros/issues/19) | When a search is made and no matches found, user is notified of this                                                            | Enter a model number that does not exist                                                                                                                                            | Page shows no matches found and prompts user to add the first post                                                                | Pass               |
| [User Story #20](https://github.com/philtipping31/PP4---BrickBros/issues/20) | If a user is logged in they can see the option to logout in the navbar                                                          | Once logged in, checked that the logout button/link is available                                                                                                                    | Once logged in, the logout button/link is available                                                                               | Pass               |
| [User Story #20](https://github.com/philtipping31/PP4---BrickBros/issues/20) | If user clicks logout, they will be asked if they meant to do this. Also option to go to the home page for UX will be an option | Click logout and check that the user is asked to confirm the action                                                                                                                 | Logout button takes you to the correct page asking to confirm whether or not you want to login or go back to the home page        | Pass               |
| [User Story #20](https://github.com/philtipping31/PP4---BrickBros/issues/20) | If user confirms logout, user will be logged out and notified                                                                   | Click confirm log out                                                                                                                                                               | User is notified that they have been logged out.                                                                                  | Pass               |


## Manual Testing

### Responsiveness

Site was tested using Chrome Dev Tools with the responsiveness section. Ensuring the webpage can be clearly used on all screensizes/devices.

### 403 and 404 pages

A 403 page were created and tested so that if a user tries to access a URL to delete a post when they do not own it, the 403 page is displayed notifying the user that they are not authorized to perform the action. 

![403 page](readmedocs/screenshots/403-page.png)




A 404 page was created so that if a user enters an incorrect URL they will be given a 404 page notifying them of this and allow the user to navigate to the home page easily.

![404 page](readmedocs/screenshots/404-page.png)



### Lighthouse Tests

Lighthouse tests were run in an incognito window. 

![Lighthouse Test home](readmedocs/screenshots/homepage-lighthouse.png)

![Lighthouse Test Add Build](readmedocs/screenshots/addbuild-lighthouse.png)



Issues found with best practices on all builds page due to Cloudinary Images 

![Lighthouse Test all builds](readmedocs/screenshots/all-builds-lighthouse.png)


### Navbar 

| Test                                                                                                      | Action                                                                                                                                         | Expected                                                                                                                                                                       | Result (Pass/Fail) |
| --------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------ |
| Nav Bar shows Home / Builds drop down > All Builds / Add Build and Register / Login for a first time user | Visit the site as a logged out user and check correct nav items are showing and navigate to the correct page                                   | Nav items correctly display and open the correct page                                                                                                                          | Pass               |
| Nav Bar Shows Same options, but Login changes to Logout when user is logged in                            | Login to the website and check the nav bar has removed login and register and now shows all items as normal but the logout link is an option   | Nav items correctly display and open the correct page                                                                                                                          | Pass               |
| Nav Bar items direct the user to the correct location                                                     | Test all navbar links by clicking on them and checking the correct page loads                                                                  | All nav items are directing the user to the correct location                                                                                                                   | Pass               |
| Nav bar works in tablet/mobile view                                                                       | Use chrome dev tools on responsive mode and also open webpage on a mobile device to check full functionality of the the nav bar view and links | All nav items are hidden in a closed button, clicking on this opens the nav menu and all items are shown based on the current state and open up the correct page when selected | Pass               |


### Footer 

| Test                                                       | Action                                                                                       | Expected                                                          | Result (Pass/Fail) |
| ---------------------------------------------------------- | -------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | ------------------ |
| All footer links open in a new tab to the correct location | Click on each footer social and check that the correct social page is opened up in a new tab | All links direct to the correct location and in a new browser tab | Pass               |


### Pagination

| Test                                                                                          | Action                                                    | Expected                                                                                                             | Result (Pass/Fail) |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ------------------ |
| Pagination works correctly as per code of 3 per page                                          | Each builds page clearly shows 3 builds posts             | 3 Builds posts show on each page                                                                                     | Pass               |
| If more than 3, next button shows                                                             | Add more than three builds to see the next button appear. | The next button shows and clearly moves the user to see the next set of builds over 3                                | Pass               |
| if more than 9 the middle set of three allows the user to see previous button and next button | Add more builds so posts extend over multiple pages.      | Next and Prev button clearly show and operate as intended, taking the user from page to page to see all builds posts | Pass               |






