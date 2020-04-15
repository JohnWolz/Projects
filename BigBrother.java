/**
 * A program that simulates Big Brother using 16 different house guests
 *
 * John Wolz
 * version 1.0.9
 * 
 * ---Version History---
 *  *version 1.0.0: initial version
 *  *version 1.0.1: added jury
 *  *version 1.0.2: fixed veto bug for when pulled player won
 *  *version 1.0.3: added a chance for hoh to back door someone
 *  *version 1.0.4: added vote counts, and included them in eviction
 *  *version 1.0.5: made renominations into its own method, cutting down on repeated code
 *  *version 1.0.6: added ability to include different number of house guest, other than 16
 *  *version 1.0.7: made house_guests directly come from houseGuests, making program simpler
 *  *version 1.0.8: created player types and genders
 *  *version 1.0.9: updated the way the program finds random values, cutting back on extra code
 */
import java.util.Random;
import java.util.ArrayList;

public class BigBrother
{
    public static Random random = new Random(); //creates random variable
    
    public static Object randomValue(ArrayList list) //randomization method
    {
        Object random_value = list.get(random.nextInt(list.size())); //finds a random index, and pulls the list value at that index
        
        return random_value;
    }
    
    public static Object reNom(Boolean replacement_good, ArrayList houseGuests, Object hoh, Object nom1, Object nom2, Object veto_winner) //method for determining eligible renominations
    {
        Object replacement_nom = "none"; //no replacement nom has been named
        
        while (replacement_good == false)
                    {
                        replacement_nom = BigBrother.randomValue(houseGuests); //finds random hg
                
                        if (replacement_nom != hoh && replacement_nom != nom1 && replacement_nom != nom2 && replacement_nom != veto_winner) //checks if eligable
                        {
                            replacement_good = true; //breaks out
                        }
                    }
        
        return replacement_nom; //returns the eligible nominee
    }
    
    public static int juryStart(int house_guests) //determines start of jury with given number of house guests
    {
        int jury_start; 
        
        if ((house_guests / 2) % 2 == 0) //if house guests / 2 is even
        {
            jury_start = (house_guests / 2) + 1; //the jury will start once half + 1 players remain, making a jury of half - 1 players, because of final 2
        }
        else //house guests / 2 is odd
        {
            jury_start = (house_guests / 2); //the jury will start once half of the players remain, making a jury of half of the players - 2, because of final 2
        }
            
        return jury_start;
    }
    
    public static Object hohComp(ArrayList houseGuests, Object prev_hoh) //hoh comp method
    {
        Boolean hoh_good = false; //hoh is not set
        Object temp_hoh = "null"; //no temp hoh yet
        
        while (hoh_good == false)
        {
            temp_hoh = BigBrother.randomValue(houseGuests); //finds random house guest
            if (temp_hoh != prev_hoh) //if they are not already hoh, they are now
            {
                hoh_good = true;
            }
        }
        
        return temp_hoh;
    }
    
    public static ArrayList nominations(ArrayList houseGuests, Object hoh_player) //nomination ceremony method
    {
        Object hoh = hoh_player;
        Boolean nom_good = false; //states that the nominations are not set
        Object nom1 = "temp"; //initilizes nom1
        ArrayList nominees = new ArrayList(); //initlizes nominees array
        
        while (nom_good == false) //repeated until nom1 is set
        {
            Object temp_nom = BigBrother.randomValue(houseGuests); //gets random houseguest
            if (temp_nom != hoh) //checks for eligibility
            {
                nominees.add(temp_nom); //sets nomnation
                nom1 = temp_nom;
                nom_good = true; //breaks out
            }
        }
        
        nom_good = false;
        while (nom_good == false) //same as above, but for second nominee
        {
            Object temp_nom = BigBrother.randomValue(houseGuests);
            if (temp_nom != hoh && temp_nom != nom1)
            {
                nominees.add(temp_nom);
                nom_good = true;
            }
        }
        
        /*for (int i = 0; i < 2; i++)
        {
            while (nom_good == false)
            {
                Object temp_nom = BigBrother.randomValue(hgs); //gets random houseguest
                if (temp_nom != hoh && temp_nom != nom1) //checks for eligibility
                {
                    nominees.add(temp_nom); //sets nomnation
                    
                    if (i == 0)
                        nom1 = temp_nom;
                    
                    nom_good = true; //breaks out
                }
            }
        }*/
            
        
        return nominees;
    }
    
