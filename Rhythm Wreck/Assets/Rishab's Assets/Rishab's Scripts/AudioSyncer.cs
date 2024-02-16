using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class AudioSyncer : MonoBehaviour
{
    public float Bias;
    public float TimeStep;
    public float TimeToBeat;
    public float RestSmoothTime;

    private float _previousAudioValue;
    private float _audioValue;
    private float _timer;

    protected bool _isBeat;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        OnUpdate();
    }

    public virtual void OnUpdate()
    {
        _previousAudioValue = _audioValue;
        _audioValue = AudioSpectrum.SpectrumValue;

        if (_previousAudioValue > Bias && _audioValue <= Bias)
        {
            if (_timer > TimeStep) OnBeat();
        }
        else if (_previousAudioValue <= Bias && _audioValue > Bias)
        {
            if (_timer > TimeStep) OnBeat();
        }
        _timer += Time.deltaTime;
    }

    public virtual void OnBeat()
    {
        //Debug.Log("beat");
        _timer = 0;
        _isBeat = true;
    }
}
