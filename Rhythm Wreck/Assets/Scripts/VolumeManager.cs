using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class NewBehaviourScript : MonoBehaviour
{
    [SerializeField] private Slider _bgmSlider, _sfxSlider;
    [SerializeField] private TextMeshProUGUI _bgmSliderText, _sfxSliderText;
    [SerializeField] private Toggle _toggleBGM, _toggleSFX;

    void OnEnable()
    {
        _bgmSlider.value = DataManager.Instance.Data.BGMSliderVal;
        _sfxSlider.value = DataManager.Instance.Data.SFXSliderVal;
        _bgmSliderText.text = _bgmSlider.value.ToString("0.00");
        _sfxSliderText.text = _sfxSlider.value.ToString("0.00");
        _toggleBGM.isOn = DataManager.Instance.Data.BGMToggle;
        _toggleSFX.isOn = DataManager.Instance.Data.SFXToggle;
    }

    void Start()
    {
        SoundManager.Instance.ChangeBGMVolume(_bgmSlider.value);
        _bgmSlider.onValueChanged.AddListener((bgmVal) =>
        {
            _bgmSliderText.text = bgmVal.ToString("0.00");
            SoundManager.Instance.ChangeBGMVolume(bgmVal);
            DataManager.Instance.Data.BGMSliderVal = bgmVal;
        });

        SoundManager.Instance.ChangeSFXVolume(_sfxSlider.value);
        _sfxSlider.onValueChanged.AddListener((sfxVal) =>
        {
            _sfxSliderText.text = sfxVal.ToString("0.00");
            SoundManager.Instance.ChangeSFXVolume(sfxVal);
            DataManager.Instance.Data.SFXSliderVal = sfxVal;
        });
    }

    public void ToggleBGM()
    {
        SoundManager.Instance.ToggleBGM(_toggleBGM.isOn);
        DataManager.Instance.Data.BGMToggle = _toggleBGM.isOn;
    }

    public void ToggleSFX()
    {
        SoundManager.Instance.ToggleSFX(_toggleSFX.isOn);
        DataManager.Instance.Data.SFXToggle = _toggleSFX.isOn;
    }
}
