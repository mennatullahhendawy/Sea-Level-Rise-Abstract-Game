# initiating Game fixed variables
game_state = 0  # 0 = Title Screen, 1 = Playing, 2 = Game Over (3 states)
sea_level_height = 100
people_remaining = 5  # Number of people to save
people = []  # List to store people positions
sea_rising_speed = 0.01
people_saved_count = 0  # When I save a person, this number increases
peopleSpeed = 0  # Speed at which people move upward

# Setup function: Initializes the game window and creates people
def setup():
    global people
    size(800, 600)
    for i in range(people_remaining):
        people.append([random(0, width), random(400, height)])  # People start randomly, within screen height

# Draw function: Main game loop
def draw():
    global game_state, sea_level_height, people_saved_count, peopleSpeed, sea_rising_speed
    
    background(135, 206, 250)  # Sky blue background

    # First game state (title)
    if game_state == 0:
        textAlign(CENTER)
        textSize(32)
        fill(0)
        text("Press SPACE to Start", width / 2, height / 2)
        if keyPressed and key == ' ':
            game_state = 1  # Start the game

    # Second state of the game (gameplay)
    elif game_state == 1:
        sea_level_height += sea_rising_speed  # Sea level rises over time
        sea_rising_speed += 0.01 #increasing the speek of sea level rise
        
        # Draw sea level (the darker blue)
        fill(0, 0, 255, 128)  # Semi-transparent blue for the sea
        rect(0, height - sea_level_height, width, sea_level_height)
        
        # Draw and move people
        for person in people:
            if keyPressed and key == ' ':  # Move people up when 'SPACE' is pressed
                person[1] -= peopleSpeed  # Move people upwards
                peopleSpeed += 0.05  # Increase speed gradually
                
            fill(255, 0, 0)  # Coloring people
            circle(person[0], person[1], 20)  # Draw people as red circles
            
            # Check if the person is under the sea level
            if person[1] >= height - sea_level_height:  # If person is under the sea
                people.remove(person)  # Person is considered "lost"
            elif person[1] <= 0:  # If person reaches the top of the screen (safety)
                people_saved_count += 1 #number of persons saved increase by 1
                people.remove(person)  # Person is saved and removed from screen

        # Check if all people are either saved or lost (function to end the game when 5 persons are either lost of saved)
        if len(people) == 0:
            game_state = 2  # Game over

# Third game state: game over
    elif game_state == 2:
        textAlign(CENTER)
        textSize(32)
        fill(0)
        text("Game Over", width / 2, height / 2)
        text(people_saved_count, width / 2, height / 2 + 50)
        text("Press R to Restart", width / 2, height / 2 + 100)  # Restarting the game
        if keyPressed and key == 'r':
            reset_game()  # Restart the game

# Function to reset the game
def reset_game():
    global sea_level_height, people, people_saved_count, game_state, peopleSpeed
    sea_level_height = 100
    people_saved_count = 0
    peopleSpeed = 0  # Reset people speed
    people = []
    for i in range(people_remaining):
        people.append([random(0, width), random(400, height)])  # People start randomly, within screen height
    game_state = 0  # Reset to the title screen
