using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class EndScreen : MonoBehaviour
{
    public static EndScreen Instance;
    public TextMeshProUGUI Score;
    public TextMeshProUGUI HighScores;
    public TextMeshProUGUI TokensEarned;
    private int[] _highScores = new int[3];
    private int _tokensEarned;
    public void Setup()
    {
        Debug.Log("");

        _tokensEarned = RustinScore.GetScore() / 10;
        if (RustinScore.GetPreviousScores().Length == 1)
            _highScores = new int [1] { RustinScore.GetPreviousScores()[0] };
        else if (RustinScore.GetPreviousScores().Length == 1)
            _highScores = new int [2] { RustinScore.GetPreviousScores()[0], RustinScore.GetPreviousScores()[1] };
        else
            _highScores = new int [3] { RustinScore.GetPreviousScores()[0], RustinScore.GetPreviousScores()[1], RustinScore.GetPreviousScores()[2] };

        Score.text = $"Score: {RustinScore.GetScore()}";
        HighScores.text = $"High Scores: {string.Join(", ", _highScores)}";
        TokensEarned.text = $"Tokens Earned: {_tokensEarned}";
    }
    // Start is called before the first frame update

    void Start()
    {
        if (Instance == null)
            Instance = this;
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
