using System.Collections;
using System.Collections.Generic;
using TMPro;
using Unity.VisualScripting;
using UnityEngine;
using UnityEngine.UI;

public class CollectiblesManager : MonoBehaviour
{
    [SerializeField] private SpriteRenderer[] _collectibles;
    [SerializeField] private GameObject[] _names;
    [SerializeField] private GameObject[] _buyButtons;

    // Start is called before the first frame update
    void Start()
    {
        int i = 0;
        foreach (KeyValuePair<string, bool> keyValuePair in FileManager.Instance.Collectibles)
        {
            if (keyValuePair.Value)
            {
                _collectibles[i].color = Color.white;
                _buyButtons[i].SetActive(false);
                _names[i].SetActive(true);
            }
            i++;
        }
    }

    public void BuyCococup()
    {
        if (FileManager.Instance.Tokens >= 20)
        {
            FileManager.Instance.RemoveTokens(20);
            FileManager.Instance.ChangeCollectibles("Cococup");
            _collectibles[0].color = Color.white;
            _buyButtons[0].SetActive(false);
            _names[0].SetActive(true);
        }
    }
    public void BuyShrimpHat()
    {
        if (FileManager.Instance.Tokens >= 15)
        {
            FileManager.Instance.RemoveTokens(15);
            FileManager.Instance.ChangeCollectibles("Shrimp Hat");
            _collectibles[1].color = Color.white;
            _buyButtons[1].SetActive(false);
            _names[1].SetActive(true);
        }
    }
    public void BuyPalmTree()
    {
        if (FileManager.Instance.Tokens >= 30)
        {
            FileManager.Instance.RemoveTokens(30);
            FileManager.Instance.ChangeCollectibles("Palm Tree");
            _collectibles[2].color = Color.white;
            _buyButtons[2].SetActive(false);
            _names[2].SetActive(true);
        }
    }
    public void BuyBanana()
    {
        if (FileManager.Instance.Tokens >= 25)
        {
            RhythmMatcher.Instance.SetBanana();
            FileManager.Instance.RemoveTokens(25);
            FileManager.Instance.ChangeCollectibles("banana");
            _collectibles[3].color = Color.white;
            _buyButtons[3].SetActive(false);
            _names[3].SetActive(true);
        }
    }
    public void BuyFlowers()
    {
        if (FileManager.Instance.Tokens >= 10)
        {
            FileManager.Instance.RemoveTokens(10);
            FileManager.Instance.ChangeCollectibles("Flowers");
            _collectibles[4].color = Color.white;
            _buyButtons[4].SetActive(false);
            _names[4].SetActive(true);
        }
    }
    public void BuySeaShell()
    {
        if (FileManager.Instance.Tokens >= 40)
        {
            FileManager.Instance.RemoveTokens(40);
            FileManager.Instance.ChangeCollectibles("Sea Shell");
            _collectibles[5].color = Color.white;
            _buyButtons[5].SetActive(false);
            _names[5].SetActive(true);
        }
    }
}
