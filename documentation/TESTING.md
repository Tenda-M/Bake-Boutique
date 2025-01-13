# Testing for Bake Boutique

## Testing Contents

1. [Validation](#validation)
2. [Browser Testing](#browser-testing)
3. [Manual Testing](#manual-testing)
4. [Testing User Stories](#testing-user-stories)
5. [Bugs](#bugs)
6. [Known Bugs](#known-bugs)

---

## Validation

The code was validated using [Code Institute's](https://pep8ci.herokuapp.com/#) linter during development. No errors were found in the final testing, as shown below:
![Pep8 Linter Validation](/documentation/readme/pep8validation.png)

## Browser Testing

Bake Boutique was thoroughly tested on the live Heroku deployment across multiple browsers, including:

- **Google Chrome**
- **Mozilla Firefox**
- **Safari**

The application performed seamlessly on all browsers without any issues.

---

## Manual Testing

### Testing Features

| **Feature**                   | **Tested?** | **Result**                                                                 |
|-------------------------------|-------------|-----------------------------------------------------------------------------|
| Homepage                      | Yes         | Homepage loads successfully with featured products and links to categories.|
| Navbar                        | Yes         | Navbar is responsive, with dropdowns and active states working correctly.  |
| About Us Page                 | Yes         | Displays a welcoming message and loads content without issues.             |
| Testimonials Page             | Yes         | Displays approved testimonials and loads the form for user submissions.    |
| Contact Us Page               | Yes         | Loads successfully with a functional contact form.                         |
| Wishlist Page                 | Yes         | Registered users can add, view, and remove items.                          |
| Login Page                    | Yes         | Users can log in successfully with email and password validation.          |
| Logout Functionality          | Yes         | Users are successfully logged out and redirected to the homepage.          |
| Registration Page             | Yes         | New users can register with form validation for all required fields.       |
| Profile Page                  | Yes         | Displays user details and purchase history accurately.                     |
| Add Product (Admin)           | Yes         | Admins can successfully add new products to the store.                     |
| Edit Product (Admin)          | Yes         | Admins can edit product details and save updates.                          |
| Delete Product (Admin)        | Yes         | Admins can delete products, with a confirmation prompt.                    |

---

## Testing User Stories

| **User Story**                                                                                  | **Feature**                              | **Tested?** | **Result**                                                             |
|-------------------------------------------------------------------------------------------------|------------------------------------------|-------------|-------------------------------------------------------------------------|
| As a public user, I want to browse the available baked goods without needing to sign up.        | Browse Products                          | Yes         | Public users can view all products without creating an account.         |
| As a public user, I want to view product details, such as pricing and description.              | Product Details                          | Yes         | Users can view detailed product pages with images, descriptions, and prices. |
| As a site user, I want to easily register for an account so that I can have a personalised experience. | User Registration                         | Yes         | Users can register successfully with a confirmation message.            |
| As a site user, I want to log in and out effortlessly so that I can manage my account access.   | Login and Logout                         | Yes         | Users can log in and log out successfully.                              |
| As a site user, I want to receive an email confirmation after registering.                      | Email Confirmation                       | Yes         | Users receive a confirmation email with registration details.           |
| As a shopper, I want to sort products by categories so that I can easily identify the best-rated or priced options. | Product Sorting                          | Yes         | Users can sort products by categories like “Cakes” or “Cookies.”        |
| As a shopper, I want to search for a specific product by name or description.                   | Search Functionality                     | Yes         | Search bar displays matching products with their images and titles.     |
| As a shopper, I want to select the size and quantity of a product.                              | Customise Orders                         | Yes         | Users can choose size and quantity before adding to the cart.           |
| As a shopper, I want to adjust the quantity of items in my bag.                                 | Cart Management                          | Yes         | Users can increase or decrease item quantities in their cart.           |
| As a shopper, I want to easily enter my payment information.                                    | Secure Payment Form                      | Yes         | Users can enter and validate payment information securely.              |
| As a shopper, I want to receive an email confirmation after checkout.                           | Order Confirmation Email                 | Yes         | Users receive order confirmation emails with details and delivery info. |
| As a registered user, I want to add products to my wishlist.                                    | Wishlist Feature                         | Yes         | Registered users can save products to their wishlist for future purchases. |
| As a registered user, I want to view and manage my wishlist.                                    | Wishlist Management                      | Yes         | Users can view and remove wishlist items easily.                        |
| As a public user, I want to be encouraged to sign up by not having access to the wishlist feature. | Wishlist Restriction                     | Yes         | Wishlist is restricted to logged-in users only.                         |
| As a registered user, I want to leave reviews on products.                                      | Product Reviews                          | Yes         | Users can submit reviews with ratings and comments.                     |
| As a visitor, I want to view product reviews.                                                   | Review Section                           | Yes         | Visitors can view reviews and ratings on product pages.                 |
| As a site owner, I want to moderate reviews.                                                    | Review Moderation                        | Yes         | Admins can approve or reject reviews before publishing.                 |
| As a user, I want to submit testimonials after contacting Bake Boutique.                        | Testimonial Submission                   | Yes         | Users can submit testimonials, pending admin approval.                  |
| As a visitor, I want to read testimonials.                                                     | Testimonial Page                         | Yes         | Visitors can read approved testimonials sorted by date.                 |
| As a store owner, I want to add products to my inventory.                                       | Product Addition (Admin)                 | Yes         | Admins can add products with images, descriptions, and prices.          |
| As a store owner, I want to edit or update product details.                                     | Product Editing (Admin)                  | Yes         | Admins can update product details via the admin dashboard.              |
| As a store owner, I want to delete products that are no longer available.                       | Product Deletion (Admin)                 | Yes         | Admins can delete products with a confirmation prompt.                  |

---

## Bugs

### Fixed Bugs in Bake Boutique

1. **Bug: Product Detail Page 404 Error**
   - **Issue**: Attempting to access a deleted product displayed a 404 error.
   - **Fix**: Updated the product detail view to handle missing products gracefully by redirecting to the homepage with a flash message.

2. **Bug: Wishlist Feature Not Accessible to Public Users**
   - **Issue**: Wishlist was visible to unauthenticated users, leading to confusion.
   - **Fix**: Restricted wishlist access to logged-in users only.

3. **Bug: Testimonial Form Not Displaying Errors**
   - **Issue**: Validation errors on the testimonial form were not displayed to the user.
   - **Fix**: Updated the template to include error messages for each field.

4. **Bug: Navbar Dropdown Overlapping Content**
   - **Issue**: Dropdown menu overlapped page content on smaller screens.
   - **Fix**: Applied responsive CSS rules to adjust the dropdown positioning.

---

## Known Bugs

After extensive testing, no unresolved bugs were identified in the Bake Boutique application.

---

## Responsiveness

The site was tested on various devices, including desktops, tablets, and mobile phones. The responsive design performed flawlessly across all screen sizes, ensuring a consistent user experience.
