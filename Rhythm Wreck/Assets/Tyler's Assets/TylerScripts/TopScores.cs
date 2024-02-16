using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEditor.SceneManagement;
using UnityEngine.UI;


public class TopScores : MonoBehaviour
{
    [SerializeField] private Text _topScore1;
    [SerializeField] private Text _topScore2;
    [SerializeField] private Text _topScore3;
    private int[] _highScores;
    private int _topScore;



    // Start is called before the first frame update
    void Start()
    {
        _highScores = new int[]
        {
            PlayerPrefs.GetInt("HighScore1", 0),
            PlayerPrefs.GetInt("HighScore2", 0),
            PlayerPrefs.GetInt("HighScore3", 0)
        };
        _topScore = PlayerPrefs.GetInt("NewScore", 0);
        Debug.Log(_topScore);
        UpdateHighScores(_topScore);

    }

    // Update is called once per frame
    void Update()
    {
    }
    public void UpdateHighScores(int Score)
    {
        if(Score > _highScores[2])
            _highScores[2] = Score;

        for (int i = 0; i < _highScores.Length - 1; i++)
        {
            for (int j = 0; j < _highScores.Length - 1 - i; j++)
            {
                if (_highScores[j] < _highScores[j + 1])
                {
                    // Swap scores if out of order
                    int temp = _highScores[j];
                    _highScores[j] = _highScores[j + 1];
                    _highScores[j + 1] = temp;
                }
            }
        }

        PlayerPrefs.SetInt("HighScore1", _highScores[0]);
        PlayerPrefs.SetInt("HighScore2", _highScores[1]);
        PlayerPrefs.SetInt("HighScore3", _highScores[2]);
        PlayerPrefs.SetInt("NewScore", 0);
        Debug.Log("I Rans");

        _topScore1.text = _highScores[0].ToString();
        _topScore2.text = _highScores[1].ToString();
        _topScore3.text = _highScores[2].ToString();
    }
}
