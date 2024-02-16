using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class NoteButtons : MonoBehaviour
{
    /*
    Initializing variables. The value variable is encapsulated to ensure it only
    changes when the player interacts with an onject that it depends on.
    */

    private static int _value;
    private int[] _inputList = new int[4];
    private string[] _fruit = new string[5] { "GRAPE", "KIWI", "PINEAPPLE", "COCONUT", "WATERMELON" };
    public AudioSource Aud;
    public AudioClip Correct;
    public AudioClip Incorrect;

/*
These functions set the cursor value to their respective fruits. They later get
added into the input list in the next funcitons
*/
    public virtual void SetValueToTa()
    {
        _value = 1;
    }
    public virtual void SetValueToTiti()
    {
        _value = 2;
    }
    public virtual void SetValueToTiTika()
    {
        _value = 3;
    }
    public virtual void SetValueToTikaTi()
    {
        _value = 4;
    }
    public virtual void SetValueToTikaTika()
    {
        _value = 5;
    }
    public virtual void SetValueToTititi()
    {
        _value = 6;
    }
/*
These functions set values to their respective indexes of the input list based
on the user input given in the previous funcitons.
*/

    public virtual void SetIndexValueOne()
    {
        _inputList[0] = _value;

    }
    public virtual void SetIndexValueTwo()
    {
        _inputList[1] = _value;
    }
    public virtual void SetIndexValueThree()
    {
        _inputList[2] = _value;
    }
    public virtual void SetIndexValueFour()
    {
        _inputList[3] = _value;
    }
    public static int GetValue()
    {
        return _value;
    }
/*
This function calls the CheckList function to see what value it returns. If the
value is true it plays the correct audio and if not it plays the incorrect audio.
After that it re-randomizes the rhythm list and resets the input list to its
default state regardless of if the player gets the answer correct.
*/
    public void CheckValues()
    {
        if (CheckList(RhythmMatcher.Instance.RhythmList, 0))
        {
            Aud.clip = Correct;
            RustinScore.AddScore();
        }
        else
        {
            Aud.clip = Incorrect;
            RustinScore.SubScore();
        }

        Aud.Play();
        RustinScore.SetRounds(RustinScore.GetRounds() + 1);
        RustinScore.ResetTimes();
        RhythmMatcher.Instance.RhythmList = new int[4] { Random.Range(1, 6), Random.Range(1, 6), Random.Range(1, 6), Random.Range(1, 6) };
        _inputList = new int[4];
    }
    public void PlayAgain()
    {
        RustinScore.SetRounds(0);
        RustinScore.SetScore();
        RustinScore.ResetTimes();
        ImageCursor.Instance.Reset();
        RhythmMatcher.Instance.RhythmList = new int[4] { Random.Range(1, 6), Random.Range(1, 6), Random.Range(1, 6), Random.Range(1, 6) };
        _inputList = new int[4];

    }
    /*
    This function recursively iterates through the input and rhythm lists to check 
    if all values are equal. If they are, it returns the value true.hu
    */
    public bool CheckList(int[] list, int num)
    {
        if (list[num] == _inputList[num])
        {
            if (num < 3)
                return CheckList(list, num + 1);
            return true;
        }
        return false;
    }

    void Start()
    {

    }
    // Update is called once per frame
    void Update()
    {

    }
}