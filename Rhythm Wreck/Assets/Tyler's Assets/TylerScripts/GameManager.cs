using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class GameManager : MonoBehaviour
{
    public static GameManager Instance;
    public KeyCode ExitKey;
    private int _missesInARow;
    private float _delay = 4f;
    [SerializeField] private AudioSource _beatmapAudio;
    [SerializeField] private AudioSource _missAudio;
    [SerializeField] private AudioSource _gradeSAudio;
    [SerializeField] private AudioSource _gradeBAudio;
    [SerializeField] private AudioSource _gradeFAudio;
    [SerializeField] private TMPro.TextMeshPro _finalText;
    [SerializeField] private TMPro.TextMeshPro _tokensEarnedText;

    public bool Ended;
    void Start()
    {
        Instance = this;
        _beatmapAudio.PlayDelayed(_delay);

        Ended = false;
    }

    void Update()
    {
        if (_missesInARow == 400)
        {
            SceneManager.LoadScene("Start");
        }
        if (NoteActuator.Missed && NoteActuator.Combo >= 5)
            _missAudio.Play();
        if (EventManager.Paused == true || Ended == false){
            _beatmapAudio.Pause();
        }
        if (EventManager.Paused == false)
            _beatmapAudio.Play();

        if (Input.GetKeyDown(ExitKey))
        {
            SceneManager.LoadScene("GameSelect");
        }
    }

    void OnTriggerEnter2D(Collider2D col)
    {
        if (NoteActuator.Combo >= 5)
        {
            _missAudio.Play();

        }
        Destroy(col.gameObject);
        NoteActuator.Combo = 0;
        _missesInARow += 1;
    }
    public void Grade()
    {
        Ended = true;
        if (NoteActuator.TotalScore > 2500000)
        {
            _finalText.text = "AMAZING SCORE";
            _tokensEarnedText.text = "Tokens Earn: 8 Press B to Exit";
            _gradeSAudio.Play();
            FileManager.Instance.AddTokens(8);
        }
        else if (NoteActuator.TotalScore > 2000000)
        {
            _finalText.text = "GREAT SCORE";
            _tokensEarnedText.text = "Tokens Earn: 6 Press B to Exit";
            _gradeSAudio.Play();
            FileManager.Instance.AddTokens(6);
        }
        else if (NoteActuator.TotalScore > 1200000)
        {
            _finalText.text = "OK SCORE";
            _tokensEarnedText.text = "Tokens Earn: 4 Press B to Exit";
            FileManager.Instance.AddTokens(4);
            _gradeBAudio.Play();
        }
        else
        {
            _finalText.text = "BAD SCORE";
            _tokensEarnedText.text = "Tokens Earn: 2 Press B to Exit";
            _gradeFAudio.Play();
            FileManager.Instance.AddTokens(2);
        }

    }

}
