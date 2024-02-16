using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class RhythmMatcher : MonoBehaviour
{

/*
Initializing variables 
*/

    public static RhythmMatcher Instance;
    public AudioSource Aud;
    public AudioClip Ta;
    public AudioClip Titi;
    public AudioClip TiTika;
    public AudioClip TikaTi;
    public AudioClip TikaTika;
    public AudioClip Tititi;
    private int _unlockBanana = 0;
    public GameObject Banana;
    public int[] RhythmList = new int[4];

    private float _waitTime = 3/4f;
    public int _iteration = 0;

/*
This function gets called by the play bar function to play an audio. Depending
on what number is in the rhythm list it sets the audio clip to the number's
respective counterpart. It then plays it after the source has been associated
with a clip.
*/

    void PlayNote(int[] list, int iteration)
    {
        int currentAudio = list[iteration];
        if (currentAudio == 1)
            Aud.clip = Ta;
        if (currentAudio == 2)
            Aud.clip = Titi;
        if (currentAudio == 3)
            Aud.clip = TiTika;
        if (currentAudio == 4)
            Aud.clip = TikaTi;
        if (currentAudio == 5)
            Aud.clip = TikaTika;
        if (currentAudio == 6)
            Aud.clip = Tititi;
        Aud.Play();
    }
/*
This function plays the sound when the user holds the space bar by waiting in
between audios for 0.75 seconds before playing the next. It does this four times
with an iteration variable that increases each time and stops when it reaches
four. The iteration gets reset to zero when the user removes their finger from
the space bar.
*/

    public void PlayBar()
    {
        _waitTime -= Time.deltaTime;
        if (_waitTime < 0f && _iteration < 4)
        {
            PlayNote(RhythmList, _iteration);
            _waitTime = 3/4f;
            _iteration++;
        }
    }
    public void SetBanana()
    {
        _unlockBanana = 1;
        Banana.SetActive(true);
    }
    public void GoMain()
    {
        SoundManager.Instance.UnPause();
        SceneManager.LoadScene("GameSelect");
    }
    // Start is called before the first frame update
    void Start()
    {
/*
Created an instance variable to get called by other classes. This is the rhythm
list that gets randomized each time the check button is clicked. Most other
functions depend on this one to perform their tasks correctly.
*/

        Instance = this;
        RhythmList = new int[4] { Random.Range(1, 6 + _unlockBanana), Random.Range(1, 6 + _unlockBanana), Random.Range(1, 6 + _unlockBanana), Random.Range(1, 6 + _unlockBanana) };

    }
    // Update is called once per frame
    void Update()
    {
        if (Input.GetKey(KeyCode.Space))
            PlayBar();
        if (Input.GetKeyDown(KeyCode.Space))
            _iteration = 0;
    }
}