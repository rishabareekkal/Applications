using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerBullet : MonoBehaviour
{
    // Start is called before the first frame update
    [SerializeField] private Rigidbody2D _rb2D;
    [SerializeField] private CircleCollider2D _collider2D;
    private const float _speed = 8f;

    void Awake()
    {
        _rb2D = GetComponent<Rigidbody2D>();
        _collider2D = GetComponent<CircleCollider2D>();
    }

    // Update is called once per frame
    void Update()
    {
        Vector2 position = transform.position;

        position = new Vector2(position.x, position.y + _speed * Time.deltaTime);

        transform.position = position;

        Vector2 max = Camera.main.ViewportToWorldPoint(new Vector2(1, 1));

        if (transform.position.y > max.y)
        {
            Destroy(gameObject);
        }
    }

    void OnTriggerEnter2D(Collider2D col)
    {
        if (col.CompareTag("EnemyShipTag") || col.CompareTag("EnemyBulletTag"))
        {
            Destroy(gameObject);
        }
    }
}
