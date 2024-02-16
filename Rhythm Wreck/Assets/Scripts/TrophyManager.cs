using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UIElements;

public class TrophyManager : MonoBehaviour
{
    private int[] _files = new int[4] { 0, 1, 2, 3 };
    private int[] _shrimpScores = new int[4] {
        DataManager.Instance.Data.HighScores[0, 3], DataManager.Instance.Data.HighScores[1, 3],
        DataManager.Instance.Data.HighScores[2, 3], DataManager.Instance.Data.HighScores[3, 3] };
    [SerializeField] private GameObject[] _shrimpTrophies;

    void Start()
    {
        for (int i = 0; i < _shrimpScores.Length - 1; i++)
        {
            if (_shrimpScores[i] > _shrimpScores[i + 1])
            {
                int tempShrimp = _shrimpScores[i];
                _shrimpScores[i] = _shrimpScores[i + 1];
                _shrimpScores[i + 1] = tempShrimp;
                int tempFiles = _files[i];
                _files[i] = _files[i + 1];
                _files[i + 1] = tempFiles;
            }
        }

        for (int j = 0; j < _shrimpScores.Length - 1; j++)
        {
            if (_shrimpScores[j] != _shrimpScores[3])
            {
                _shrimpTrophies[_files[j]].SetActive(false);
            }
        }
    }
}
