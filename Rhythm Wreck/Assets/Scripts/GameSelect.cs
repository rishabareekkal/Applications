using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class GameSelect : MonoBehaviour
{
    public void ToJacksGame()
    {
        SceneManager.LoadScene("Jack Song Select");
    }

    public void ToTylersGame()
    {
        SceneManager.LoadScene("Tyler Wen Game Menu");
    }

    public void ToRustinsGame()
    {
        SceneManager.LoadScene("Rustin's game");
    }

    public void ToRishabsGame()
    {
        SceneManager.LoadScene("Shrimp Swiper");
    }

    public void ToUselessShop()
    {
        SceneManager.LoadScene("Useless Shop");
    }
}
