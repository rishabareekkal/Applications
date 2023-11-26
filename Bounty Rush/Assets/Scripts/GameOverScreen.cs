using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using static UnityEditor.Experimental.GraphView.GraphView;

public class GameOverScreen : MonoBehaviour
{
    public static GameOverScreen Instance;
    [SerializeField] private GameObject _gameOverMenu;
    [SerializeField] private GameObject _player;
    [SerializeField] private GameObject _enemy;

    void Start()
    {
        Instance = this;
        _gameOverMenu.SetActive(false);
    }

    public void GameOver()
    {
        _gameOverMenu.SetActive(true);
        _player.SetActive(false);
        _enemy.SetActive(false);
        Time.timeScale = 0f;
    }

    public void ToRestart()
    {
        _gameOverMenu.SetActive(false);
        Time.timeScale = 1f;
        SceneManager.LoadScene("playscene");
    }

    public void ToMeinMenu()
    {
        _gameOverMenu.SetActive(false);
        Time.timeScale = 1f;
        SceneManager.LoadScene("mainmenuscene");
    }

    public void QuitGame()
    {
        Application.Quit();
    }
}
