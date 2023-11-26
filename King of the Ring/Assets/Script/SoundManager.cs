using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SoundManager : MonoBehaviour
{
    public static SoundManager Instance;

    [SerializeField] private AudioSource _bgmSource, _sfxSource;
    [SerializeField] private AudioClip _clip;

    void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
            DontDestroyOnLoad(gameObject);
        }
        else
        {
            Destroy(gameObject);
        }
        _bgmSource.loop = true;
    }

    void Update()
    {
        if (Input.GetMouseButtonDown(0))
        {
            _sfxSource.PlayOneShot(_clip);
        }
    }

    public void ChangeMasterVolume(float value)
    {
        AudioListener.volume = value;
    }

    public void ToggleSFX()
    {
        _sfxSource.mute = !_sfxSource.mute;
    }

    public void ToggleBGM()
    {
        _bgmSource.mute = !_bgmSource.mute;
    }
}
