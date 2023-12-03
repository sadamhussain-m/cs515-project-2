# CS515-Project-2

Sadam Mohamed Usman,smohamed1@stevens.edu 
Sathya Kalyan Paladugu,spaladu3@stevens.edu
https://github.com/sadamhussain-m/cs515-project-2

1.an estimate of how many hours you spent on the project

We have spent 12 hours on this project development

2.a description of how you tested your code

We have tested our code with the reference from the loop.map file and ambig.map file from the project's documentation.We have tested our code in considering all the corner cases of the baseline behaviour features and extensions feature by giving invalid commands on directions of exits and items to pick and drop on the patricular room and by providing case sensitive and insensitive commands to check whether the engine able to parse it or not.Also while testing 

Case 1:whether the game engine able to parse the shortcuts of directions of exits given by the user as [n,w,s,e,nw,ne,se,sw] without the go command.

Case 2:Whether the game engine able to recommend items to the user if any of the user's item to pick character string matches with the list of the items of the room as below.

What would you like to do? get b
Did you want to get the banana, bandana or the bellows?
What would you like to do? get be
You pick up the bellows.
What would you like to do? get ban
Did you want to get the banana or the bandana?

Case 3:Whether the game engine ale to recommend the directions to the user if any of the characters of the direction of exits matches with the list of directions of exits

3.any bugs or issues you could not resolve
There are no issues and bugs as far as we tested our code.

4.an example of a difficult issue or bug and how you resolved?

In the case of drop feature if the user drops an items to the room.If the room doesn't contains items list then the item can't be dropped from the inventory.So in this scenario I wrote a condition in checking the items property exits in the room.If not,I added an items property to the room object so that the insertion of the items will be done easily.


5.a list of the extensions you’ve chosen to implement, with appropriate detail on them for the CAs to evaluate them (i.e., what are the new verbs/features, how do you exercise them, where are they in the map)

The list of extensions that we are implemented are:
1.drop:
Implemented the drop feature as mentioned in the documentation.You can test the code with the ambig.map file

2.Help:
Implemented the help feature as mentioned in the documentation.You can test the code with the ambig.map file

3.Direction become verbs:
Implemented the directions become verb feature.With this feature if the user enters the commands of exits as shortcut [ n,w,e,s,nw,ne,se,sw] the user will be entered in to the respective room with the go command

4.Items should be matchable based on any included string:
Implemented the above item matching feature which would recommend the user in selecting the item if multiple matches of the item to pick matches with the list of items.If there is one it will automatically
add the item to the user's inventory and delete it from the room's items list.
What would you like to do? get b
Did you want to get the banana, bandana or the bellows?
What would you like to do? get be
You pick up the bellows.
What would you like to do? get ban
Did you want to get the banana or the bandana?

5.Abbreviations for Direction:

Implemented the abbreviations for direction feature it will recommend the user if any of the user exit string matches with the direction of exits list as

==>>go n will ask to the user whether in going in the direction of north or northwest as [n] matches with the list of exits string

==>Also go wes will ask to the user whether in going in the direction of west or northwest as [wes] matches with the list of exits stringgo n will ask to the user whether in going in the direction of north or northwest as n matches with the list of exits string?

==>Also go eas will ask to the user whether in going in the direction of east or southeast as [eas] matches with the list of exits stringgo n will ask to the user whether in going in the direction of north or northwest as n matches with the list of exits string?
 
