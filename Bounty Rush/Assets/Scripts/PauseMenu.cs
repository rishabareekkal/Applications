using System.Collections;
using System.Collections.Generic;
using System.Linq;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class PauseMenu : MonoBehaviour
{
    public static PauseMenu Instance;
    [SerializeField] private GameObject _pauseMenu;
    [SerializeField] private GameObject _pauseButton;
    [SerializeField] private GameObject _player;
    [SerializeField] private GameObject _enemy;

    void Start()
    {
        _pauseMenu.SetActive(false);
    }

    public void PauseGame()
    {
        _pauseMenu.SetActive(true);
        _pauseButton.SetActive(false);
        _player.SetActive(false);
        _enemy.SetActive(false);
        Time.timeScale = 0f;
    }

    public void ResumeGame()
    {
        _pauseMenu.SetActive(false);
        _pauseButton.SetActive(true);
        _player.SetActive(true);
        _enemy.SetActive(true);
        Time.timeScale = 1f;
    }

    public void ToRestart()
    {
        _pauseMenu.SetActive(false);
        _pauseButton.SetActive(true);
        Time.timeScale = 1f;
        SceneManager.LoadScene("playscene");
    }

    public void ToMainMenu()
    {
        _pauseMenu.SetActive(false);
        _pauseButton.SetActive(true);
        Time.timeScale = 1f;
        SceneManager.LoadScene("mainmenuscene");
    }

    public void QuitGame()
    {
        Application.Quit();
    }
}
