using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;

public class RustinScore : MonoBehaviour
{
    private static int _rounds = 0;

    public TextMeshProUGUI Score;

    private static int _scoreNum = 0;
    private static int _timesReplayed = 0;

    private static int[] _previousScores = new int[1];

    public GameObject EndScreenObject;
    // Start is called before the first frame update
    public static void SubScore()
    {
        _scoreNum -= 10;
    }
    public static void AddScore()
    {
        _scoreNum += 10;
    }
    public static void ResetTimes()
    {
        _timesReplayed = 0;
    }
    public static int GetScore()
    {
        return _scoreNum;
    }
    public static void SetScore()
    {
        _scoreNum = 0;
    }
    public static int[] GetPreviousScores()
    {
        return _previousScores;
    }
    public void EndGame()
    {
        AddScore(_scoreNum);
        ScoreSort(_previousScores);
        EndScreenObject.SetActive(true);
        EndScreen.Instance.Setup();
        _scoreNum = 0;
    }
    public static void SetRounds(int round)
    {
        _rounds = round;
    }
    public static int GetRounds()
    {
        return _rounds;
    }
    private void ScoreSort(int[] list)
    {
        for (int j = list.Length - 1; j > 0; j--)
        {
            bool sorted = true;
            for (int i = 0; i < j; i++)
            {
                int temp = 0;
                if (list[i] > list[i + 1])
                {
                    temp = list[i + 1];
                    list[i + 1] = list[i];
                    list[i] = temp;
                    sorted = false;
                }
            }
            if (sorted)
                break;
        }

    }
    public static void AddScore(int n)
    {
        int[] newList = new int[_previousScores.Length + 1];
        for (int i = 0; i < _previousScores.Length; i += 1)
        {
            newList[i] = _previousScores[i];
        }
        newList[newList.Length - 1] = n;
        _previousScores = newList;
    }
    void Start()
    {
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Space))
        {
            _timesReplayed++;
            if (_timesReplayed > 1)
                _scoreNum -= 5;
        }
        Score.text = $"{_scoreNum}";

        if (_rounds >= 10)
        {
            EndGame();
            Debug.Log("End");
        }
    }
}
//FileManager.Instance.AddTokens(8);
//FileManager.Instance.ChangeHighScore(3, Score);
//FileManager.Instance.Change(3, Score);
