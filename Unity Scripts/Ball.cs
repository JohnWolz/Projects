using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;
using HutongGames.PlayMaker;
using MoreMountains.NiceVibrations;

public class Ball : MonoBehaviour
{
    public Vector3 direction; // direction the ball will travel. set when spawned
    public float min_speed; // the mininum speed a ball can move at the beginning of the game 
    public float max_speed; // the maximum speed a ball can move at the beginning of the game
    public float speed_modifier; // the ammount both min and max speed will increase as the level is completed. (if level is 100% filled then newminspeed = minspeed + speed_modifyer)
    public GameObject splat_particles; // Game object that contains the particle effects for a ball splat
    public GameObject[] splats; // Array of gameobjects that contains all the splat objects
    public Material[] gridfills; // Array of materials that contains all the grid fill materials
    public Material ball_material; // The material for the ball. Different for ball and special ball
    public float rotation_speed_multiplier;

    float speed;
    int hits;
    int touch_timer;

    // Start is called before the first frame update
    void Start()
    {
        // alters starting speeds based off how much of the board is completed
        min_speed += speed_modifier * FsmVariables.GlobalVariables.FindFsmFloat("GridPercent").Value;
        max_speed += speed_modifier * FsmVariables.GlobalVariables.FindFsmFloat("GridPercent").Value;

        //speed = FsmVariables.GlobalVariables.FindFsmFloat("BallSpeed").Value;
        speed = Random.Range(min_speed, max_speed);

        if (!gameObject.name.Contains("bad"))
        {
            ball_material.color = FsmVariables.GlobalVariables.FindFsmColor("BallColor").Value;
        }

        if (name.Contains("special")) // additonal code for special balls
        {
            Debug.Log("speical");
            GetComponentInChildren<SpriteRenderer>().color = FsmVariables.GlobalVariables.FindFsmColor("BallColor").Value;
            hits = 3;
            speed /= 3;
        }

        transform.rotation = Quaternion.LookRotation(direction);
    }

    // Update is called once per frame
    void Update()
    {
        if (!FsmVariables.GlobalVariables.FindFsmBool("Playing").Value)
        {
            Destroy(this.gameObject);
        }
        if (!FsmVariables.GlobalVariables.FindFsmBool("Paused").Value) // only move if game not paused
        {
            transform.Translate(direction * speed * Time.deltaTime, Space.World); // moves the ball

            transform.Rotate(new Vector3(speed*rotation_speed_multiplier,0,0), Space.Self);

            //transform.GetChild(1).transform.Rotate(new Vector3(-speed*rotation_speed_multiplier, 0, 0), Space.Self);

            if (name.Contains("special")) // additonal code for special balls
            {
                TextMeshPro[] text = gameObject.GetComponentsInChildren<TextMeshPro>();
                text[0].text = hits.ToString();
            }

            // Touch Detection
            /*if (touch_timer <= 0)
            {
                if ((Input.touchCount > 0) && (Input.GetTouch(0).phase == TouchPhase.Began))
                {
                    Ray raycast = Camera.main.ScreenPointToRay(Input.GetTouch(0).position);
                    RaycastHit raycastHit;
                    if (Physics.Raycast(raycast, out raycastHit))
                    {
                        //Debug.Log("Something Hit");
                        if (raycastHit.collider == this.GetComponent<Collider>())
                        {
                            Debug.Log("hit ball");
                            HitBall();
                            touch_timer = 15;
                        }
                    }
                }
            }

            touch_timer--;*/
        }
    }

    private void OnMouseDown() // Performed when ball is touched
    {
        if (!FsmVariables.GlobalVariables.FindFsmBool("Paused").Value) // only if not paused
        {
            HitBall();
        }
    }

