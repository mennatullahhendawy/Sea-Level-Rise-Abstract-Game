# Sea Level Rise Abstract Game
 
Sea Level Rise Game
This repository contains the Sea Level Rise Game developed as part of the Game Development 1 course at the University of California, Santa Cruz. The game simulates the effects of sea level rise due to climate change, and players are tasked with saving people from rising waters by moving them to higher ground.

Acknowledgments
This project was developed as an assignment for the Game Development 1 course (GAME 235) at the University of California, Santa Cruz. The code was developed with the help of Mohamed Samy. Additionally, we used ChatGPT to assist in structuring and refining parts of the project. The game concept is inspired by  
by the 2023 Interdisciplinary Innovation Program (I2P), a collaboration between CITRIS at UC Santa Cruz and the campus’s Innovation & Business Engagement Hub. The program funds projects aimed at addressing climate resilience, with a focus on solutions to California’s climate challenges. Building on the initiative led by Prof. Magy Seif El-Nasr, chair of the Department of Computational Media, and Prof. Brent Haddad, professor of environmental studies, our game aims to explore how serious games can drive climate-conscious behavior at both policy and household levels. The project is coordinated by Dr. Mennatullah Hendawy. The game uses the context of sea level rise to raise awareness and simulate the urgent need for action in the face of rising waters, aligning with the I2P's mission to innovate for climate resilience.

Overview
The Climate Impact Game is a serious game focusing on the challenges of sea level rise. The player must help people living on the seashore move to higher ground before they are overtaken by the rising sea. The game aims to raise awareness of the effects of climate change and the importance of behavior change in climate resilience.

Grading Rubric Fulfillment
•	1 point: Title screen where a given key starts the game. (DONE)
•	3 points: Countdown timer and sea level rise simulation, affected by rising rainfall. (DONE)
•	1 point: Players press a key to move people upward. (DONE)
•	1 point: The speed at which people move increases the longer the player holds the key. (DONE)
•	1 point: A results screen appears after saving or losing people. (DONE)
•	2 points: The total number of people saved is displayed on the results screen. (DONE)
•	1 point: Players can restart the game from the results screen by pressing a given key. (DONE)

Installation
1.	Download and install Processing.
2.	Enable Python Mode:
o	Open Processing.
o	Go to the Mode drop-down menu at the top right.
o	Select Python mode from the list.
3.	Clone or download this repository to your local machine.
4.	Open the climate_impact_game.pde file in Processing.

Usage
Controls
•	Press SPACE: Starts the game and moves people upward to escape the rising sea.
•	Press R: Restarts the game from the results screen.
Running the Program
1.	Launch Processing.
2.	Open the climate_impact_game.pde file from this repository.
3.	Click the Run button in Processing to start the game.
4.	On the title screen, press SPACE to begin the game.
5.	Move people upward by holding down SPACE to save them from the rising sea.
6.	The game ends when all people are either saved or lost.
7.	Press R to restart the game from the results screen.

Game Features
•	Sea Level Rise: The sea level rises gradually as the game progresses, simulating the effects of climate change.
•	Saving People: Players must move people upward to escape the rising sea, and their speed increases the longer the key is held.
•	Results Screen: Displays the number of people saved and provides an option to restart the game.
•	Replayability: Players can restart the game after each round by pressing R.

Example Code Snippet
```python
Copy code
# Initiating game fixed variables
game_state = 0  # 0 = Title Screen, 1 = Playing, 2 = Game Over
sea_level_height = 100
people_remaining = 5  # Number of people to save
people = []  # List to store people positions
sea_rising_speed = 1
people_saved_count = 0  # Count of people saved
peopleSpeed = 0  # Speed at which people move upward

def setup():
    global people
    size(800, 600)
    for i in range(people_remaining):
        people.append([random(0, width), random(400, height)])  # Random positions for people

def draw():
    global game_state, sea_level_height, people_saved_count, peopleSpeed, sea_rising_speed

    background(135, 206, 250)  # Sky blue background

    # Title Screen
    if game_state == 0:
        textAlign(CENTER)
        textSize(32)
        fill(0)
        text("Press SPACE to Start", width / 2, height / 2)
        if keyPressed and key == ' ':
            game_state = 1  # Start the game

    # Gameplay
    elif game_state == 1:
        sea_level_height += sea_rising_speed  # Sea level rises over time
        sea_rising_speed += 0.01  # Increase the speed of sea level rise

        # Draw the sea level
        fill(0, 0, 255, 128)  # Semi-transparent blue for the sea
        rect(0, height - sea_level_height, width, sea_level_height)

        # Draw and move people
        for person in people:
            if keyPressed and key == ' ':
                person[1] -= peopleSpeed  # Move people upwards
                peopleSpeed += 0.05  # Increase speed gradually
            fill(255, 0, 0)  # Red color for people
            circle(person[0], person[1], 20)  # Draw people as red circles

            # Check if the person is under the sea level or saved
            if person[1] >= height - sea_level_height:
                people.remove(person)  # Person is lost
            elif person[1] <= 0:
                people_saved_count += 1  # Person is saved
                people.remove(person)  # Remove from the screen

        # Game over if all people are saved or lost
        if len(people) == 0:
            game_state = 2  # Game over

    # Game Over Screen
    elif game_state == 2:
        textAlign(CENTER)
        textSize(32)
        fill(0)
        text("Game Over", width / 2, height / 2)
        text(people_saved_count, width / 2, height / 2 + 50)
        text("Press R to Restart", width / 2, height / 2 + 100)
        if keyPressed and key == 'r':
            reset_game()  # Restart the game

# Function to reset the game
def reset_game():
    global sea_level_height, people, people_saved_count, game_state, peopleSpeed
    sea_level_height = 100
    people_saved_count = 0
    peopleSpeed = 0
    people = []
    for i in range(people_remaining):
        people.append([random(0, width), random(400, height)])  # Reset positions
    game_state = 0  # Back to the title screen
 

