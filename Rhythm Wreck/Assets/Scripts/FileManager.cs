using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class FileManager : MonoBehaviour
{
    public static FileManager Instance;
    public int CurrentFile { get; private set; } = -1;
    public int Tokens { get; set; } = 0;
    public int[] HighScores { get; set; } = new int[4];
    public Dictionary<string, bool> Collectibles { get; set; } = new();

    void Start()
    {
        if (Instance == null)
        {
            Instance = this;
            DontDestroyOnLoad(gameObject);
        }
        else
            Destroy(gameObject);
        SceneManager.sceneLoaded += OnSceneLoaded;
    }

    void OnSceneLoaded(Scene scene, LoadSceneMode mode)
    {
        if (scene.name == "FileSelect")
        {
            CurrentFile = -1;
            Tokens = 0;
            for (int i = 0; i < HighScores.Length; i++)
                HighScores[i] = 0;
        }
        // -1 means that the game is in an undecided file state.
    }

    public void SetCurrentFile(int fileNumber)
    {
        CurrentFile = fileNumber;
        Tokens = DataManager.Instance.Data.Tokens[fileNumber];
        Collectibles = DataManager.Instance.Data.AllCollectibles[fileNumber];
        for (int i = 0; i < 4; i++)
            HighScores[i] = DataManager.Instance.Data.HighScores[fileNumber, i];
    }

    public void ChangeCollectibles(string collectibleName)
    {
        Collectibles[collectibleName] = true;
        DataManager.Instance.Data.AllCollectibles[CurrentFile][collectibleName] = true;
        DataManager.Instance.SaveData();
    }

    public void ChangeHighScore(int gameNumber, int newScore)
    {
        HighScores[gameNumber] = newScore;
        DataManager.Instance.Data.HighScores[CurrentFile, gameNumber] = newScore;
        DataManager.Instance.SaveData();
    }

    public void AddTokens(int amount)
    {
        Tokens += amount;
        DataManager.Instance.Data.Tokens[CurrentFile] = Tokens;
        DataManager.Instance.SaveData();
    }

    public void RemoveTokens(int amount)
    {
        Tokens -= amount;
        DataManager.Instance.Data.Tokens[CurrentFile] = Tokens;
        DataManager.Instance.SaveData();
    }
}
