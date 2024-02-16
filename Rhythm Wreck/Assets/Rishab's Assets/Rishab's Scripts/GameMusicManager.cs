using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GameMusicManager : MonoBehaviour
{
    public static GameMusicManager Instance;
    private AudioSource[] _allSources;
    public AudioSource Audio { get; private set; }
    private AudioSource _tutorialMusic;
    private int _currentTimeStamp = 0;
    private float _timeFromPrevStamp = 0f;
    private bool _canSpawnInRow = false;
    private int _spawnLocation = 0;
    readonly private float _minimumTimeDiff = 0.3f;
    public bool ReadyToPlay { get; set; }

    private List<float> _timeStamps = new()
    {
        3.605329f, 3.66932f, 3.882653f, 4.074648f, 5.034648f, 5.226644f, 5.397324f, 5.58932f, 6.015986f, 6.378662f,
        6.741315f, 7.146644f, 7.50932f, 7.850657f, 8.234649f, 8.639977f, 9.237325f, 9.557324f, 10.13331f, 10.79465f,
        11.26399f, 11.62664f, 12.22399f, 13.16265f, 13.52533f, 13.952f, 14.33599f, 14.69866f, 15.67998f, 15.82932f,
        16.04265f, 16.21331f, 17.21599f, 17.36533f, 17.53599f, 17.70664f, 18.09066f, 18.47465f, 18.81599f, 19.24265f,
        19.62664f, 19.98932f, 20.30932f, 20.73599f, 21.31199f, 21.71733f, 22.25066f, 22.91199f, 23.38132f, 23.76533f,
        24.34131f, 25.25866f, 25.85599f, 26.26131f, 26.64533f, 27.45599f, 28.28798f, 28.71465f, 29.11998f, 29.50399f,
        29.88798f, 30.05866f, 30.25066f, 30.46399f, 30.82664f, 31.38132f, 31.74399f, 32.14932f, 32.53331f, 32.89598f,
        33.08798f, 33.27998f, 33.472f, 33.83465f, 34.49599f, 34.83733f, 35.22131f, 35.58399f, 35.98932f, 36.18132f,
        36.37331f, 36.56533f, 37.39732f, 38.20798f, 38.592f, 38.80533f, 39.42399f, 39.97866f, 40.17066f, 40.36265f,
        40.53331f, 41.51465f, 41.70664f, 41.87732f, 42.09066f, 42.45331f, 42.81599f, 43.24265f, 43.56265f, 43.96798f,
        44.33066f, 44.71465f, 45.07732f, 45.67465f, 46.05866f, 46.57066f, 47.14664f, 47.74399f, 48.12798f, 48.72533f,
        49.62132f, 50.00533f, 50.38932f, 50.752f, 51.13599f, 52.18132f, 52.33066f, 52.52265f, 52.71465f, 53.58932f,
        53.75998f, 53.99465f, 54.16533f, 54.57066f, 54.95465f, 55.29599f, 55.70132f, 56.08533f, 56.46932f, 56.81066f,
        57.21599f, 57.74932f, 58.17599f, 58.68798f, 59.28533f, 59.88265f, 60.24533f, 60.82132f, 61.73866f, 62.33599f,
        62.71998f, 63.16798f, 63.87199f, 64.85331f, 65.23733f, 65.57866f, 65.96265f, 66.32533f, 66.51733f, 66.70932f,
        66.90131f, 67.26399f, 67.86131f, 68.20265f, 68.60798f, 69.01331f, 69.37598f, 69.56799f, 69.78132f, 69.97331f,
        70.33598f, 70.97598f, 71.29599f, 71.65866f, 72.02132f, 72.40533f, 72.57599f, 72.78932f, 72.95998f, 73.34399f,
        73.79199f, 74.66664f, 75.05066f, 75.24265f, 75.96798f, 76.41599f, 76.58665f, 76.75732f, 76.97066f, 77.97331f,
        78.14399f, 78.33598f, 78.50665f, 78.89066f, 79.29599f, 79.65866f, 80.02132f, 80.40533f, 80.78932f, 81.17331f, 81.53599f
    };

    // Start is called before the first frame update
    void Start()
    {
        Instance = this;
        _allSources = GetComponents<AudioSource>();
        Audio = _allSources[0];
        _tutorialMusic = _allSources[1];

        Audio.Pause();
    }

    void Update()
    {
        if (PauseManager.Instance.Paused)
        {
            Audio.Pause();
            return;
        }

        if (ReadyToPlay)
        {
            Audio.UnPause();
            _tutorialMusic.Stop();
        }

        if (_currentTimeStamp < _timeStamps.Count)
        {
            if (_currentTimeStamp > 0)
            {
                _timeFromPrevStamp = _timeStamps[_currentTimeStamp] - _timeStamps[_currentTimeStamp - 1];
                if (_minimumTimeDiff <= _timeFromPrevStamp) _canSpawnInRow = true;
            }


            if (_timeStamps[_currentTimeStamp] - 2.22 <= Audio.time)
            {
                if (_canSpawnInRow)
                {
                    _spawnLocation = Random.Range(0, 2);
                }
                else
                {
                    if (_spawnLocation == 0) _spawnLocation = 1;
                    else _spawnLocation = 0;
                }

                if (_spawnLocation == 0)
                    ShrimpSpawner.Instance.SpawnSwimmingShrimp(_timeStamps[_currentTimeStamp]);
                else
                    ShrimpSpawner.Instance.SpawnFlyingShrimp(_timeStamps[_currentTimeStamp]);
                _canSpawnInRow = false;
                _currentTimeStamp++;
            }
        }

        if (Audio.time >= Audio.clip.length)
        {
            ScoreHolder.Instance.ShowResults = true;
        }
    }
}
