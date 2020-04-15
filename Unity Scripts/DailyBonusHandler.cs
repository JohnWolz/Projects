using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class DailyBonusHandler : MonoBehaviour
{
    int temp;

    // Start is called before the first frame update
    void Start()
    {
        SetUI();
    }

    void SetUI()
    {
        if (PlayerPrefs.GetInt("CurrentReward") > 7)
        {
            PlayerPrefs.SetInt("CurrentReward", 1); // resets reward if the player is on a combo of greater than 7
        }

        int daily_bonus = PlayerPrefs.GetInt("CurrentReward");
        temp = daily_bonus;

        switch (daily_bonus)
        {
            case 1: // UI arragnement for 1st Reward
                gameObject.transform.Find("current").GetComponent<RectTransform>().localPosition = new Vector3(0, 330, 0);
                break;
            case 2: // UI arragnement for 1st Reward
                gameObject.transform.Find("current").GetComponent<RectTransform>().localPosition = new Vector3(0, 229, 0);
                break;
            case 3: // UI arragnement for 1st Reward
                gameObject.transform.Find("current").GetComponent<RectTransform>().localPosition = new Vector3(0, 128, 0);
                break;
            case 4: // UI arragnement for 1st Reward
                gameObject.transform.Find("current").GetComponent<RectTransform>().localPosition = new Vector3(0, 25, 0);
                break;
            case 5: // UI arragnement for 1st Reward
                gameObject.transform.Find("current").GetComponent<RectTransform>().localPosition = new Vector3(0, -75, 0);
                break;
            case 6: // UI arragnement for 1st Reward
                gameObject.transform.Find("current").GetComponent<RectTransform>().localPosition = new Vector3(0, -178, 0);
                break;
            case 7: // UI arragnement for 1st Reward
                gameObject.transform.Find("current").GetComponent<RectTransform>().localPosition = new Vector3(0, -280, 0);
                break;
        }

        for (int i = 1; i < daily_bonus; i++) // loops through day bonus ui and sets them to already claimed depending on what the current daily bonus is 
        {
            string day = "day" + i;
            GameObject day_obj = gameObject.transform.Find(day).gameObject;
            day_obj.GetComponent<Image>().color = new Color(255, 255, 255, .5f);
            day_obj.transform.Find("check").gameObject.GetComponent<Image>().enabled = true;
        }
    }

    // Update is called once per frame
    void Update()
    {
        if (temp != PlayerPrefs.GetInt("CurrentReward"))
        {
            SetUI();
        }

        //temp = PlayerPrefs.GetInt("CurrentReward");
    }
}
