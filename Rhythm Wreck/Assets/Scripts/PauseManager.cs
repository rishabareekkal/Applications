using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class PauseManager : MonoBehaviour
{
    public static PauseManager Instance;
    [SerializeField] private GameObject _pauseMenu;
    [SerializeField] private GameObject _pauseButton;
    [SerializeField] private Toggle _guidersToggle;
    public bool Paused { get; private set; } = false;

    void Start()
    {
        Instance = this;
        _pauseMenu.SetActive(false);
        _pauseButton.SetActive(true);
    }

    public void PauseGame()
    {
        _pauseMenu.SetActive(true);
       
        _pauseButton.SetActive(false);
        Paused = true;
        Time.timeScale = 0f;
    }

    public void ResumeGame()
    {
        Debug.Log("mrtyui");
        _pauseMenu.SetActive(false);
        _pauseButton.SetActive(true);
        Paused = false;
        Time.timeScale = 1f;
    }

    public void ToggleGuiders()
    {

        PlayerController.Instance.Guiders = _guidersToggle.isOn;
    }

    public void ToRestart()
    {
        _pauseMenu.SetActive(false);
        _pauseButton.SetActive(true);
        Paused = false;
        Time.timeScale = 1f;
        SceneManager.LoadScene(SceneManager.GetActiveScene().name);
    }

    public void ToGameSelect()
    {
        _pauseMenu.SetActive(false);
        _pauseButton.SetActive(true);
        Paused = false;
        Time.timeScale = 1f;
        SceneManager.LoadScene("GameSelect");
    }

    public void ToFileSelect()
    {
        _pauseMenu.SetActive(false);
        _pauseButton.SetActive(true);
        Paused = false;
        Time.timeScale = 1f;
        SceneManager.LoadScene("FileSelect");
    }

    public void QuitGame()
    {
        DataManager.Instance.SaveData();
        Application.Quit();
    }
}
