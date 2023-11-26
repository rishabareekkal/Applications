using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class MainMenu : MonoBehaviour
{
    void Update()
    {
        if (Input.GetKey("escape"))
        {
            Application.Quit();
        }
    }

    public void PlayGame()
    {
        SceneManager.LoadScene("playscene");
    }

    public void ToSettingsMenu()
    {
        SceneManager.LoadScene("settingsscene");
    }

    public void ToMainMenu()
    {
        SceneManager.LoadScene("mainmenuscene");
    }

    public void QuitGame()
    {
        Application.Quit();
    }
}