    public static ArrayList vetoPlayerMeeting(ArrayList houseGuests, Object hoh, Object nom1, Object nom2) //Veto player meeting method
    {
        ArrayList temp_veto_players = new ArrayList(); //initializes veto player array
        
        temp_veto_players.add(hoh); //makes hoh play in veto
        temp_veto_players.add(nom1); // makes nom1 play in veto
        temp_veto_players.add(nom2); //makes nom2 play in veto
        temp_veto_players.add("3"); //saves room for other player
        temp_veto_players.add("4"); //saves room for other player
        temp_veto_players.add("5"); //saves room for other player
        
        int rest_of_players = 3; //sets number to current index
        
        while (rest_of_players < 6) //assures 3 more will be selected
        {
            Object temp_veto_player_random = BigBrother.randomValue(houseGuests); //pulls random house guest
            
            if (temp_veto_player_random != hoh && temp_veto_player_random != nom1 && temp_veto_player_random != nom2) //assures house guest is not hoh or non
            {
                if (temp_veto_players.get(3) != temp_veto_player_random && temp_veto_players.get(4) != temp_veto_player_random && temp_veto_players.get(5) != temp_veto_player_random) //assures house guest is not already playing
                {
                    temp_veto_players.set(rest_of_players, temp_veto_player_random);
                    rest_of_players++; //incriments index number
                }    
            }
        }
        
        return temp_veto_players;
    }
    
    public static ArrayList lateGameVetoPlayerMeeting(ArrayList houseGuests) //Late Game Veto Player meeting method
    {
        ArrayList temp_veto_players = new ArrayList(houseGuests); //all house guests play in veto
        return temp_veto_players;
    }
    
    public static Object vetoComp(ArrayList veto_players) //Veto Compitition method
    {
        Object veto_winner = BigBrother.randomValue(veto_players); //selects a random veto player to win
        return veto_winner;
    }    
    
