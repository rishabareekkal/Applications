using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Score : MonoBehaviour
{
    public Text ComboText;
    public Text ScoreText;
    // Start is called before the first frame update
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {
        ComboText.text = NoteActuator.Combo.ToString() + "x";
        ScoreText.text = NoteActuator.TotalScore.ToString();

    }
}
