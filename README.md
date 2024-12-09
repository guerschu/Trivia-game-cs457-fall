# Trivia Game 

We wanted to make a fun terminal co-op game where you and your friends can test your Trivia knowledge!

**Describe All Functions In Client**
1. Network Connection:
 * The code establishes a socket connection to the specified host and port. It sends and receives messages using a custom protocol, including a 64-byte header for message length.
2. Game Interaction:
* The start function initiates the game, sends the username to the server, and enters a loop to receive and process server messages. It handles different message types:
        Server messages: Printed to the console.
        Prompt messages (starting with "!"): Trigger user input and send the response to the server.
## How To Run
* When it comes to running this trivia game to set up a server all you need is to type "server.py -p "#####" (w/o the quotes)
    * This will allow the server to be able to run and start
* When it comes to the clients, a lot more goes into it! in the terminal you can type "python3 client.py -i (lab machine name or IP address here) -p (the port number). This client can run as many people as you would like but we need at least two to start the trivia game!
* Now we are running those commands on the client side it is going to ask for the username you would like to use! Make it anything you want! Then going to ask for a category you would like to try Animal, History, and Location! All have 6 questions to test your knowledge!
* Once you answer it will wait till all the other players have answered the question then show the scoreboard, leading into the next question. All players must answer the question before being allowed to move on!
* Once you have answered all the questions you are going to see who won and be prompted to ask to play again! 

**Describe All Functions In Server**
1. Data Structures:
   * players: Stores information about connected players, including their IP address, game progress (GP), and selected category (SEL).
   * Answers: Contains correct answers for different categories.
   * Questions: Maps categories to their respective questions.

2. Server Functionality:
   * Connection Handling: Accepts incoming connections and spawns threads to handle each client.
    * Message Handling: Receives messages from clients, logs them, and sends responses.
    * Player Management: Updates the player's dictionary with player information and handles disconnections.

**Limitation of The Game**
* the lack of security is a main limitation of the game, if we were able to have more time to add the encryption would be a great way to get rid of this limitation
* There is no team-based part of the game that someone might want from this like they added into Kahoot.
* 

**How to play:**
1. **Start the server:** Run the `server.py` script. 'IP' 'Port number'
2. **Connect clients:** Run the `client.py` client is going to take three inputs from the terminal 'host IP address' 'port number' 'trivia' 'what kind of trivia you would like to play' 'the player name for the game'
3. **Pick Trivia:** We only have 'animal' trivia as an option, more soon to come to pick to be able to have a variety of fun trivia options
   * Animal
   * History
   * Locations
4. **Play the game:** Trying to get the most points by getting the most correct answers.  (not fully implemented yet)


**Technologies used:**
* Python 
* Sockets
* Splash
* Threading

**Text-Editor**
* We have decided to go with Visual Studio Code to work with when developing this game in Python

**Libraries**
*Here is where we will put what Libraries we are using as we find them*
*  sys
* socket
* selectors
* types
* Sockets
* Splash
* Threading

**Additional resources:**
* coming soon!

**Challenges**
* When it comes to making this game, we have run into many different issues that have caused hiccups along the way.
* When we first started this game we followed the code in the homework which led us astray since it was things we were not fully getting we were using, so we last minute decided to switch everything up and go with our way of coding it so the server and the client talk. We wanted to make a trivia game that seems closer to Kahoot in the way people who answer faster are the ones who get more points for their answers on correctness and time. We also learned how to communicate better about the code and functions we are thinking of since we cannot read the other brain.
* This project has taught us much about how to do things in a group and more about threading/server communications.

## Retrospective

### RoadMap
* If we had more than a semester would be nice to make it into a webserver that is similar to Kahoot allowing people to join into lobbies and pick an avatar along with a username.
* Another great add would be a chat function when waiting in between the questions to be able to tease those or talk while they wait.
* Making the lobbies more specific would also be a great add so that anyone who joins can see who is joining the lobby and prompt them to see if they are ready to start to play and able to give a chance for all who want to play to join before the questions load up.
* This could have more of a life than just this, but for the sake of our sanity, this is as much as we were able to get done.

### What Went Right
* Things that went right were once we changed to threading being able to run many clients and using a better way to show the questions and to show them
* Logging once was implemented was a great thing that never caused an issue.
* Getting to send things back and forth from the client and server went very smoothly once we were able to break away from the code provided in the homework to something that we both would be able to understand a whole lot better.

### Things that could be improved on
* How to clean our code way at points and add comments so when we both look at things we would be able to jump right into the code without having to fiddle around so much about what they other wrote to see if we could add to it or fix it
* I would say the way we send things from the server to client before of usernames and keeping better track
* the lobby dictionary is a lot to do so much and would have liked to be able to make a better way of keeping track to also help with the code cleanness.
* I think if we did not stick so close to the HWs from this semester and went with something we already know like threading we would have been a lot better set for this project to get milestones a lot better and not have to play catch up so late.
