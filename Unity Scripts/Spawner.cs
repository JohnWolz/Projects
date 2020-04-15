using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using HutongGames.PlayMaker;

public class Spawner : MonoBehaviour
{
    public float spawn_rate;
    float timer;
    float dir;
    bool current_play_val;
    GameObject[] unfilled_squares;
    GameObject square;
    Vector3 square_pos;
    Vector3 pos;
    int initial_spawn_modifier;

    public Vector3 direction;

    public float angle_variance_min;
    public float angle_variance_max;
    public float filled_percentage_until_seeking;
    public float seeking_chance;

    public GameObject ball;
    GameObject spawnball;

    // Start is called before the first frame update
    void Start()
    {
        spawn_rate = FsmVariables.GlobalVariables.FindFsmFloat("SpawnRate").Value;

        ball = FsmVariables.GlobalVariables.FindFsmGameObject("Ball").Value;

        current_play_val = FsmVariables.GlobalVariables.FindFsmBool("Playing").Value;
    }

    void SetTimer()
    {
        timer = Random.Range(2, spawn_rate); // random spawn range around the given spawn rate
    }

    // Update is called once per frame
    void Update()
    {
        // CODE FOR INITIAL SPAWN
        if (current_play_val != FsmVariables.GlobalVariables.FindFsmBool("Playing").Value)
        {
            if (FsmVariables.GlobalVariables.FindFsmInt("Level").Value % 10 == 0) // code for bonus level
            {
                GameObject.Find("UI-BonusLevel").GetComponent<Animator>().SetBool("bonuson", true);
                Spawn();
                Spawn();
                Spawn();
            }

            // Chance for Initial Spawn
            int spawn_chance = Random.Range(0, 5);
            if (spawn_chance == 0)
            {
                initial_spawn_modifier = 20; // ensures that initial spawns will only be normal balls
                Spawn();
            }

            SetTimer();
        }

        if (!FsmVariables.GlobalVariables.FindFsmBool("Paused").Value)
        {
            current_play_val = FsmVariables.GlobalVariables.FindFsmBool("Playing").Value;
            
            timer -= Time.deltaTime; // timer counts down

            if (timer < .3f) // close enough to 0, time to spawn
            {
                if (FsmVariables.GlobalVariables.FindFsmBool("Playing").Value) // Only Spawn if the player is playing
                {
                    initial_spawn_modifier = 0;
                    Spawn();
                }
            }
        }
    }

    void CheckForPrioritySpots()
    {
        unfilled_squares = GameObject.FindGameObjectsWithTag("Clean");
        int index = Random.Range(0, unfilled_squares.Length);
        square = unfilled_squares[index];
        square_pos = new Vector3(square.transform.position.x, .25f, square.transform.position.z);

    }

    void Spawn()
    {      
        pos = new Vector3(0,0,0);

        if (this.gameObject.tag == "LR") // the spawner is on the right or the left, so z component is varied
        {
            pos = RandomPointInBoundsLR(this.GetComponent<BoxCollider>().bounds);
            direction.z = dir; // sets direction z to random angle 
        }
        else // spawner is on the top or bottom
        {
            pos = RandomPointInBoundsUD(this.GetComponent<BoxCollider>().bounds);
            direction.x = dir; // sets direction x to random angle
        }

        int rand_ball = Random.Range(0, 20) + initial_spawn_modifier;
        if (rand_ball == 0)
        {
            spawnball = FsmVariables.GlobalVariables.FindFsmGameObject("SpecialBall").Value; // special ball will spawn
        }
        else if (rand_ball <= 3)
        {
            spawnball = FsmVariables.GlobalVariables.FindFsmGameObject("BadBall").Value; // special ball will spawn
        }
        else
        {
            spawnball = ball;
        }

        if (FsmVariables.GlobalVariables.FindFsmFloat("GridPercent").Value >= filled_percentage_until_seeking) // most spaces are filled, balls have a chance to go towards unfilled space
        {
            if (Random.Range(0.0f, 1.0f) <= seeking_chance) // ball will go towards unfilled
            {
                CheckForPrioritySpots();

                GameObject ball_inst = Instantiate(spawnball, pos, Quaternion.identity);
                ball_inst.GetComponent<Ball>().direction = (square_pos - pos) / (square_pos - pos).magnitude;
            }       
            else
            {
                dir = Random.Range(angle_variance_min, angle_variance_max);

                if (this.gameObject.tag == "LR") // the spawner is on the right or the left, so z component is varied
                {
                    direction.z = dir; // sets direction z to random angle 
                }
                else // spawner is on the top or bottom
                {
                    direction.x = dir; // sets direction x to random angle
                }

                GameObject ball_inst = Instantiate(spawnball, pos, Quaternion.identity);
                ball_inst.GetComponent<Ball>().direction = direction;
            }
        }
        else
        {
            dir = Random.Range(angle_variance_min, angle_variance_max);

            if (this.gameObject.tag == "LR") // the spawner is on the right or the left, so z component is varied
            {
                direction.z = dir; // sets direction z to random angle 
            }
            else // spawner is on the top or bottom
            {
                direction.x = dir; // sets direction x to random angle
            }

            GameObject ball_inst = Instantiate(spawnball, pos, Quaternion.identity);
            ball_inst.GetComponent<Ball>().direction = direction;
        }

        SetTimer();
    }

    Vector3 RandomPointInBoundsLR(Bounds bounds) // finds random point in the collider
    {
        return new Vector3(
            this.transform.position.x,
            .25f,
            Random.Range(bounds.min.z, bounds.max.z)
        );
    }

    Vector3 RandomPointInBoundsUD(Bounds bounds) // finds random point in the collider
    {
        return new Vector3(
            Random.Range(bounds.min.x, bounds.max.x),
            .25f,
            this.transform.position.z
        );
    }
}
