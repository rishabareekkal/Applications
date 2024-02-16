using System.Collections;
using System.Collections.Generic;
using Unity.VisualScripting.Antlr3.Runtime;
using UnityEngine;
using UnityEngine.SceneManagement;

public class EventManager : MonoBehaviour
{
    public GameObject PausedScreen;
    static public bool Paused;

    // Start is called before the first frame update
    void Start()
    {
        PausedScreen.SetActive(false);
        Paused = false;

    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKey("escape"))
            PausedGame();
    }

    public void PausedGame()
    {
        PausedScreen.SetActive(true);
        Paused = true;
    }
    public void ResumeGame()
    {
        PausedScreen.SetActive(false);
        Paused = false;
    }

    public void RestartGame()
    {
        SceneManager.LoadScene("Tyler Wen Game Menu");
    }

    public void QuitGame()
    {
        SceneManager.LoadScene("Start");
    }
}
