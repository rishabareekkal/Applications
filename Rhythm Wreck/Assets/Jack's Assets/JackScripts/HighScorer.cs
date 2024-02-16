using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UIElements;
using TMPro;

public class HighScorer : MonoBehaviour

{
    public string BestBlocker = "?????";
    private int[] _files = new int[4] { 0, 1, 2, 3 };
    private int[] _blockerScores = new int[4] {
        DataManager.Instance.Data.HighScores[0, 0], DataManager.Instance.Data.HighScores[1, 0],
        DataManager.Instance.Data.HighScores[2, 0], DataManager.Instance.Data.HighScores[3, 0] };
    [SerializeField] private TextMeshPro BestBlockerText;

    void Start()
    {
        for (int i = 0; i < _blockerScores.Length - 1; i++)
        {
            if (_blockerScores[0] < _blockerScores[i + 1])
            {
                int tempBlock = _blockerScores[i + 1];
                _blockerScores[i + 1] = _blockerScores[0];
                _blockerScores[0] = tempBlock;
                int tempFiles = _files[i + 1];
                _files[i + 1] = _files[0];
                _files[0] = tempFiles;
            }
        }


        if (_files[0] == 0)
            BestBlocker = DataManager.Instance.Data.FileName1;
        else if (_files[0] == 1)
            BestBlocker = DataManager.Instance.Data.FileName2;
        else if (_files[0] == 2)
            BestBlocker = DataManager.Instance.Data.FileName3;
        else if (_files[0] == 3)
            BestBlocker = DataManager.Instance.Data.FileName4;
    }
    private void Update()
    {
        BestBlockerText.text = BestBlocker;
    }
}
