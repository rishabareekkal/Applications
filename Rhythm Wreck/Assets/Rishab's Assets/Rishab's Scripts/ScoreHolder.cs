using System.Collections;
using System.Collections.Generic;
using System.Data.Common;
using TMPro;
using UnityEditor.SearchService;
using UnityEngine;
using UnityEngine.SceneManagement;

public class ScoreHolder : MonoBehaviour
{
    public static ScoreHolder Instance;
    [SerializeField] private TextMeshProUGUI _scoreText;
    [SerializeField] private AudioClip _success;
    [SerializeField] private AudioClip _failure;
    public int Score { get; set; }
    public bool ShowResults { get; set; } = false;
    private float _waitTime = 0.5f;
    private bool _done = false;
    private float _returnTime = 5f;

    void Start()
    {
        Instance = this;
        ShowResults = false;
        _waitTime = 0.5f;
        _done = false;
        _returnTime = 5f;
    }

    void Update()
    {
        if (GameMusicManager.Instance.Audio.isPlaying)
            _scoreText.text = Score.ToString();
        if (ShowResults)
        {
            _waitTime -= Time.deltaTime;
            if (_waitTime < 0 && !_done)
            {
                _scoreText.transform.localPosition = Vector3.zero;
                if (Score < 955)
                {
                    SoundManager.Instance.PlaySFX(_failure);
                    _scoreText.color = Color.grey;
                    _scoreText.text = "you lose...";
                }
                else if (Score < 1335)
                {
                    SoundManager.Instance.PlaySFX(_failure);
                    _scoreText.color = Color.magenta;
                    _scoreText.text = "eh, just ok..";
                    FileManager.Instance.AddTokens(1);
                }
                else if (Score < 1625)
                {
                    SoundManager.Instance.PlaySFX(_success);
                    _scoreText.color = Color.blue;
                    _scoreText.text = "not bad.";
                    FileManager.Instance.AddTokens(2);
                }
                else if (Score < 1815)
                {
                    SoundManager.Instance.PlaySFX(_success);
                    _scoreText.color = Color.yellow;
                    _scoreText.text = "quite good!";
                    FileManager.Instance.AddTokens(4);
                }
                else if (Score < 1910)
                {
                    SoundManager.Instance.PlaySFX(_success);
                    _scoreText.color = new Color(1f, 0.6f, 0.01f);
                    _scoreText.text = "spectacular!!";
                    FileManager.Instance.AddTokens(6);
                }
                else
                {
                    SoundManager.Instance.PlaySFX(_success);
                    _scoreText.color = Color.red;
                    _scoreText.text = "perfection!!!";
                    FileManager.Instance.AddTokens(8);
                }
                ShowResults = false;
                _done = true;
            }
        }

        if (_done)
        {
            _returnTime -= Time.deltaTime;
            if (_returnTime < 0 )
            {
                if (Score > FileManager.Instance.HighScores[3])
                    FileManager.Instance.ChangeHighScore(3, Score);
                SoundManager.Instance.UnPause();
                SceneManager.LoadScene("GameSelect");
            }
        }
    }
}
