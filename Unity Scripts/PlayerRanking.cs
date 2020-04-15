using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using HutongGames.PlayMaker;
using System.Text.RegularExpressions;
using System.Globalization;
using System.Net;

public class PlayerRanking : MonoBehaviour
{
    System.DateTime now;

    // Start is called before the first frame update
    void Start()
    {

    }

    void OnEnable()
    {
        now = System.DateTime.Now;
        //Debug.Log(now);

        if (!PlayerPrefs.HasKey("DateTimeRanking")) // First time booting game
        {
            if (PlayerPrefs.HasKey("Username")) // Only reset if username has been set
            {
                PlayerPrefs.SetString("DateTimeRanking", now.ToBinary().ToString()); // first time player boots up game, the timer begins
                Reset();
                Debug.Log("Resetting because player prefs not established");
            }
        }
        else
        {   
            long temp = System.Convert.ToInt64(PlayerPrefs.GetString("DateTimeRanking")); // grabs saved date time from player prefs
            System.DateTime oldDate = System.DateTime.FromBinary(temp);
            //Debug.Log("oldDate :" + oldDate);

            System.TimeSpan difference = now.Subtract(oldDate); // gets difference between saved time and current time
            double hours = difference.TotalHours;
            //print("Difference: " + difference);
            //print("hours: " + hours);

            if (hours > 168) // over 1 week since reset
            {
                PlayerPrefs.SetString("DateTimeRanking", now.ToBinary().ToString());
                Reset();
                Debug.Log("Reset because time out");
            }
            else
            {
                PullFromPrefs();
                Debug.Log("Pulling from Prefs");
            }
        }


        // grabs past data by either reseting or pulling from player prefs
        /*if (!PlayerPrefs.HasKey("PlayerName0"))
        {
            Reset();
        }
        else
        {
            PullFromPrefs();
        }*/

        int player_index = -1;
        // copies player name array so the index of the player can be found
        for (int i = 0; i<=8; i++)
        {
            // if the name is the players username, then the player's score will go here
            if (FsmVariables.GlobalVariables.GetFsmArray("PlayerNames").Get(i).ToString() == PlayerPrefs.GetString("Username"))
            {
                player_index = i;
            }
            else 
            {
                FsmArray score = FsmVariables.GlobalVariables.GetFsmArray("PlayerScores");

                int new_score = int.Parse(score.Get(i).ToString()) + Random.Range(0,2);
                score.Set(i, new_score);
            }
        }

        FsmVariables.GlobalVariables.FindFsmArray("PlayerScores").Set(player_index, PlayerPrefs.GetInt("Level"));
        FsmVariables.GlobalVariables.FindFsmArray("PlayerAvatars").Set(player_index, FsmVariables.GlobalVariables.FindFsmArray("AvatarsList").Get(FsmVariables.GlobalVariables.FindFsmInt("CurrentAvatar").Value));

        // sort lists
        Sort();

        // save player prefs for names, avatars, and scores based on sorted list. sets correct animation
        for (int i = 0; i <= 8; i++)
        {
            // sets animation based on where player is ranked
            if (FsmVariables.GlobalVariables.GetFsmArray("PlayerNames").Get(i).ToString() == PlayerPrefs.GetString("Username"))
            {
                transform.parent.GetComponent<Animator>().SetInteger("ranking", i + 1);
            }

            PlayerPrefs.SetString("PlayerName" + i, FsmVariables.GlobalVariables.GetFsmArray("PlayerNames").Get(i).ToString());
            PlayerPrefs.SetInt("PlayerScore" + i, int.Parse(FsmVariables.GlobalVariables.GetFsmArray("PlayerScores").Get(i).ToString()));

            GameObject avatar = (GameObject)FsmVariables.GlobalVariables.FindFsmArray("PlayerAvatars").Get(i);
            PlayerPrefs.SetInt("PlayerAvatar" + i, int.Parse(Regex.Match(avatar.name, @"\d+").Value) - 1);
        }
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    void Sort()
    {
        FsmArray scores = FsmVariables.GlobalVariables.GetFsmArray("PlayerScores");
        int[] new_scores = new int[9];
        GameObject[] new_avatars = new GameObject[9];
        string[] new_names = new string[9];

        // loops until array is sorted
        for (int i = 0; i < scores.Length; i++)
        {
            int max = -1;
            int max_index = -1;

            // loops over old array to find min
            for (int j = 0; j < scores.Length; j++)
            {
                if (int.Parse(scores.Get(j).ToString()) > max) // compares current value to min
                {
                    max = int.Parse(scores.Get(j).ToString()); // sets min
                    max_index = j;
                }
            }

            new_scores[i] = max;
            new_names[i] = FsmVariables.GlobalVariables.FindFsmArray("PlayerNames").Get(max_index).ToString();
            new_avatars[i] = (GameObject)FsmVariables.GlobalVariables.FindFsmArray("PlayerAvatars").Get(max_index);
            scores.Set(max_index, -1);
        }

        // sets scores to new score array
        for (int i = 0; i <= 8; i++)
        {
            FsmVariables.GlobalVariables.GetFsmArray("PlayerNames").Set(i, new_names[i]);
            FsmVariables.GlobalVariables.GetFsmArray("PlayerScores").Set(i, new_scores[i]);
            FsmVariables.GlobalVariables.GetFsmArray("PlayerAvatars").Set(i, new_avatars[i]);
        }
    }

    void PullFromPrefs()
    {
        for (int i = 0; i <= 8; i++)
        {
            FsmVariables.GlobalVariables.GetFsmArray("PlayerNames").Set(i, PlayerPrefs.GetString("PlayerName" + i));
            FsmVariables.GlobalVariables.GetFsmArray("PlayerAvatars").Set(i, FsmVariables.GlobalVariables.FindFsmArray("AvatarsList").Get(PlayerPrefs.GetInt("PlayerAvatar" + i)));
            FsmVariables.GlobalVariables.GetFsmArray("PlayerScores").Set(i, PlayerPrefs.GetInt("PlayerScore" + i));
        }
    }

    private void Reset()
    {
        FsmVariables.GlobalVariables.GetFsmArray("PlayerNames").Set(0, PlayerPrefs.GetString("Username")); // sets player's username in first name slot
        PlayerPrefs.SetString("PlayerName0", PlayerPrefs.GetString("Username"));

        // randomly generates other 8 names
        for(int i = 1; i<=8; i++)
        {
            FsmVariables.GlobalVariables.GetFsmArray("PlayerNames").Set(i, FsmVariables.GlobalVariables.GetFsmArray("UsernameList").Get(Random.Range(0, 49)));
            PlayerPrefs.SetString("PlayerName" + i, FsmVariables.GlobalVariables.GetFsmArray("PlayerNames").Get(i).ToString());
        }

        FsmVariables.GlobalVariables.GetFsmArray("PlayerAvatars").Set(0, FsmVariables.GlobalVariables.GetFsmArray("AvatarsList").Get(FsmVariables.GlobalVariables.FindFsmInt("CurrentAvatar").Value - 1)); // sets player's avatar in first name slot
        PlayerPrefs.SetInt("PlayerAvatar0", FsmVariables.GlobalVariables.FindFsmInt("CurrentAvatar").Value - 1);

        // randomly generates other 8 avatars
        for (int i = 1; i <= 8; i++)
        {
            int rand = Random.Range(0, 14);
            FsmVariables.GlobalVariables.GetFsmArray("PlayerAvatars").Set(i, FsmVariables.GlobalVariables.GetFsmArray("AvatarsList").Get(rand));
            PlayerPrefs.SetInt("PlayerAvatar" + i, rand);
        }

        // Reset player score
        FsmVariables.GlobalVariables.FindFsmInt("Level").Value = 0;
        PlayerPrefs.SetInt("Level", 0);

        // resets all scores to 0
        for (int i = 1; i <= 8; i++)
        {
            FsmVariables.GlobalVariables.GetFsmArray("PlayerScores").Set(i, 0);
            PlayerPrefs.SetInt("PlayerScore" + i, 0);
        }
    }
}
