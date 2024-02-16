using System.Collections;
using System.Collections.Generic;
using TMPro;
using UnityEngine;

public class TokensManager : MonoBehaviour
{
    [SerializeField] private TextMeshProUGUI _tokens;
    [SerializeField] private TextMeshProUGUI[] _highScores;

    private void Start()
    {
        _tokens.text = $"Tokens: ^{FileManager.Instance.Tokens}";
        if (_highScores != null)
        {
            for (int i = 0; i < _highScores.Length; i++)
                _highScores[i].text = $"HighScore: {FileManager.Instance.HighScores[i]}";
        }
    }
}
