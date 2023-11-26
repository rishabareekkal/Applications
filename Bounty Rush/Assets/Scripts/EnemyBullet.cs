using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class EnemyBullet : MonoBehaviour
{
    [SerializeField] private Rigidbody2D _rb2D;
    [SerializeField] private CircleCollider2D _collider2D;
    const float _speed = 8f;
    Vector2 _direction;
    bool isReady;

    void Awake()
    {
        _rb2D = GetComponent<Rigidbody2D>();
        _collider2D = GetComponent<CircleCollider2D>();
        isReady = false;
    }


    // Start is called before the first frame update
    void Start()
    {

    }

    public void SetDirection(Vector2 direction)
    {
        _direction = direction.normalized;

        isReady = true;
    }


    // Update is called once per frame
    void Update()
    {
        if (isReady)
        {
            Vector2 position = transform.position;

            position += _speed * Time.deltaTime * _direction;
            transform.position = position;

            Vector2 min = Camera.main.ViewportToWorldPoint(new Vector2(0, 0));
            Vector2 max = Camera.main.ViewportToWorldPoint(new Vector2(1, 1));

            if ((transform.position.x < min.x) || (transform.position.x > max.x) ||
                (transform.position.y < min.y) || (transform.position.y > max.y))
            {
                Destroy(gameObject);
            }
        }



    }

    void OnTriggerEnter2D(Collider2D col)
    {
        if (col.CompareTag("PlayerShipTag") || col.CompareTag("PlayerBulletTag"))
        {
            Destroy(gameObject);
        }
    }
}