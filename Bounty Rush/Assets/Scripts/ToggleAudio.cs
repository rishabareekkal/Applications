using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ToggleAudio : MonoBehaviour
{
    [SerializeField] private bool _toggleBGM, _toggleSFX;

    public void Toggle()
    {
        if (_toggleSFX) SoundManager.Instance.ToggleSFX();
        if (_toggleBGM) SoundManager.Instance.ToggleBGM();
    }
}
