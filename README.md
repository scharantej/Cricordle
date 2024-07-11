## Flask Application Design: Cricket Wordle

### HTML Files

- `index.html`: Main page of the application. It presents the game board, where users can guess a cricket player's name. It also displays the results of previous guesses.

- `about.html`: Provides information about the application, including its purpose, usage, and any relevant documentation.

### Routes

- `/`: The root route that renders `index.html`.

- `/guess`: Handles user guesses. It validates the guess and displays the results on the `index.html` page.

- `/hint`: Provides a hint to the user if they are struggling with the current wordle. The hint can be a related keyword or a fact about the cricketer.

- `/reset`: Resets the game, allowing the user to start a new wordle.

- `/about`: Renders `about.html`, providing information about the application.

### Additional Considerations

- The application can store the cricketers' names in a database or a JSON file for easy management.

- The application can track user statistics, such as the number of games played, wins, and hints used. This data can be used to provide insights into user behavior and improve the application's design.

- To make the game more challenging, the application can limit the number of guesses allowed per wordle.