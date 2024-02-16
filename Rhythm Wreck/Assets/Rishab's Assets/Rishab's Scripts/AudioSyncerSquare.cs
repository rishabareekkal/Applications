using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using UnityEngine;

public class AudioSyncerSquare : AudioSyncer
{
    private GameObject[] squares = new GameObject[128];

    private void Start()
    {
        for (int i = 0; i < squares.Length; i++)
        {
            squares[i] = transform.GetChild(i).gameObject;
            squares[i].transform.localPosition = new Vector3((float)i / 20f, 0f, 0f);
        }
    }

    public override void OnUpdate()
    {
        base.OnUpdate();
        for (int i = 0; i < AudioSpectrum.Spectrum.Length; i++)
        {
            squares[i].transform.localScale = new Vector3 (0.05f, AudioSpectrum.Spectrum[i] * 5, 1.0f);
        }
    }

    public override void OnBeat()
    {
        base.OnBeat();
    }
}