    public void HitBall()
    {
        bool haptic = FsmVariables.GlobalVariables.GetFsmBool("HapticOn").Value; // bool for if haptic is enabled or not

        if (name.Contains("bad")) // Code For Bad ball
        {
            // Spawns an invisible splat that will be used to tell the grid to disable
            GameObject splat = splats[Random.Range(0, splats.Length)]; 
            splat = Instantiate(splat, new Vector3(transform.position.x, .02f, transform.position.z), Quaternion.identity);
            splat.tag = "BadSplat";
            splat.GetComponent<Renderer>().enabled = false;
            splat.GetComponent<BoxCollider>().size = new Vector3(.5f, .5f, .5f);

            if (haptic)
            {
                MMVibrationManager.Haptic(HapticTypes.MediumImpact); // med impace haptic
            }
            iTween.ShakePosition(Camera.main.gameObject, new Vector3(.15f, .15f, .15f), .25f); // screen shake (camera, intensity, duration)

            Camera.main.GetComponent<AudioSource>().timeSamples = Camera.main.GetComponent<AudioSource>().clip.samples - 1;
            Camera.main.GetComponent<AudioSource>().pitch = Random.Range(-1f, -.6f); // get random pitch
            Camera.main.GetComponent<AudioSource>().Play();

            Destroy(this.gameObject);
        }
        else if (name.Contains("special") && hits > 1) // Code for special ball with more than 1 hit left
        {
            Debug.Log("hits: " + hits);
            if (haptic)
            {
                MMVibrationManager.Haptic(HapticTypes.LightImpact); // light impace haptic
            }
            iTween.ShakePosition(Camera.main.gameObject, new Vector3(.07f, .07f, .07f), .15f); // screen shake (camera, intensity, duration)
            hits--;
        }
        else if (name.Contains("mega"))
        {
            GameObject splat = splats[Random.Range(0, splats.Length)]; // random splat is chosen
            splat = Instantiate(splat, new Vector3(transform.position.x, .02f, transform.position.z), Quaternion.identity); // Instantiates a splat object at the ball's x and z coord

            //Color color = this.gameObject.GetComponent<Renderer>().material.GetColor("_Color"); // Gets the color of the ball's material
            Color color = FsmVariables.GlobalVariables.FindFsmColor("BallColor").Value;
            splat.GetComponent<Renderer>().material.SetColor("_Color", color); // sets splat color to color of the ball
            splat.tag = "MegaSplat";
            splat.transform.localScale = new Vector3(.5f, 1, .5f); // enlarges initial splat        

            // turns off overlay
            GameObject.Find("UI-Megaball Overlay").SetActive(false);

            Destroy(this.gameObject);
        }
        else // code for every other type of ball
        { 
            // -------- SPLAT OBJECT -------------------
            GameObject splat = splats[Random.Range(0, splats.Length)]; // random splat is chosen
            splat = Instantiate(splat, new Vector3(transform.position.x, .02f, transform.position.z), Quaternion.identity); // Instantiates a splat object at the ball's x and z coord

            Color color = this.gameObject.GetComponent<Renderer>().material.GetColor("_Color"); // Gets the color of the ball's material
            splat.GetComponent<Renderer>().material.SetColor("_Color", color); // sets splat color to color of the ball

            // -------- SPECIAL BALL CODE ------------------
            if (name.Contains("special")) // ball is a special ball
            {
                splat.transform.localScale = new Vector3(.3f, 1, .3f); // enlarges initial splat
                for (int i = 0; i < 8; i++)
                {
                    int x_change = 0;
                    int z_change = 0;

                    switch (i)
                    {
                        case 0:
                            x_change = 0;
                            z_change = 1;
                            break;
                        case 1:
                            x_change = 1;
                            z_change = 1;
                            break;
                        case 2:
                            x_change = 1;
                            z_change = 0;
                            break;
                        case 3:
                            x_change = 1;
                            z_change = -1;
                            break;
                        case 4:
                            x_change = 0;
                            z_change = -1;
                            break;
                        case 5:
                            x_change = -1;
                            z_change = -1;
                            break;
                        case 6:
                            x_change = -1;
                            z_change = 0;
                            break;
                        case 7:
                            x_change = -1;
                            z_change = 1;
                            break;
                    }

                    splat = splats[Random.Range(0, splats.Length)];
                    splat = Instantiate(splat, new Vector3(transform.position.x + x_change, .02f, transform.position.z + z_change), Quaternion.identity); // Instantiates a splat object at the ball's x and z coord
                    splat.GetComponent<MeshRenderer>().enabled = false;
                }
            }

            // --------- SPLAT PARTICLE --------------------
            GameObject splat_particle;
            splat_particle = Instantiate(splat_particles, new Vector3(transform.position.x, 1f, transform.position.z), Quaternion.identity); // Creates splat particle effect
            var main = splat_particle.gameObject.GetComponent<ParticleSystem>().main;
            main.startColor = color;

            // --------- CHANGE GRID FILL MATERIAL COLORS ------
            foreach (Material mat in gridfills)
            {
                mat.color = color;
            }

            // ---------- SPLAT UI -------------------------
            GameObject splatUI = GameObject.Find("UI-Ball Splats");
            foreach (Transform child in splatUI.transform)
            {
                child.GetComponent<RawImage>().color = color;
            }

            Animator anim = splatUI.GetComponent<Animator>();
            int random = Random.Range(0, 2);
            if (random == 0)
            {
                anim.SetBool("Splats01", true);
            }
            else if (random == 1)
            {
                anim.SetBool("Splats02", true);
            }
            else
            {
                anim.SetBool("Splats03", true);
            }

            // ------------- HAPTIC ---------------------
            if (haptic)
            {
                MMVibrationManager.Haptic(HapticTypes.MediumImpact); // light impace haptic
            }
            iTween.ShakePosition(Camera.main.gameObject, new Vector3(.15f, .15f, .15f), .25f); // screen shake (camera, intensity, duration)

            // ------------- PLAY SOUND -----------------
            Camera.main.GetComponent<AudioSource>().timeSamples = Camera.main.GetComponent<AudioSource>().clip.samples;
            Camera.main.GetComponent<AudioSource>().pitch = Random.Range(.8f, 1.2f); // get random pitch
            Camera.main.GetComponent<AudioSource>().Play();

            Destroy(this.gameObject);
            
        }
    }
}
