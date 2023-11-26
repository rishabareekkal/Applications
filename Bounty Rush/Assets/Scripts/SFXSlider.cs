using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class SFXSlider : MonoBehaviour
{
    [SerializeField] private Slider _sfxSlider;
    [SerializeField] private TextMeshProUGUI _sfxSliderText;

    void Start()
    {
        SoundManager.Instance.ChangeSFXVolume(_sfxSlider.value);
        _sfxSlider.onValueChanged.AddListener((sfxVal) => {
            _sfxSliderText.text = sfxVal.ToString("0.00");
            SoundManager.Instance.ChangeSFXVolume(sfxVal);
        });
    }
}
