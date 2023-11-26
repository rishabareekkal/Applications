using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class EnemyControl : MonoBehaviour
{
    [SerializeField] private Rigidbody2D _rb2D;
    [SerializeField] private BoxCollider2D _collider2D;
    float speedx;
    float speedy;


    // Start is called before the first frame update
    void Start()
    {
        _rb2D = GetComponent<Rigidbody2D>();
        _collider2D = GetComponent<BoxCollider2D>();
        speedx = 2f;
        speedy = 0.2f;
    }

    // Update is called once per frame
    void Update()
    {
        Vector2 position = transform.position;

        position = new Vector2(position.x - speedx * Time.deltaTime, position.y - speedy * Time.deltaTime);

        transform.position = position;

      //  Vector2 max = Camera.main.ViewportToWorldPoint(new Vector2(0, 0));

        if (transform.position.x < -4.4)
        {
            Destroy(gameObject);
        }
    }

    void OnTriggerEnter2D(Collider2D col)
    {
        if ((col.CompareTag("PlayerShipTag")) || (col.CompareTag("PlayerBulletTag")))
        {
            Destroy(gameObject);
            ScoreController.Instance.IncreaseScore();
        }
    }
}