    public static ArrayList vetoCeremony(Object hoh, Object nom1, Object nom2, Object veto_winner, ArrayList houseGuests) //Veto Ceremony method
    {
        ArrayList post_veto_noms = new ArrayList(); //initilizes post veto nom array
     
        int veto_use; //creates a value for if veto is used
        
        Object replacement_nom; //initilizes replacement nom
        Boolean replacement_good; //initilizes replacement check boolean
        
        if (veto_winner == hoh) //if hoh won veto it is not used
        {
            int backdoor = random.nextInt(5); //makes a 1 in 5 chance for a backdoor
        
            if (backdoor != 0) //if it is not equal to the 4th spot in backdoor, the 1, then there is no backdoor
            {
                post_veto_noms.add(nom1);
                post_veto_noms.add(nom2);
            }
            
            else
            {
                veto_use = random.nextInt(2); //decided if veto is used
                
                if (veto_use == 0) //if 0, nom1 is saved
                {
                    post_veto_noms.add(nom2); //nom2 is not saved
                    replacement_good = false;
                    
                    replacement_nom = BigBrother.reNom(replacement_good, houseGuests, hoh, nom1, nom2, veto_winner); //calls renom method
                    
                    post_veto_noms.add(replacement_nom);   
                }
                
                else //if 1, nom2 is saved
                {
                    post_veto_noms.add(nom1); //nom1 is not saved
                    replacement_good = false;
                    
                    replacement_nom = BigBrother.reNom(replacement_good, houseGuests, hoh, nom1, nom2, veto_winner); //calss renom method
                    
                    post_veto_noms.add(replacement_nom);
                }
            }
        }
        
        else if (veto_winner == nom1) // if nom1 wins veto, it is used on nom1 
        {
            post_veto_noms.add(nom2); // it is not used on nom2
            replacement_good = false;
            
            replacement_nom = BigBrother.reNom(replacement_good, houseGuests, hoh, nom1, nom2, veto_winner); //calls renom method
            
            post_veto_noms.add(replacement_nom);
        }
        
        else if (veto_winner == nom2) // if nom2 wins veto, it is used on nom2
        {
            post_veto_noms.add(nom1); // it is not used on nom1
            replacement_good = false;
            
            replacement_nom = BigBrother.reNom(replacement_good, houseGuests, hoh, nom1, nom2, veto_winner); //calls renom method
            
            post_veto_noms.add(replacement_nom);
        }
        
        else //decides if veto winner will use veto is not on the block or hoh
        {
            veto_use = random.nextInt(2); //finds if veto is used
            
            if (veto_use == 0) //if 0, veto is not used
            {
                post_veto_noms.add(nom1);
                post_veto_noms.add(nom2);
            }
            
            //else if (random == chance.get(1)) //if 1, veto is used
            else
            {
                veto_use = random.nextInt(2);
                
                if (veto_use == 0) //if 0, nom1 is saved
                {
                    post_veto_noms.add(nom2); //nom2 is not saved
                    replacement_good = false;
                    
                    replacement_nom = BigBrother.reNom(replacement_good, houseGuests, hoh, nom1, nom2, veto_winner); //calls renom method
                    
                    post_veto_noms.add(replacement_nom);
                }
                
                else //if 1, nom2 is saved
                {
                    post_veto_noms.add(nom1); //nom1 is not saved
                    replacement_good = false;
                    
                    replacement_nom = BigBrother.reNom(replacement_good, houseGuests, hoh, nom1, nom2, veto_winner); //calls renom method
                    
                    post_veto_noms.add(replacement_nom);
                }
            }
        }
        
        return post_veto_noms;
    }
    
    public static ArrayList eviction(ArrayList nominees, ArrayList houseGuests) //eviction method
    {
        ArrayList chance = new ArrayList(); //creates chance list to use in determining votes
        chance.add(0);
        chance.add(1);
        
        Object evicted;
        
        int nom_1_votes = 0; //initilizes votes for noms 1 and 2
        int nom_2_votes = 0;
        
        int eviction_vote;
        
        for (int i=1; i <= (houseGuests.size() - 3); i++) // runs until all eligible voters vote 
        {
            eviction_vote = random.nextInt(2); //decides on current eviction vote
            
            if (eviction_vote == 0) //the voter votes for nom 1 to leave
            {
                nom_1_votes ++; //votes for nom 1 increase
            }
            else //the voter votes for nom 2 to leave
            {
                nom_2_votes ++; //votes for nom 2 increase
            }
        }
  
        if (nom_1_votes > nom_2_votes) //if nom 1 has more votes, they leave and become the evicted value
        {
            evicted = nominees.get(0);
        }
        else if (nom_2_votes > nom_1_votes) //same as above, but with nom 2
        {
            evicted = nominees.get(1);
        }
        else //if its a tie, the HOH casts the deciding vote, which is random
        {
            evicted = BigBrother.randomValue(nominees);
        }
        
        ArrayList eviction_list = new ArrayList(); //creates a list to return, and fills it with votes and evicted house guest
        eviction_list.add(nom_1_votes);
        eviction_list.add(nom_2_votes);
        eviction_list.add(evicted);
        
        return eviction_list;
        
    }
    
