using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class ScoreController : MonoBehaviour
{
    public static ScoreController Instance;
    private static int _scoreValue;
    private int _highScore;
    [SerializeField] private TextMeshProUGUI _scoreText;
    [SerializeField] private TextMeshProUGUI _highScoreText;

    // Start is called before the first frame update
    void Start()
    {
        Instance = this;
        _scoreValue = 0;
        _scoreText.text = "Score: 0";
        _highScore = PlayerPrefs.GetInt("highscore");
        _highScoreText.text = $"High Score:\n{_highScore}";
    }

    // Update is called once per frame
    public void IncreaseScore()
    {
        _scoreValue += 20;
        _scoreText.text = $"Score:\n{_scoreValue}";
        if (_scoreValue > _highScore) {
            _highScore = _scoreValue;
            PlayerPrefs.SetInt("highscore", _highScore);
            _highScoreText.text = $"High Score:\n{_highScore}";
        }
    }
}
