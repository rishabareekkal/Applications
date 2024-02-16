using System.Collections;
using System.Collections.Generic;
using System.IO.Enumeration;
using TMPro;
using UnityEngine;
using UnityEngine.Rendering;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class FileSelect : MonoBehaviour
{
    [SerializeField] private TMP_Text _titleText;
    [SerializeField] private GameObject _settingsButton, _fileButton1, _fileButton2, _fileButton3, _fileButton4;
    [SerializeField] private TextMeshProUGUI _fileName1, _fileName2, _fileName3, _fileName4;
    [SerializeField] private TMP_InputField _inputName;
    [SerializeField] private GameObject _inputField;

    void Start()
    {
        _inputField.SetActive(false);
        _fileName1.text = DataManager.Instance.Data.FileName1;
        _fileName2.text = DataManager.Instance.Data.FileName2;
        _fileName3.text = DataManager.Instance.Data.FileName3;
        _fileName4.text = DataManager.Instance.Data.FileName4;
    }

    public void SetFileName(int fileNumber)
    {
        _titleText.text = "Enter A File Name";
        _settingsButton.SetActive(false); _fileButton1.SetActive(false); _fileButton2.SetActive(false); _fileButton3.SetActive(false); _fileButton4.SetActive(false);
        _inputField.SetActive(true);
        _inputName.onEndEdit.AddListener((TextVal) =>
        {
            if (TextVal != "New Game" && !string.IsNullOrWhiteSpace(TextVal))
            {
                if (fileNumber == 1)
                {
                    _fileName1.text = TextVal;
                    DataManager.Instance.Data.FileName1 = _fileName1.text;
                }
                if (fileNumber == 2)
                {
                    _fileName2.text = TextVal;
                    DataManager.Instance.Data.FileName2 = _fileName2.text;
                }
                if (fileNumber == 3)
                {
                    _fileName3.text = TextVal;
                    DataManager.Instance.Data.FileName3 = _fileName3.text;
                }
                if (fileNumber == 4)
                {
                    _fileName4.text = TextVal;
                    DataManager.Instance.Data.FileName4 = _fileName4.text;
                }
                _inputName.text = "";
                _inputField.SetActive(false);
                // _settingsButton.SetActive(true); _fileButton1.SetActive(true); _fileButton2.SetActive(true); _fileButton3.SetActive(true); _fileButton4.SetActive(true);
                _titleText.text = "Select A File";
                DataManager.Instance.SaveData();
                _inputName.onEndEdit.RemoveAllListeners();
                SceneManager.LoadScene("GameSelect");
            }
            else
            {
                Debug.LogError("A proper name has not been set for the file.");
            }
        });
    }

    public void FirstFileSelect()
    {
        FileManager.Instance.SetCurrentFile(0);
        if (string.IsNullOrWhiteSpace(DataManager.Instance.Data.FileName1) || DataManager.Instance.Data.FileName1 == "New Game")
            SetFileName(1);
        else
            SceneManager.LoadScene("GameSelect");
    }

    public void SecondFileSelect()
    {
        FileManager.Instance.SetCurrentFile(1);
        if (string.IsNullOrWhiteSpace(DataManager.Instance.Data.FileName2) || DataManager.Instance.Data.FileName2 == "New Game")
            SetFileName(2);
        else
            SceneManager.LoadScene("GameSelect");
    }

    public void ThirdFileSelect()
    {
        FileManager.Instance.SetCurrentFile(2);
        if (string.IsNullOrWhiteSpace(DataManager.Instance.Data.FileName3) || DataManager.Instance.Data.FileName3 == "New Game")
            SetFileName(3);
        else
            SceneManager.LoadScene("GameSelect");
    }

    public void FourthFileSelect()
    {
        FileManager.Instance.SetCurrentFile(3);
        if (string.IsNullOrWhiteSpace(DataManager.Instance.Data.FileName4) || DataManager.Instance.Data.FileName4 == "New Game")
            SetFileName(4);
        else
            SceneManager.LoadScene("GameSelect");
    }
}
