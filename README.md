# Pizza Restaurant

This project is a Pizza Restaurant System that is built with Flask and SQLAlchemy. The app allows users to manage restaurants and the pizza menus, as it has several functionalities like adding, updating, and deleting restaurants and pizzas.

## Features

- Add, update, and delete restaurants
- Add, update, and delete pizzas
- Assign pizzas to restaurants and vice versa
- View list of restaurants and their pizzas
- Validation for restaurant and pizza data

## Setup

1. Clone the repository: 
```
git clone git@github.com:wachuka7/phase4-code_challenge1.git
```
2. Install dependencies
```pip install -r requirements.txt```

3. Set up the database:
```flask db upgrade```

4. Run the application:
```flask run```

5. Access the application:

To access the app, open your web browser and go to `http://localhost:5000`

## API Endpoints

- GET /restaurants: Get a list of all restaurants
- GET /restaurants/:id: Get details of a specific restaurant by ID
- POST /restaurants: Add a new restaurant
- PUT /restaurants/:id: Update details of a restaurant by ID
- DELETE /restaurants/:id: Delete a restaurant by ID
- GET /pizzas: Get a list of all pizzas
- GET /pizzas/:id: Get details of a specific pizza by ID
- POST /pizzas: Add a new pizza
- PUT /pizzas/:id: Update details of a pizza by ID
- DELETE /pizzas/:id: Delete a pizza by ID

## Authors

- Rachael Wachuka Chege
- email: `rachaelwachuka7@gmail.com`
- github: `https://github.com/wachuka7`


## License

This project is licensed under the MIT License - see the `MIT License` file for details.






