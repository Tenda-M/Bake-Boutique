# Bake Boutique

![mock-up images](docs/readme/responsive.PNG "Website preview at different resolutions")

[View The Live Project Here](https://bake-boutique.herokuapp.com/) <!-- Add link to live site here -->

## Purpose of the Project

Bake Boutique is an e-commerce platform designed to provide users with a seamless experience for browsing, customizing, and purchasing baked goods for all occasions. It offers a wide selection of cakes, cupcakes and cookies while allowing users to customize their orders to suit their preferences.

## Table Of Contents
1. [Introduction](#Introduction)
    1. [Scenario](#Scenario)
2. [UX](#UX)
    1. [User Stories](#User-Stories)
    2. [Design Thinking](#Design-Thinking)
    3. [Colour Scheme](#Colour-Scheme)
3. [Features](#Features)
    1. [Design Features](#Design-Features)
    2. [Existing Features](#Existing-Features)
       1. [Public User Features](Public-User-Features)
       2. [Private User Features](Private-User-Features)
       3. [Admin/Staff Features](Admin/Staff-Features)
    3. [Future Adaptations](#Future-Adaptations)
4. [Technologies Used](#Technologies-Used)
    1. [Main Languages Used](#Main-Languages-Used)
    2. [Frameworks, Libraries & Programs Used](#Frameworks,-Libraries-&-Programs-Used)
5. [Database Design](#Database_Design)
6. [Testing](#Testing)
7. [Issues and Bugs](#Issues-and-Bugs)
8. [Deployment](#Deployment)
9. [Credits](#Credits)
10. [Acknowledgements](#Acknowledgements)

---

## UX

### User Stories

Bake Boutique was designed with three types of users in mind: 

- **Public Users**:
  - Browse baked goods and view product details without signing in.
  - Access the "About Us" and "Contact Us" pages for more information.

- **Private Users**:
  - Create accounts and sign in to access custom features like the wishlist.
  - Place orders and view order history.

- **Admin/Staff Users**:
  - Manage product inventory and customer orders efficiently.

### Design Thinking

- **User-Friendly Interface**: Bake Boutique is designed to ensure smooth navigation and intuitive usability.
- **Mobile-First Design**: The platform is fully responsive, offering an optimized experience across devices.
- **Warm and Welcoming**: The platform's color scheme and visual elements create an inviting experience for users.

### Colour Scheme

A warm palette inspired by baked goods was selected. Soft tones combined with bold accents create a visually appealing aesthetic that resonates with the theme of a bakery.

---

## Features

### Design Features

- A responsive homepage showcasing featured products and offers.
- Dropdown navigation for easy browsing by category.

### Existing Features

- **Homepage**: Displays featured products and categories.
- **About Us Page**: Introduces the platform's story and mission.
- **Contact Us Page**: Enables users to reach out via a simple form.
- **Product Pages**: Showcases detailed descriptions, pricing, and customization options.
- **Wishlist**: Allows logged-in users to save products for future purchases.
- **Order Management**: Users can view their order history and track statuses.

### Future Adaptations

- **Recipe Sharing Feature**: Add a community section for users to share their baking recipes.
- **Social Media Integration**: Enable sharing of products and reviews on platforms like Instagram and Facebook.

---


## Technologies Used
- [HTML](https://en.wikipedia.org/wiki/HTML) is used to structure the main content of the site.
- [CSS](https://en.wikipedia.org/wiki/CSS) is used for designing the layout and appearance of the website.
- [CSS Flexbox](https://www.w3schools.com/css/css3_flexbox.asp) is implemented for a responsive layout that adapts to different screen sizes.
- [CSS Grid](https://www.w3schools.com/css/css_grid.asp) is also used for creating flexible, responsive layouts.
- [JavaScript](https://www.javascript.com) is used to enhance user interaction and dynamic elements on the site.
- [Python](https://www.python.org) is used as the back-end programming language, handling server-side functionality.
- [Git](https://git-scm.com) is used for version control, allowing me to track and manage changes (`git add`, `git commit`, `git push`).
- [GitHub](https://github.com) is used for secure online storage of the project code and for collaboration.
- [Gitpod](https://gitpod.io) is the cloud-based integrated development environment (IDE) used for writing and testing code.
- [Bootstrap](https://getbootstrap.com) is used to create a responsive front-end design with pre-built components and styling.
- [Django](https://www.djangoproject.com) is the Python framework used to develop the back-end of the site and manage its functionalities.
- [PostgreSQL](https://www.postgresql.org) is used as the relational database to store data such as user information and recipes.
- [ElephantSQL](https://www.elephantsql.com) is used to host the PostgreSQL database for production.
- [Heroku](https://www.heroku.com) is the hosting platform used to deploy and run the live site.
- [Cloudinary](https://cloudinary.com) is used for managing and hosting static files and images for the site.

### Main Languages Used
- HTML, CSS, JavaScript for frontend development.
- Python (Django) for backend logic.
- SQL (PostgreSQL/MySQL) for database management.

### Frameworks, Libraries & Programs Used
- Django for backend web development.
- Bootstrap for responsive design and layout.
- Cloudinary for image storage.

## Database Design
- While planning this project, I drew up an Entity Relationship Diagram to help me visualise the database models and their relationships.
![screenshot](documentation/design_images/database.png)

## Testing
Manual testing was conducted for all key features, including recipe submission,  edit shared recipes, and commenting functionality. Testing ensures that all components work smoothly on various devices and browsers.
For all testing, please refer to the [TESTING.md](documentation]TESTING.md) file.
## Issues and Bugs
- Resolved issues with recipe form submission.
- Adjusted layout for consistent display of recipe cards.
- Ongoing improvements for mobile responsiveness.

## Deployment
- The application was deployed using Heroku, and the database was configured with PostgreSQL.
- Cloudinary was integrated to manage image uploads for recipes.

The following steps for creating and configuring a new Python workspace and API credentials have been informed by and adapted from the Python walkthrough project 'Recipe Haven' by [Code Institute's](https://codeinstitute.net/ie/). Please ensure each step is applicable to your project requirements and adjust the provided data accordingly.

### Creating a new repository 
<details open>
<summary>Steps to create a new repository.</summary>  
The [Code Institute's Python Essential Template](https://github.com/Code-Institute-Org/python-essentials-template) was used to create a terminal for my Python file to generate it's output. 

To utilise this template, adhere to these steps:
1. Sign in to [GitHub](https://github.com/) or register for a new account.
2. Go to the Python template repository provided above.
3. Select '**Use this template**' -> '**Create a new repository**'.
4. Pick a new repository name and choose '**Create repository from template**'.
5. Within your new repository area, click the green '**Gitpod**' button to create a new workspace.

</details> 

#### Deploying to Heroku 
The Recipe Haven project was deployed using [Heroku](https://www.heroku.com) and connected to an external PostgreSQL database hosted on [ElephantSQL](https://www.elephantsql.com). Below is a step-by-step guide to the deployment process:

##### Steps for Deployment:

1. **Set Up the Project Locally**:
   - Ensure that your project is properly set up and working locally before deploying. Install all necessary dependencies listed in `requirements.txt` using the following command:
     ```bash
     pip install -r requirements.txt
     ```

2. **Set Up Heroku**:
   - Log in to your [Heroku](https://dashboard.heroku.com) account.
   - Create a new Heroku app by clicking **New** > **Create New App**.
   - Choose a unique app name and select the region closest to your location.

3. **Set Up PostgreSQL**:
   - In Heroku, go to the **Resources** tab of your app.
   - Under **Add-ons**, search for and add **Heroku Postgres** as your database.
   - Alternatively, use [ElephantSQL](https://www.elephantsql.com) for your PostgreSQL database by creating an instance on ElephantSQL and copying the database URL.
   - In your Heroku app, navigate to **Settings** > **Reveal Config Vars** and set the following environment variables:
     - `DATABASE_URL`: Your PostgreSQL database URL (from either Heroku Postgres or ElephantSQL).
     - `SECRET_KEY`: A secret key for your Django project.
     - `DEBUG`: Set to `False` for production.

4. **Set Up Cloudinary for Static and Media Files**:
   - Sign up for a [Cloudinary](https://cloudinary.com) account to store static files and images.
   - In Heroku’s **Config Vars**, add the following variable:
     - `CLOUDINARY_URL`: Your Cloudinary API environment variable.
   - Update your Django settings to handle static and media files via Cloudinary.

5. **Prepare Your Application for Deployment**:
   - Make sure you have a `Procfile` in the root of your project, specifying how Heroku should run your app:
     ```
     web: gunicorn your_project_name.wsgi
     ```
   - Make migrations for your database:
     ```bash
     python manage.py makemigrations
     python manage.py migrate
     ```
   - Collect static files to be served by Cloudinary:
     ```bash
     python manage.py collectstatic
     ```

6. **Deploy to Heroku**:
   - Connect your Heroku app to your GitHub repository under the **Deploy** tab in Heroku.
   - Enable automatic deploys from the `main` branch, or manually deploy by clicking the **Deploy Branch** button.

7. **Run the App**:
   - Once deployed, your app should be live at `https://your-app-name.herokuapp.com`.
   - Use the **Heroku logs** command to troubleshoot any issues:
     ```bash
     heroku logs --tail
     ```

-----  

### Forking the GitHub Repository

A copy of the original repository can be made through GitHub. Please follow the below steps to fork this repository:  

1. Visit GitHub and sign in.
2. After logging in, access this repository using the following link: [Recipe Haven Repository](https://github.com/Tenda-M/recipe-haven).
3. Above the file section of the repository and located at the top right of the page, you'll find the '**Fork**' button. Click on it to create a fork of this repository.
4. You should now find a forked version of this repository in your GitHub account.

-----  

### Clone this GitHub Repository

A local clone of this repository can be made on GitHub. Please follow the below steps:
1. Go to GitHub and sign in.
2. You can find the [Recipe Haven Repository](https://github.com/Tenda-M/recipe-haven) at this address.
3. Above the section containing repository files, locate the '**Code**' button.
4. Click on it and select your preferred cloning method from HTTPS, SSH, or GitHub CLI. Copy the URL to your clipboard using the '**Copy**' button.
5. Launch your Git Bash Terminal.
6. Navigate to the directory where you want the cloned directory to be created.
7. Enter `git clone` followed by pasting the copied URL from step 4.
8. Hit '**Enter**' to initiate the creation of the local clone.

## Credits
### Content
- Recipe content was provided by the community and contributors.

- The Code Institute's 'Codestar' project provides guidance for setting up Google Sheets API and Credentials: [Code Institute](https://codeinstitute.net/ie/)

- W3Schools provided helpful Python tutorials. [W3Schools](https://www.w3schools.com/python/default.asp)

- The Python Typing Text Effect us was from. [computing.net](https://www.101computing.net/python-typing-text-effect/)

- Use of alert colour [coolors.co](https://coolors.co/000000-333333-a1a1a1-f5f5f5-ffffff-507e50-507948-304f2a-263e21)

- Use of all images [Vecteezy](https://www.vecteezy.com)

- All recipes were taken from the BBC Goodfood website and can be found here [BBC Good Food](https://www.bbc.co.uk/food).

- HTML, CSS, javascript[mdn](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/email)

- Use of django urls [django](https://docs.djangoproject.com/en/5.1/ref/urls/)

- Use of profile creation [youtube](https://www.youtube.com/watch?v=FdVuKt_iuSI&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=9)

- Use of Bootstrap FAQ Page [bootstrapbrain.com](https://bootstrapbrain.com/component/bootstrap-faq-page-using-accordion/)
  
### People
- Project development and design by [Tatenda Mudehwe].

## Acknowledgements
- I extend my heartfelt gratitude to my family for their unwavering support during discussions on ideas and debugging, as well as for diligently testing my work.
- Special thanks to my mentor, Excellence Ilesanmi, for providing invaluable support and guidance throughout this journey.
- I am deeply thankful to my fellow peers at Code Institute for their invaluable support and camaraderie.