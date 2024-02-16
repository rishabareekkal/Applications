using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UIElements;

public class TutorialManager : MonoBehaviour
{
    [SerializeField] private GameObject[] _textLines;
    private int _currentLine = 0;
    private float _waitTime = 6f;

    private void Start()
    {
        _currentLine = 0;
        _waitTime = 6f;
    }

    void Update()
    {
        if (PauseManager.Instance.Paused) { return; }
        for (int i = 0; i < _textLines.Length; i++)
        {
            _textLines[i].SetActive(true);
            if (i != _currentLine)
                _textLines[i].SetActive(false);

        }
        if (_currentLine == 0)
        {
            if (Input.GetKeyDown(KeyCode.DownArrow)) _currentLine++;
        } else if (_currentLine == 1)
        {
                if (Input.GetKeyDown(KeyCode.UpArrow)) _currentLine++;
        } else if ( _currentLine == 2)
        {
            _waitTime -= Time.deltaTime;
            if (_waitTime < 0f)
            {
                PlayerController.Instance.InTutorial = false;
                PlayerController.Instance.LowerAttackable = false;
                PlayerController.Instance.UpperAttackable = false;
                GameMusicManager.Instance.ReadyToPlay = true;
                _currentLine++;
            }
        }
    }
}
