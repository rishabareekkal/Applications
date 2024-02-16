using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEditor.SceneManagement;

public class NoteActuator : MonoBehaviour
{
    public static NoteActuator Instance;
    public KeyCode Key;
    public KeyCode Exit;
    static public int Combo;
    private int _score;
    static public int TotalScore;
    bool active = false;
    static public bool Missed;
    static public int MaxCombo;
    static public int[] TopScores = new int[3];

    static public int HighScore1;
    static public int HighScore2;
    static public int HighScore3;

    private TopScores TopScoreManager;
    public int NewScore;


    GameObject note;
    Color old;

    
    // Start is called before the first frame update
    void Start()
    {
        Instance = this;
        old = GetComponent<SpriteRenderer>().color;
        _score = 0;
        TotalScore = 0;
        MaxCombo = 0;
        TopScoreManager = FindObjectOfType<TopScores>();


    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(Key))
        {
            GetComponent<SpriteRenderer>().color = new Color(0,0,0);
            if(active)
            {
                Destroy(note);
                Combo += 1;
                _score = 197 * Combo;
                TotalScore = TotalScore + _score;
            }
            else
            {
                Missed = true;
                Combo = 0;
            }

                
        }
        if (Input.GetKeyUp(Key))
            GetComponent<SpriteRenderer>().color = old;
        PlayerPrefs.SetInt("NewScore",TotalScore);

       
    }

    void OnTriggerEnter2D(Collider2D col)
    {
        if(col.gameObject.tag == "LastNote"){
            GameManager.Instance.Grade();
        }

        if (col.gameObject.tag == "Note"){
            active = true;
            note = col.gameObject;

        }
    }
    private void OnTriggerExit2D(Collider2D col)
    {
        active = false; 
    }

    //public void SetNewScore()
    //{
      // PlayerPrefs.SetInt("NewScore",TotalScore);
    //}
}
