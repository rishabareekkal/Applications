using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class BGMSlider : MonoBehaviour
{
    [SerializeField] private Slider _bgmSlider;
    [SerializeField] private TextMeshProUGUI _bgmSliderText;

    void Start()
    {
        SoundManager.Instance.ChangeBGMVolume(_bgmSlider.value);
        _bgmSlider.onValueChanged.AddListener((bgmVal) => {
            _bgmSliderText.text = bgmVal.ToString("0.00");
            SoundManager.Instance.ChangeBGMVolume(bgmVal);
        });
    }
}
