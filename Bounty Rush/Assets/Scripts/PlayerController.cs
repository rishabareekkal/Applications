using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerController : MonoBehaviour
{
    public GameObject PlayerBulletGo;
    public GameObject BulletFiringPos;

    public AudioSource FireSound;

    [SerializeField] private float _speed = 5f;

    [SerializeField] private Rigidbody2D _rb2D;
    [SerializeField] private BoxCollider2D _collider2D;

    private const float _leftBorder = -4.725f;
    private const float _rightBorder = 4.725f;
    private const float _topBorder = 0f;
    private const float _bottomBorder = -5f;

    private Vector2 _movement;

    void Awake()
    {
        _rb2D = GetComponent<Rigidbody2D>();
        _collider2D = GetComponent<BoxCollider2D>();
    }

    void Update()
    {
        if (Input.GetKeyDown("space"))
        {
            FireSound.Play();

            GameObject bullet = (GameObject)Instantiate(PlayerBulletGo);
            bullet.transform.position = BulletFiringPos.transform.position;
        }

        _movement.x = Input.GetAxis("Horizontal");
        _movement.y = Input.GetAxis("Vertical");
    }

    void FixedUpdate()
    {
        if (_collider2D.bounds.center.x - _collider2D.bounds.size.x / 2 <= _leftBorder)
        {
            if (_movement.x < 0)
                _movement.x = 0;
        }
        if (_collider2D.bounds.center.x + _collider2D.bounds.size.x / 2 >= _rightBorder)
        {
            if (_movement.x > 0)
                _movement.x = 0;
        }
        if (_collider2D.bounds.center.y + _collider2D.bounds.size.y / 2 >= _topBorder)
        {
            if (_movement.y > 0)
                _movement.y = 0;
        }
        if (_collider2D.bounds.center.y - _collider2D.bounds.size.y / 2 <= _bottomBorder)
        {
            if (_movement.y < 0)
                _movement.y = 0;
        }
        _rb2D.MovePosition(_speed * Time.fixedDeltaTime * _movement + _rb2D.position);
    }

    void OnTriggerEnter2D(Collider2D col)
    {
        if ((col.CompareTag("EnemyShipTag")) || (col.CompareTag("EnemyBulletTag")))
        {
            HealthBar.Instance.TakeDamage();
        }
    }
}
