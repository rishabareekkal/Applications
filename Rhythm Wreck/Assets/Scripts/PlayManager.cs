using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using System.IO;
using System.ComponentModel;

public class PlayManager : MonoBehaviour
{
    void Update()
    {
        if (SceneManager.GetActiveScene().name == "Start")
        {
            if (Input.GetKeyDown(KeyCode.Return) || Input.GetMouseButtonDown(0))
            {
                ToFileSelect();
            }
        }
        if (Input.GetKeyDown(KeyCode.Escape))
        {
            DataManager.Instance.SaveData();
            Application.Quit();
        }
    }

    public void ToFileSelect()
    {
        DataManager.Instance.SaveData();
        DataManager.Instance.LoadData();
        SceneManager.LoadScene("FileSelect");
    }

    public void ToGameSelect()
    {
        SceneManager.LoadScene("GameSelect");
    }

    public void ToSettings()
    {
        SceneManager.LoadScene("Settings");
    }

    public void QuitGame()
    {
        DataManager.Instance.SaveData();
        Application.Quit();
    }
}
