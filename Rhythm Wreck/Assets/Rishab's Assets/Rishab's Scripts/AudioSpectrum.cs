using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class AudioSpectrum : MonoBehaviour
{
    // This was made with https://www.youtube.com/watch?v=PzVbaaxgPco.
    public static float SpectrumValue { get; private set; }
    public static float[] Spectrum { get; private set; }
    private AudioSource _source;

    void Start()
    {
        Spectrum = new float[128];
    }

    void Update()
    {
        if (PauseManager.Instance.Paused) { return; }
        if (GameMusicManager.Instance.ReadyToPlay)
            GameMusicManager.Instance.Audio.GetSpectrumData(Spectrum, 0, FFTWindow.Hamming);

        if (Spectrum != null && Spectrum.Length > 0)
        {
           SpectrumValue = Spectrum[0] * 100;
        }
    }
}
