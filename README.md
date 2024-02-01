# Django Restaurant Menu

Welcome to the Django Restaurant Menu project! This web application is designed to display a menu with various items, their details, and additional information. The project uses Django, a high-level web framework for Python.

## Getting Started

### Prerequisites
- Python 3.x
- Django

### Installation
1. Clone the repository: `git clone https://github.com/your-username/django-restaurant-menu.git`
2. Navigate to the project directory: `cd django-restaurant-menu`
3. Install dependencies: `pip install -r requirements.txt`
4. Apply migrations: `python manage.py migrate`
5. Run the development server: `python manage.py runserver`

### Usage
- Access the menu: [http://localhost:8000/](http://localhost:8000/)
- View item details: [http://localhost:8000/menu/item/{item_id}](http://localhost:8000/menu/item/{item_id})
- About page: [http://localhost:8000/about/](http://localhost:8000/about/)

## Features
- Display a list of menu items.
- View details of each menu item.
- About page providing additional information.

## Project Structure
- `django-restaurant-menu/`
  - `menu/`: Django app for handling menu-related functionality.
    - `models.py`: Defines the database models (e.g., `Item`).
    - `views.py`: Contains class-based views and function-based views.
    - `templates/`: HTML templates for rendering views.
  - `about.html`: About page template.
  - `index.html`: Main menu page template.
  - `menu_item_detail.html`: Template for displaying detailed information about a menu item.

## Contributing
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`
3. Make your changes and commit them: `git commit -m 'Add feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