    public static ArrayList finalTwo(Object hoh, ArrayList houseGuests) //dinal two method
    {
        ArrayList final_two = new ArrayList();
        final_two.add(hoh); //hoh makes it to final two
        
        Object other; //person hoh brings
        
        Boolean final_two_good = false; //final two is not set
        while (final_two_good == false)
        {
            other = BigBrother.randomValue(houseGuests); //finds random house guest out of final 3
            
            if (other != hoh) // if not hoh, they make it to final two
            {
                final_two.add(other);
                final_two_good = true;
            }
        }
        
        return final_two;
    }
    
    public static void main(String[] args) //main section of the program
    {
        //-------------------------------------------------------------------------------------
        // Variable Declaration Section
        //-------------------------------------------------------------------------------------
        ArrayList houseGuests = new ArrayList(); //creates the houseguests, and populates them with the names specified below
        ArrayList player_type = new ArrayList(); //states which comp type the player is best at, p = physical, m = mental, s = social
        ArrayList gender = new ArrayList(); //keeps track of the players gender, m for male, f for female
        
        /*1*/   houseGuests.add("John");
                player_type.add("m");
                gender.add("m");
        
        /*2*/   houseGuests.add("Kenzie");
                player_type.add("m");
                gender.add("f");
        
        /*3*/   houseGuests.add("Shelby");
                player_type.add("s");
                gender.add("m");
        
        /*4*/   houseGuests.add("Clayton");
                player_type.add("m");
                gender.add("m");
        
        /*5*/   houseGuests.add("Gabby");
                player_type.add("s");
                gender.add("f");
        
        /*6*/   houseGuests.add("Sydnie");
                player_type.add("s");
                gender.add("f");
        
        /*7*/   houseGuests.add("Josh");
                player_type.add("m");
                gender.add("m");
        
        /*8*/   houseGuests.add("Ally");
                player_type.add("p");
                gender.add("f");
        
        /*9*/   houseGuests.add("Avery");
                player_type.add("p");
                gender.add("f");
        
        /*10*/  houseGuests.add("Kason");
                player_type.add("m");
                gender.add("m");
        
        /*11*/  houseGuests.add("Brandan");
                player_type.add("p");
                gender.add("m");
        
        /*12*/ houseGuests.add("Jordanne");
                player_type.add("s");
                gender.add("f");
        
        /*13*/  houseGuests.add("Clara");
                player_type.add("s");
                gender.add("f");
        
        /*14*/  houseGuests.add("Dominique");
                player_type.add("m");
                gender.add("f");
        
        /*15*/  houseGuests.add("Brett");
                player_type.add("m");
                gender.add("m");
        
        /*16*/  houseGuests.add("Bren");
                player_type.add("p");
                gender.add("m");
        
        /*17*/  //houseGuests.add("Jared");
                //player_type.add("m");
                //gender.add("m");
        
        /*18*/  //houseGuests.add("Matt");
                //player_type.add("p");
                //gender.add("m");
        
        /*19*/  //houseGuests.add("Cora");
                //player_type.add("m");
                //gender.add("f");
        
        /*20*/  //houseGuests.add("Kristyn");
                //player_type.add("m");
                //gender.add("f");
        
        /*21*/  //houseGuests.add("Paxton");
                //player_type.add("p");
                //gender.add("m");
        
        /*22*/  //houseGuests.add("Billy");
                //player_type.add("p");
                //gender.add("f");
        
        /*23*/  //houseGuests.add("Joby");
                //player_type.add("p");
                //gender.add("m");
        
        /*24*/  //houseGuests.add("Kelli");
                //player_type.add("m");
                //gender.add("f");
        
        
        int house_guests = houseGuests.size();// sets number of house guests
        
        String pronoun;
        
        String full_player_type;
        
        ArrayList jury = new ArrayList(); //declares an Array List that is used for jury
        
        Object prev_hoh = "null"; //declares previous hoh variable, and sets it as null as there is no previous hoh when the game begins
        
        Object hoh; //declares hoh variable
        
        ArrayList noms; //declares nominations variable
        
        ArrayList veto_players; //declares an array list for veto players
        
        Object veto_winner; //creates veto winner variable
        
        ArrayList post_veto_noms; //creates a nomination list for after veto ceremony
        
        ArrayList evicted; //creates an evicted variable
        
        ArrayList final_two; //creates a final two variable
        
        Object winner; //creates a winner variable
        
        //-------------------------------------------------------------------------------------------
        // The Meat of the Program
        //-------------------------------------------------------------------------------------------
        
        int week = 1; //begins at week 1 
        
        int jury_start = BigBrother.juryStart(house_guests);
        
        System.out.println("--------------------------------------------------------------------------------------");
        
        System.out.println("Meet the House Guests!"); //runs info on house guests
        for (int i = 0; i < house_guests; i++) //does so for every house guest
        {
            if (gender.get(i) == "m") //finds appropriate pronoun based on gender
                pronoun = "He";
            else
                pronoun = "She";
            
            if (player_type.get(i) == "p") //finds player type
                full_player_type = "physical";
            else if (player_type.get(i) == "m")
                full_player_type = "mental";
            else
                full_player_type = "social";
            
            System.out.println(houseGuests.get(i) + ". " + pronoun + " is best at " + full_player_type + " competitions.");
        }
        
        System.out.println(" ");
        
        while (house_guests > 3) //final 3 is done differently
        {
            hoh = BigBrother.hohComp(houseGuests, prev_hoh); //Determines HOH from random houseguest
            
            noms = BigBrother.nominations(houseGuests, hoh); //Determines Nominees
        
            if (house_guests > 6)
            {
                veto_players = BigBrother.vetoPlayerMeeting(houseGuests, hoh, noms.get(0), noms.get(1)); //Determines Veto players
            }
            else
            {
                veto_players = BigBrother.lateGameVetoPlayerMeeting(houseGuests);
            }
        
            veto_winner = BigBrother.vetoComp(veto_players); //Determines Veto winner
        
            post_veto_noms = BigBrother.vetoCeremony(hoh, noms.get(0), noms.get(1), veto_winner, houseGuests); //Determines if Veto is used
        
            evicted = BigBrother.eviction(post_veto_noms, houseGuests); //Determines eviction
            houseGuests.remove(evicted.get(2)); //Renoves evictee from house Guest list
            house_guests--; //number of houseguests decreases
            
            if (house_guests < jury_start) //adds to jury
            {
                jury.add(evicted.get(2));
            }
           
            prev_hoh = hoh; //current hoh becomes previouse hoh
            
            
            System.out.println("WEEK " + week);
            System.out.println("HOH: " + hoh);
            System.out.println("Nominees: " + noms.get(0) + " and " + noms.get(1));
            System.out.println("Veto Players: " + veto_players);
            System.out.println("Veto Winner: " + veto_winner);
            System.out.println("Post Veto Nominees: " + post_veto_noms.get(0) + " and " + post_veto_noms.get(1));
            System.out.println("Evicted by a vote of " + evicted.get(0) + " to " + evicted.get(1) + ": " + evicted.get(2));
            System.out.println(house_guests + " House Guests Remaining: " + houseGuests);
            
            if (house_guests < jury_start)
            {
                System.out.println("Jury: " + jury);
            }
            
            System.out.println(" ");
            
            week++;
        }
        
        hoh = BigBrother.randomValue(houseGuests); //Determines final hoh
        final_two = BigBrother.finalTwo(hoh, houseGuests); //Determines final two
        winner = BigBrother.randomValue(final_two); //Determines winner
        
        System.out.println("FINAL WEEK");
        System.out.println("HOH: " + hoh);
        System.out.println("Final Two: " + final_two.get(0) + " and " + final_two.get(1));
        System.out.println("Winner: " + winner);
        System.out.println(" ");

    }  
}

