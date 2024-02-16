using System.Collections;
using System.Collections.Generic;
using TMPro;
using Unity.VisualScripting;
using UnityEngine;

public class SwimmingShrimpController : MonoBehaviour
{

    private float _tempoX;
    private float _initialSpeed;
    private float _timeStamp;
    private SpriteRenderer[] _spriteRenderers;
    [SerializeField] private GameObject _hat;
    private int _randomNumber;

    void Start()
    {
        _spriteRenderers = GetComponentsInChildren<SpriteRenderer>();
        _tempoX = 4f;
        _initialSpeed = _tempoX;
        _timeStamp = ShrimpSpawner.Instance.CurrentTimeStamp;
        _randomNumber = Random.Range(0, 80);
        if (_randomNumber == 0)
        {
            foreach(SpriteRenderer spriteRenderer in _spriteRenderers)
                spriteRenderer.color = Color.black;
        }
    }

    // Update is called once per frame
    void Update()
    {
        if (PauseManager.Instance.Paused)
        {
            foreach (SpriteRenderer spriteRenderer in _spriteRenderers)
            {
                if (!spriteRenderer.enabled) break;
                spriteRenderer.enabled = false;
            }
        }
        else
        {
            foreach (SpriteRenderer spriteRenderer in _spriteRenderers)
            {
                if (spriteRenderer.enabled) break;
                spriteRenderer.enabled = true;
            }
        }

        if (!FileManager.Instance.Collectibles["Shrimp Hat"]) _hat.SetActive(false);

        Vector2 position = transform.position;
        position = new Vector2(position.x - _tempoX * Time.deltaTime, position.y);
        transform.position = position;

        if (transform.position.x < -3f)
            Destroy(gameObject);

        if (PlayerController.Instance.Guiders && _timeStamp - 0.2f <= GameMusicManager.Instance.Audio.time)
        {
            foreach (SpriteRenderer renderer in _spriteRenderers)
            {
                renderer.color = Color.red;
            }
        }
        if (_timeStamp - 0.1f <= GameMusicManager.Instance.Audio.time && GameMusicManager.Instance.Audio.time <= _timeStamp + 0.2f)
        {
            PlayerController.Instance.LowerAttackable = true;
            if (Input.GetKeyDown(KeyCode.DownArrow))
            {
                ScoreHolder.Instance.Score += 10;
                if (_randomNumber == 0) ScoreHolder.Instance.Score += 10;
                Destroy(gameObject);
                PlayerController.Instance.LowerAttackable = false;
            }
        }
        if (GameMusicManager.Instance.Audio.time > _timeStamp + 0.2f)
        {
            _tempoX = _initialSpeed * 2;
            foreach (SpriteRenderer renderer in _spriteRenderers)
            {
                renderer.color = Color.white;
                if (_randomNumber == 0)
                    renderer.color = Color.black;
            }
        }
        if (transform.position.x < 945) Destroy(gameObject);
    }
}
